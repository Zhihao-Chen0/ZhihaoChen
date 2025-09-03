class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade

class Teacher:
    def __init__(self, name, subject):
        self.name = name       # public
        self._subject = subject # protected
        self.__salary = 50000   # private

    def get_salary(self):
        return self.__salary

s = Student('Ali', 20)
print(s.name)         # accessible
print(s._age)         # discouraged
print(s.get_grade())  # correct way

print("------------------------------")

t = Teacher('Mr. John', 'Mathematics')
print(t.name)          # accessible
print(t._subject)     # discouraged
print(t.get_salary())  # correct way
