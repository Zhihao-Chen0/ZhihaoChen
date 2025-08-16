#You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
#Create at least two Employee objects with different data.
#Call the display_info() method to show each employee’s details.
#Call the give_raise() method to increase an employee’s salary and display the updated amount

# Create Employee class
class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

# Method to display employee information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary:.2f}")
        print(f"Job Title: {self.job_title}")

# Method to give a raise to the employee
    def give_raise(self, amount):
        if amount < 0:
            print("Raise amount must be positive.")
            return
        self.salary += amount
        print(f"New Salary for {self.name} is {self.salary:.2f}")

# Method to handle employee raises
def handle_raise(employees):
    while True:
        name_input = input("Enter the employee's name to give a raise(enter 'exit' to quit): ").strip()
        if name_input.lower() == "exit":
            break

        found_employee = None
        for emp in employees:
            if emp.name.lower() == name_input.lower():
                found_employee = emp
                break

        if not found_employee:
            print("Employee not found.")
            continue

        try:
            amount_input = float(input(f"Enter the raise amount for {found_employee.name}: "))
            found_employee.give_raise(amount_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

# Main function to run the HR program
def main():
    employees = [
        Employee("Ben", 50000, "Cleaner"),
        Employee("Sam", 70000, "Manager"),
        Employee("Jack", 60000, "Data Analyst")
    ]

    print("_" * 20)
    print("Employee Information:")
    for emp in employees:
        emp.display_info()
    print("_" * 20)

    handle_raise(employees)

    print("\nUpdated Employee Information:")
    for emp in employees:
        emp.display_info()
    print("_" * 20)

# Entry point of the program
if __name__ == "__main__":
    main()
