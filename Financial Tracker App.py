#  I'm going to import sqlite3 to create a database for my tracker app.
import sqlite3

#  import datetime to get the current date and time
from datetime import datetime

#  I'm going to create a connection to the database
#  I'm going to create a cursor object to execute SQL commands
def initialize_db():
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()

#  I'm going to create a table for the trackers for expenses   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses
        (id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        date TEXT)
    ''')

#  I'm going to create a table for income
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income
        (id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        date TEXT)
    ''')

#  I'm going to create a table for budget
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS budget
        (id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        date TEXT)
    ''')

#  I'm going to create a table for financial goals
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS goals
        (id INTEGER PRIMARY KEY,
        goal TEXT,
        target_amount REAL,
        current_amount REAL,
        date TEXT)
    ''')

    conn.commit()
    conn.close()

#  Called to initialize the database and create the tables.
initialize_db()

#  I'm going to create a function to add an expense to the database.
#  I'm going to connect to the database and create a cursor
#  object to execute SQL commands.
def add_expense(category, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (category, amount, date)
        VALUES (?, ?, ?)
    ''', (category, amount, date))
    conn.commit()
    conn.close()
    print(f"Expense '{category}' added successfully!")

# I'm going to create a function to add income to the database.
#  I'm going to connect to the database and create a cursor
#  object to execute SQL commands.
def add_income(category, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO income (category, amount, date)
        VALUES (?, ?, ?)
    ''', (category, amount, date))
    conn.commit()
    conn.close()
    print(f"Income '{category}' added successfully!")

#  I'm going to create a function to add a budget to the database.
#  I'm going to connect to the database and create a cursor
#  object to execute SQL commands.
def add_budget(category, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO budget (category, amount, date)
        VALUES (?, ?, ?)
    ''', (category, amount, date))
    conn.commit()
    conn.close()
    print(f"Budget '{category}' added successfully!")

#  I'm going to create a function to add a financial goal to the database.
#  I'm going to connect to the database and create a cursor
#  object to execute SQL commands.
def add_goal(goal, target_amount, current_amount):
    date = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO goals (goal, target_amount, current_amount, date)
        VALUES (?, ?, ?, ?)
    ''', (goal, target_amount, current_amount, date))
    conn.commit()
    conn.close()
    print(f"Goal '{goal}' added successfully!")

#  Created a programme that can be used by the user to view their expenses.
#  Create a function to view all expenses in the database.
#  Created a menu function to display the options to the user.
def display_menu():
    print("\n======== Welcome to the Financial Tracker App =========")
    print("Please select an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Expenses by Category")
    print("4. Add Income")
    print("5. View Income")
    print("6. View Income by Category")
    print("7. Set Budget for a category")
    print("8. View Budget for a category")
    print("9. Set Financial Goal")
    print("10. View progress towards Financial Goal")
    print("0. Exit")
    print("=========================================")

#  I'm going to connect menu options to the functions I created above.
#  I'm going to create a loop to keep the program running
#  until the user chooses to exit.
def main():
    while True:
        display_menu()
        choice = input("Please enter your choice (0 - 10): ")

        if choice == '1':
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            add_expense(category, amount)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            category = input("Enter the category to view expenses: ")
            view_expenses_by_category(category)

        elif choice == '4':
            category = input("Enter the income category: ")
            amount = float(input("Enter the income amount: "))
            add_income(category, amount)

        elif choice == '5':
            view_income()

        elif choice == '6':
            category = input("Enter the category to view income: ")
            view_income_by_category(category)

        elif choice == '7':
            category = input("Enter the budget category: ")
            amount = float(input("Enter the budget amount: "))
            add_budget(category, amount)

        elif choice == '8':
            category = input("Enter the category to view budget: ")
            view_budget_by_category(category)

        elif choice == '9':
            goal = input("Enter your financial goal: ")
            target_amount = float(input("Enter the target amount: "))
            current_amount = float(input("Enter the current amount towards the goal: "))
            add_goal(goal, target_amount, current_amount)

        #  Placeholder for future feature to reduce crashes.
        elif choice == '10':
            view_goal_progress()

        elif choice == '0':
            print("Thank you for using the Financial Tracker App!")
            break

        else:
            print("Invalid choice. Please try again.")

#  I'm going to create a function to view all expenses in the database.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_expenses():
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if expenses:
        total = 0
        print("\n======== Expenses ========")
        for expense in expenses:
            print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Date: {expense[3]}")
            total += expense[2]
        print(f"Total Expenses: {total}")

    else:
        print("No expenses found.")

    conn.close()

#  I'm going to create a function to view expenses by category.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_expenses_by_category(category):
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    expenses = cursor.fetchall()

    if expenses:
        print(f"\n======== Expenses for '{category}' ========")
        for expense in expenses:
            print(f"ID: {expense[0]}, Category: {expense[1]}, Amount: {expense[2]}, Date: {expense[3]}")
    else:
        print(f"No expenses found for category '{category}'.")

    conn.close()

#  I'm going to create a function to view all budget in the database.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_budget():
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budget")
    budget = cursor.fetchall()

    if budget:
        print("\n======== Budget ========")
        for bud in budget:
            print(f"ID: {bud[0]}, Category: {bud[1]}, Amount: {bud[2]}, Date: {bud[3]}")
    else:
        print("No budget found.")

    conn.close()

#  I'm going to create a function to view budget by category.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_budget_by_category(category):
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM budget WHERE category = ?", (category,))
    budget = cursor.fetchall()

    if budget:
        print(f"\n======== Budget for '{category}' ========")
        for bud in budget:
            print(f"ID: {bud[0]}, Category: {bud[1]}, Amount: {bud[2]}, Date: {bud[3]}")
    else:
        print(f"No budget found for category '{category}'.")

    conn.close()

#  I'm going to create a function to view all income in the database.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_income():
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income")
    income = cursor.fetchall()

    if income:
        print("\n======== Income ========")
        for inc in income:
            print(f"ID: {inc[0]}, Category: {inc[1]}, Amount: {inc[2]}, Date: {inc[3]}")
    else:
        print("No income found.")

    conn.close()

#  I'm going to create a function to view income by category.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_income_by_category(category):
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM income WHERE category = ?", (category,))
    income = cursor.fetchall()

    if income:
        print(f"\n======== Income for '{category}' ========")
        for inc in income:
            print(f"ID: {inc[0]}, Category: {inc[1]}, Amount: {inc[2]}, Date: {inc[3]}")
    else:
        print(f"No income found for category '{category}'.")

    conn.close()

#  I'm going to create a function to view progress towards a financial goal.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_goal_progress():
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM goals")
    goals = cursor.fetchall()

    if goals:
        print("\n======== Financial Goals ========")
        for goal in goals:
            print(f"ID: {goal[0]}, Goal: {goal[1]}, Target Amount: {goal[2]}, Current Amount: {goal[3]}, Date: {goal[4]}")
    else:
        print("No financial goals found.")

    conn.close()

#  I'm going to create a function to view all financial goals in the database.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_goals():
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM goals")
    goals = cursor.fetchall()

    if goals:
        print("\n======== Financial Goals ========")
        for goal in goals:
            print(f"ID: {goal[0]}, Goal: {goal[1]}, Target Amount: {goal[2]}, Current Amount: {goal[3]}, Date: {goal[4]}")
    else:
        print("No financial goals found.")

    conn.close()

#  I'm going to create a function to view progress towards
#  a financial goal by category.
#  I'm going to connect to the database and create a cursor.
#  object to execute SQL commands.
def view_goal_progress_by_category(category):
    conn = sqlite3.connect('tracker_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM goals WHERE goal = ?", (category,))
    goals = cursor.fetchall()

    if goals:
        print(f"\n======== Financial Goals for '{category}' ========")
        for goal in goals:
            print(f"ID: {goal[0]}, Goal: {goal[1]}, Target Amount: {goal[2]}, Current Amount: {goal[3]}, Date: {goal[4]}")
    else:
        print(f"No financial goals found for category '{category}'.")

    conn.close()

#  I'm going to call the main function to run the programme.
main()
