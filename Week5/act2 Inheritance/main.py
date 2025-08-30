from person import Person
class Student(Person):
    def __init__(self, name, id, age, address, academic_record):
        super().__init__(name, id, age, address)
        self.academic_record = academic_record

class Staff(Person):
    def __init__(self, name, id, age, address, tax_code):
        super().__init__(name, id, age, address)
        self.tax_code = tax_code
    

class Academic(Staff):
    def __init__(self, name, id, age, address, tax_code, salary):
        super().__init__(name, id, age, address, tax_code)
        self.salary = salary

class General(Staff):
    def __init__(self, name, id, age, address, tax_code, pay_rate):
        super().__init__(name, id, age, address, tax_code)
        self.pay_rate = pay_rate

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