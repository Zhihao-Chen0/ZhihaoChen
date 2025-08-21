from database import create_connection

def add_user():
    conn = create_connection()
    cursor = conn.cursor()

    try:
        User_ID = input("Enter User ID: ")
        User_name = input("Enter User Name: ")
        User_email = input("Enter User Email: ")
        sql = "INSERT INTO Users (User_ID, User_name,User_email)VALUES(?, ?, ?)"
        data = (User_ID, User_name, User_email)
        cursor.execute(sql, data)
        conn.commit()
        print("User added successfully.")
    except ValueError:
        print("Error: User ID must be a number.")
    finally:
        conn.close()

def delete_user():
    conn = create_connection()
    cursor = conn.cursor()

    user_id = input("Enter User ID to delete: ")
    sql = "DELETE FROM Users WHERE User_ID = ?"
    cursor.execute(sql, (user_id,))
    conn.commit()
    print(f"User with ID {user_id} deleted successfully.")
    conn.close()

def search_user():
    conn = create_connection()
    cursor = conn.cursor()
    user_id = input("Enter User ID to search: ")
    sql = "SELECT * FROM Users WHERE User_ID = ?"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchone()

    if result:
        print(f"User found: ID={result[0]}, Name={result[1]}, Email={result[2]}")
    else:
        print("User not found.")
    
    conn.close()

def get_info_user():
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Users"
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print("All user: ")
        for row in results:
            print(f"ID={row[0]}, Name={row[1]}, Email={row[2]}")
    else:
        print("No user found.")

    conn.close()
    
def add_student():
    conn = create_connection()
    cursor = conn.cursor()

    try:
        Stu_ID = input("Enter Student ID: ")
        Stu_name = input("Enter Student Name: ")
        Stu_address = input("Enter Student Address: ")

        sql = "INSERT INTO Students (Stu_ID, Stu_name, Stu_address)VALUES(?, ?, ?)"
        data = (Stu_ID, Stu_name, Stu_address)
        cursor.execute(sql, data)
        conn.commit()
    except ValueError:
        print("Error: Student ID must be a number.")
    finally:
        conn.close()

def delete_student():
    conn = create_connection()
    cursor = conn.cursor()
    stu_id = input("Enter Student ID to delete: ")
    sql = "DELETE FROM Students WHERE Stu_ID = ?"
    cursor.execute(sql, (stu_id,))
    conn.commit()
    print(f"Student with ID {stu_id} deleted successfully.")
    conn.close()

def search_student():
    conn = create_connection()
    cursor = conn.cursor()
    stu_id = input("Enter Student ID to search: ")
    sql = "SELECT * FROM Students WHERE Stu_ID = ?"
    cursor.execute(sql, (stu_id,))
    result = cursor.fetchone()

    if result:
        print(f"Student found: ID={result[0]}, Name={result[1]}, Address={result[2]}")
    else:
        print("Student not found.")
    
    conn.close()

    
def get_info_student():
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Students"
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print("All students: ")
        for row in results:
            print(f"ID={row[0]}, Name={row[1]}, Address={row[2]}")
    else:
        print("No student found.")

    conn.close()