from person import Student
from person import Academic
from person import General

def main():
    student = Student("Alice", 1, 20, "123 Main St", {"Math": "A", "Science": "B"})
    academic_staff = Academic("Dr. Smith", 2, 45, "456 Elm St", "TAX123", 80000)
    general_staff = General("Mr. Johnson", 3, 38, "789 Oak St", "TAX456", 20)

    print("Student Information:")
    print(f"Name: {student.name}, ID: {student.id}, Age: {student.age}, Address: {student.address}, Academic Record: {student.academic_record}")

    print("\nAcademic Staff Information:")
    print(f"Name: {academic_staff.name}, ID: {academic_staff.id}, Age: {academic_staff.age}, Address: {academic_staff.address}, Tax Code: {academic_staff.tax_code}, Salary: {academic_staff.salary}")

    print("\nGeneral Staff Information:")
    print(f"Name: {general_staff.name}, ID: {general_staff.id}, Age: {general_staff.age}, Address: {general_staff.address}, Tax Code: {general_staff.tax_code}, Pay Rate: {general_staff.pay_rate}")

if __name__ == "__main__":
    main()