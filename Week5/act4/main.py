from person import Student
from person import Academic
from person import General

def main():
    student = Student("Alice", 1, 20, "123 Main St", {"Math": "A", "Science": "B"})
    academic_staff = Academic("Dr. Smith", 2, 45, "456 Elm St", "TAX123", 80000)
    general_staff = General("Mr. Johnson", 3, 38, "789 Oak St", "TAX456", 20)

    student.display_info()
    academic_staff.display_info()
    general_staff.display_info()

if __name__ == "__main__":
    main()