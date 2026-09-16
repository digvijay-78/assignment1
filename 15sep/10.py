"""
Assignment 10: Personal Expense Calculator

 A person wants to calculate monthly expenses and savings.

Create a class ExpenseTracker with the following attributes:

Person name

Monthly salary

Rent

Food expenses

Travel expenses

Other expenses

Create the following methods:

calculate_total_expenses() – Calculate all expenses.

calculate_savings() – Calculate salary minus total expenses.

display_expense_report() – Display salary, expenses, and savings.

Formula:

Total Expenses = Rent + Food + Travel + Other Expenses
Savings = Monthly Salary - Total Expenses

Sample data:

Monthly Salary: 60000
Rent: 12000
Food: 8000
Travel: 5000
Other Expenses: 3000

Expected result:

Total Expenses: 28000
Savings: 32000
"""
class ExpenseTracker:
    def __init__(self):
        self.name=input("Enter name:")
        self.salary=int(input("Enter monthly salary:"))
        self.rent=int(input("Enter rent:"))
        self.food_expense=int(input("Enter food expense:"))
        self.travel_expense=int(input("Enter Travel expenses:"))
        self.other=int(input("Enter other expenses:"))
    def calculate_total_expenses(self):
        self.total=self.rent+self.food_expense+self.travel_expense+self.other
    def calculate_savings(self):
        self.saving=self.salary-self.total
    def display_expense_report(self):
        print("\nMonthly salary:",self.salary)
        print("Rent:",self.rent)
        print("Food:",self.travel_expense)
        print("Other expenses:",self.other)
        print()
        print("Total expenses:",self.total)
        print("saving:",self.saving)
e1=ExpenseTracker()
e1.calculate_total_expenses()
e1.calculate_savings()
e1.display_expense_report()                    