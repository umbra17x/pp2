import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        phone VARCHAR(20)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully!")

def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV!")

def insert_from_console():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")

def update_contact():
    conn = connect()
    cur = conn.cursor()

    old_name = input("Enter contact name to update: ")
    new_name = input("Enter new name: ")
    new_phone = input("Enter new phone: ")

    cur.execute(
        """
        UPDATE phonebook
        SET first_name = %s, phone = %s
        WHERE first_name = %s
        """,
        (new_name, new_phone, old_name)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated!")

def query_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def query_by_name():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter name: ")

    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def query_by_phone():
    conn = connect()
    cur = conn.cursor()

    phone = input("Enter phone: ")

    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_by_name():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter name to delete: ")

    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted!")

def delete_by_phone():
    conn = connect()
    cur = conn.cursor()

    phone = input("Enter phone to delete: ")

    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted!")

def menu():
    while True:
        print("\n1. Create table")
        print("2. Insert from CSV")
        print("3. Insert from console")
        print("4. Update contact")
        print("5. Show all contacts")
        print("6. Search by name")
        print("7. Search by phone")
        print("8. Delete by name")
        print("9. Delete by phone")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            query_all()
        elif choice == "6":
            query_by_name()
        elif choice == "7":
            query_by_phone()
        elif choice == "8":
            delete_by_name()
        elif choice == "9":
            delete_by_phone()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

menu()