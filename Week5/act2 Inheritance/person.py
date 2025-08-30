class Person:
    def __init__(self, name, id, age, address):
        self.name = name
        self.id = id
        self.age = age
        self.address = address
        
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
