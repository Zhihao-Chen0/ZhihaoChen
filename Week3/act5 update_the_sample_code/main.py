from database import create_table
from db_manager import (
    add_user, 
    delete_user, 
    search_user, 
    get_info_user, 
    add_student, 
    delete_student, 
    search_student, 
    get_info_student
)

def main():
    create_table()

    while True:
        print("\n----------- Yoobee Database Management System -----------")
        print("1. Add User")
        print("2. Delete User")
        print("3. Search User")
        print("4. Get Info of Users")
        print("5. Add Student")
        print("6. Delete Student")
        print("7. Search Student")
        print("8. Get Info of Students")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            search_user()
        elif choice == '4':
            get_info_user()
        elif choice == '5':
            add_student()
        elif choice == '6':
            delete_student()
        elif choice == '7':
            search_student()
        elif choice == '8':
            get_info_student()
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()