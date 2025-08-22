import sqlite3
# Create a database connection
def create_connection():
    return sqlite3.connect("college_database.db")

# Create the necessary tables
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            student_email TEXT NOT NULL
        )
    ''')

    cursor.execute ('''
        CREATE TABLE IF NOT EXISTS Tutors (
            tutor_id INTEGER PRIMARY KEY,
            tutor_name TEXT NOT NULL,
            tutor_email TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            credits INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()