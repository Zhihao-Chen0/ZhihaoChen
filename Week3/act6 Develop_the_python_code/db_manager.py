from database import create_connection

def add_student():
    conn = create_connection()
    cursor = conn.cursor()

    try:
        Student_ID = input("Enter student ID: ")
        if not Student_ID.isdigit():
            print("Error: Student ID must be a number.")
            return
        Student_Name = input("Enter student name: ")
        Student_Email = input("Enter student email: ")

        sql = "INSERT INTO Students (Student_ID, Student_Name, Student_Email) VALUES (?, ?, ?)"
        cursor.execute(sql, (Student_ID, Student_Name, Student_Email))
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print("Error occurred:", e)
    finally:
        conn.close()

def delete_student():
    conn = create_connection()
    cursor = conn.cursor()

    student_id = input("Enter student ID to delete: ")
    if not student_id.isdigit():
        print("Error: Student ID must be a number.")
        return
    
    sql = "DELETE FROM Students WHERE Student_ID = ?"
    cursor.execute(sql, (student_id,))
    conn.commit()
    print(f"Student with ID {student_id} deleted successfully.")
    conn.close()

def get_all_students():
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Students"
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print("Students:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    else:
        print("No students found.")

    conn.close()

def add_tutor():
    conn = create_connection()
    cursor = conn.cursor()

    try:
        Tutor_ID = input("Enter tutor ID: ")
        if not Tutor_ID.isdigit():
            print("Error: Tutor ID must be a number.")
            return

        Tutor_Name = input("Enter tutor name: ")
        Tutor_Email = input("Enter tutor email: ")
        sql = "INSERT INTO Tutors (Tutor_ID, Tutor_Name, Tutor_Email) VALUES (?, ?, ?)"
        cursor.execute(sql, (Tutor_ID, Tutor_Name, Tutor_Email))
        conn.commit()
        print("Tutor added successfully.")
    except Exception as e:
        print("Error occurred:", e)
    finally:
        conn.close()

def get_all_tutors():
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Tutors"
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print("Tutors:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    else:
        print("No tutors found.")

    conn.close()

def add_course():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        Course_ID = input("Enter course ID: ")
        if not Course_ID.isdigit():
            print("Course ID must be a number.")
            return
        Course_Name = input("Enter course name: ")
        Credits = input("Enter credits: ")
        if not Credits.isdigit():
            print("Credits must be a number.")
            return

        sql = "INSERT INTO Courses (Course_ID, Course_Name, Credits) VALUES (?, ?, ?)"
        cursor.execute(sql, (Course_ID, Course_Name, Credits))
        conn.commit()
        print("Course added successfully.")
    except Exception as e:
        print("Error occurred:", e)
    finally:
        conn.close()

def get_all_courses():
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Courses"
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print("All courses:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Credits: {row[2]}")
    else:
        print("No courses found.")

    conn.close()
