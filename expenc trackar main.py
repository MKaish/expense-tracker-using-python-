import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_data()

    def load_data(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_data(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            expense = {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'amount': amount,
                'category': category,
                'description': description
            }

            self.expenses.append(expense)
            self.save_data()
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        for expense in self.expenses:
            print(f"{expense['date']} - {expense['category']} - ${expense['amount']:.2f}: {expense['description']}")

    def monthly_summary(self):
        monthly_totals = {}

        for expense in self.expenses:
            month = expense['date'][:7]
            monthly_totals[month] = monthly_totals.get(month, 0) + expense['amount']

        for month, total in monthly_totals.items():
            print(f"{month}: ${total:.2f}")

    def category_summary(self):
        category_totals = {}

        for expense in self.expenses:
            category = expense['category']
            category_totals[category] = category_totals.get(category, 0) + expense['amount']

        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")

    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Monthly Summary")
            print("4. Category Summary")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                amount = input("Enter amount: ")
                category = input("Enter category (e.g., Food, Transport): ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)

            elif choice == '2':
                self.view_expenses()

            elif choice == '3':
                self.monthly_summary()

            elif choice == '4':
                self.category_summary()

            elif choice == '5':
                print("Exiting Expense Tracker. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

if __name__ == '__main__':
    tracker = ExpenseTracker()
    tracker.run()
