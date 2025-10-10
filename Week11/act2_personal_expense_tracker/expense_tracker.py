"""This module provides a simple expense tracker with doctest support."""

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
 
    def add_expense(self, amount, category, description=""):
        """Add a new expense to the tracker.
        
        >>> tracker = ExpenseTracker()
        >>> tracker.add_expense(50, "Food", "Dinner")
        >>> len(tracker.get_all_expenses())
        1
        """
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)

    def get_total_expenses(self):
        """Calculate the total expenses.
        >>> tracker = ExpenseTracker()
        >>> tracker.add_expense(20, "Transport", "Bus")
        >>> tracker.add_expense(50, "Food", "Dinner")
        >>> tracker.get_total_expenses()
        70
        """
        return sum(expense["amount"] for expense in self.expenses)

    def get_expenses_by_category(self, category):
        """Get all expenses for a specific category.
        >>> tracker = ExpenseTracker()
        >>> tracker.add_expense(20, "Transport", "Bus")
        >>> tracker.add_expense(50, "Food", "Dinner")
        >>> len(tracker.get_expenses_by_category("Food"))
        1
        """
        return [expense for expense in self.expenses if expense["category"] == category]

    def get_all_expenses(self):
        """Get all recorded expenses.
        >>> tracker = ExpenseTracker()
        >>> tracker.add_expense(20, "Transport", "Bus")
        >>> tracker.add_expense(50, "Food", "Dinner")
        >>> len(tracker.get_all_expenses())
        2
        """
        return self.expenses

    def display_expenses(self, expenses=None):
        """Display given expenses in a formatted table."""
        if expenses is None:
            expenses = self.expenses
        if not expenses:
            print("No expenses recorded.")
            return

        # Table header
        print("+----+----------+----------------+---------------------------+")
        print("| No |  Amount  |    Category    |        Description        |")
        print("+----+----------+----------------+---------------------------+")

        # Table rows
        for idx, expense in enumerate(expenses, start=1):
            print("| {:<2} | ${:<7.2f} | {:<14} | {:<25} |".format(
                idx,
                expense['amount'],
                expense['category'],
                expense['description'] if expense['description'] else "-"
            ))
        print("+----+----------+----------------+---------------------------+")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense(50, "Food", "Ingredients for dinner")
    tracker.add_expense(30, "Food", "Dining out")
    tracker.add_expense(20, "Transport", "Bus ticket")
    tracker.add_expense(50, "Transport", "Gas")
    tracker.add_expense(100, "Entertainment", "Concert ticket")
    tracker.add_expense(200, "Entertainment", "Game purchase")

    print("\nAll Expenses:")
    tracker.display_expenses(tracker.get_all_expenses())

    print(f"Total Expenses: {tracker.get_total_expenses()}\n")

    print("\nFood Expenses:")
    tracker.display_expenses(tracker.get_expenses_by_category("Food"))

    print("\nTransport Expenses:")
    tracker.display_expenses(tracker.get_expenses_by_category("Transport"))

    print("\nEntertainment Expenses:")
    tracker.display_expenses(tracker.get_expenses_by_category("Entertainment"))

    import doctest
    doctest.testmod(verbose=True)