import unittest
from expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        """Set up a new ExpenseTracker instance before each test."""
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        """Test adding an expense."""
        self.tracker.add_expense(50, "Food", "Dinner")
        self.assertEqual(len(self.tracker.get_all_expenses()), 1)

    def test_get_total_expenses(self):
        """Test calculating total expenses."""
        self.tracker.add_expense(50, "Food", "Dinner")
        self.tracker.add_expense(30, "Transport", "Bus")
        self.assertEqual(self.tracker.get_total_expenses(), 80)

    def test_get_expenses_by_category(self):
        """Test getting expenses by category."""
        self.tracker.add_expense(50, "Food", "Dinner")
        self.tracker.add_expense(30, "Transport", "Bus")
        food_expenses = self.tracker.get_expenses_by_category("Food")
        self.assertEqual(len(food_expenses), 1)
        self.assertEqual(food_expenses[0]["description"], "Dinner")

    def test_get_all_expenses(self):
        """Test retrieving all expenses."""
        self.tracker.add_expense(50, "Food", "Dinner")
        self.tracker.add_expense(30, "Transport", "Bus")
        all_expenses = self.tracker.get_all_expenses()
        self.assertEqual(len(all_expenses), 2)
        self.assertEqual(all_expenses[0]["description"], "Dinner")
        self.assertEqual(all_expenses[1]["description"], "Bus")

    def test_display_expenses(self):
        """Test displaying expenses (output verification is manual)."""
        self.tracker.add_expense(50, "Food", "Dinner")
        self.tracker.add_expense(30, "Transport", "Bus")
        # This test is to ensure the method runs without error.
        try:
            self.tracker.display_expenses()
        except Exception as e:
            self.fail(f"display_expenses raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()