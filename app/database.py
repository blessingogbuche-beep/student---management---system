import sqlite3


def create_database():
    connection = sqlite3.connect("students.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            student_class TEXT NOT NULL,
            gender TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            parent_guardian TEXT NOT NULL,
            parent_email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

