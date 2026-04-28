import csv
import json
from connect import connect


def show_rows(rows):
    for row in rows:
        print(row)


def insert_contact():
    conn = connect()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday YYYY-MM-DD: ")
    group_name = input("Group Family/Work/Friend/Other: ")
    phone = input("Phone: ")
    phone_type = input("Phone type home/work/mobile: ")

    cur.execute("""
        INSERT INTO groups (name)
        VALUES (%s)
        ON CONFLICT (name) DO NOTHING
    """, (group_name,))

    cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
    group_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO contacts (first_name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """, (name, email, birthday, group_id))

    contact_id = cur.fetchone()[0]

    cur.execute("""
        INSERT INTO phones (contact_id, phone, type)
        VALUES (%s, %s, %s)
    """, (contact_id, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")


def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY c.id
    """)

    show_rows(cur.fetchall())

    cur.close()
    conn.close()


def filter_by_group():
    group_name = input("Enter group: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.email, c.birthday, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
        ORDER BY c.first_name
    """, (group_name,))

    show_rows(cur.fetchall())

    cur.close()
    conn.close()


def search_by_email():
    query = input("Enter email part: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, first_name, email, birthday
        FROM contacts
        WHERE email ILIKE %s
        ORDER BY first_name
    """, (f"%{query}%",))

    show_rows(cur.fetchall())

    cur.close()
    conn.close()


def sort_contacts():
    print("1. Sort by name")
    print("2. Sort by birthday")
    print("3. Sort by date added")
    choice = input("Choose: ")

    if choice == "1":
        order_by = "first_name"
    elif choice == "2":
        order_by = "birthday"
    elif choice == "3":
        order_by = "id"
    else:
        print("Invalid choice!")
        return

    conn = connect()
    cur = conn.cursor()

    cur.execute(f"""
        SELECT id, first_name, email, birthday
        FROM contacts
        ORDER BY {order_by}
    """)

    show_rows(cur.fetchall())

    cur.close()
    conn.close()


def paginated_contacts():
    page = 0
    limit = 5

    while True:
        conn = connect()
        cur = conn.cursor()

        offset = page * limit

        cur.execute("""
            SELECT id, first_name, email, birthday
            FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (limit, offset))

        rows = cur.fetchall()

        print(f"\nPage {page + 1}")
        show_rows(rows)

        cur.close()
        conn.close()

        command = input("\nnext / prev / quit: ")

        if command == "next":
            page += 1
        elif command == "prev":
            if page > 0:
                page -= 1
        elif command == "quit":
            break
        else:
            print("Invalid command!")


def export_to_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.id, c.first_name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.id
    """)

    contacts = []

    for contact in cur.fetchall():
        contact_id, name, email, birthday, group_name = contact

        cur.execute("""
            SELECT phone, type
            FROM phones
            WHERE contact_id = %s
        """, (contact_id,))

        phones = cur.fetchall()

        contacts.append({
            "name": name,
            "email": email,
            "birthday": str(birthday),
            "group": group_name,
            "phones": [
                {"phone": p[0], "type": p[1]} for p in phones
            ]
        })

    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)

    cur.close()
    conn.close()
    print("Exported to contacts.json")


def import_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["first_name"]
            email = row["email"]
            birthday = row["birthday"]
            group_name = row["group"]
            phone = row["phone"]
            phone_type = row["type"]

            cur.execute("""
                INSERT INTO groups (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
            """, (group_name,))

            cur.execute("SELECT id FROM groups WHERE name = %s", (group_name,))
            group_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO contacts (first_name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (name, email, birthday, group_id))

            contact_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO phones (contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (contact_id, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported!")


def menu():
    while True:
        print("\n1. Add contact")
        print("2. Show all contacts")
        print("3. Filter by group")
        print("4. Search by email")
        print("5. Sort contacts")
        print("6. Paginated contacts")
        print("7. Export to JSON")
        print("8. Import from CSV")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_contact()
        elif choice == "2":
            show_all()
        elif choice == "3":
            filter_by_group()
        elif choice == "4":
            search_by_email()
        elif choice == "5":
            sort_contacts()
        elif choice == "6":
            paginated_contacts()
        elif choice == "7":
            export_to_json()
        elif choice == "8":
            import_from_csv()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


menu()