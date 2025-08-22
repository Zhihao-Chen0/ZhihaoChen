from database import create_table
from db_manager import (
    add_student,
    delete_student,
    get_all_students,
    add_tutor,
    get_all_tutors,
    add_course,
    get_all_courses
)

def main():
    create_table()

    while True:
        print("\n----------Yoobee College Database Management System----------")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View All Students")
        print("4. Add Tutor")
        print("5. View All Tutors")
        print("6. Add Course")
        print("7. View All Courses")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            get_all_students()
        elif choice == "4":
            add_tutor()
        elif choice == "5":
            get_all_tutors()
        elif choice == "6":
            add_course()
        elif choice == "7":
            get_all_courses()
        elif choice == "8":
            print("Exited")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
