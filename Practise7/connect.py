import psycopg2

def connect():
    return psycopg2.connect(
        database="phonebook_db",
        user="postgres",
        password="12345678",
        host="localhost",
        port="5432"
    )