class Person:
    def __init__(self, name, id, age, address):
        self.name = name
        self.id = id
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self, name, id, age, address, academic_record):
        super().__init__(name, id, age, address)
        self.academic_record = academic_record

    def display_info(self):
        super().display_info()
        print(f"Academic Record: {self.academic_record}")

class Staff(Person):
    def __init__(self, name, id, age, address, tax_code):
        super().__init__(name, id, age, address)
        self.tax_code = tax_code

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}")

class Academic(Staff):
    def __init__(self, name, id, age, address, tax_code, salary):
        super().__init__(name, id, age, address, tax_code)
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Salary: {self.salary}")

class General(Staff):
    def __init__(self, name, id, age, address, tax_code, pay_rate):
        super().__init__(name, id, age, address, tax_code)
        self.pay_rate = pay_rate

    def display_info(self):
        super().display_info()
        print(f"Pay Rate: {self.pay_rate}")


def main():
    student = Student("Alice", 1, 20, "123 Main St", {"Math": "A", "Science": "B"})
    academic_staff = Academic("Dr. Smith", 2, 45, "456 Elm St", "TAX123", 80000)
    general_staff = General("Mr. Johnson", 3, 38, "789 Oak St", "TAX456", 20)

    student.display_info()
    academic_staff.display_info()
    general_staff.display_info()

if __name__ == "__main__":
    main()

