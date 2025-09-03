class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade
    
    def grade_info(self):
        return f"{self.name}'s grade is {self.__grade}"

class Teacher:
    def __init__(self, name, subject):
        self.name = name       # public
        self._subject = subject # protected
        self.__salary = 50000   # private

    def get_salary(self):
        return self.__salary

    def need_raise(self):
        return self.__salary < 60000
    
    def display_info(self):
        return "Need a raise!" if self.need_raise() else "Salary is sufficient."

s = Student('Ali', 20)
print(s.name)         # accessible
print(s._age)         # discouraged
print(s.get_grade())  # correct way
print(s.grade_info())  # correct way

print("------------------------------")

t = Teacher('Mr. John', 'Mathematics')
print(t.name)          # accessible
print(t._subject)     # discouraged
print(t.get_salary())  # correct way
print(t.display_info()) # correct way
