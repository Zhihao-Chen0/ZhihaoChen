import sqlite3

# Database setup
def create_connection():
    return sqlite3.connect("student.db")

# Create tables
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    # Create Users table
    cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS Users (
                    User_ID INTEGER PRIMARY KEY,
                    User_name TEXT NOT NULL,
                    User_email TEXT NOT NULL
                )
                ''')

    # Create Students table
    cursor.execute(''' 
                   CREATE TABLE IF NOT EXISTS Students (
                       Stu_ID INTEGER PRIMARY KEY,
                       Stu_name TEXT NOT NULL,
                       Stu_address TEXT NOT NULL
                   )
                   ''')
    

    conn.commit()
    conn.close()