import json
import datetime

expenses = []

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

load_expenses()

def add_expense():
    try:
        name = input("Enter expense name: ")
        if not name.strip():
            print("Error: Expense name cannot be empty.")
            return
        
        amount_input = input("Enter expense amount: ")
        if not amount_input.strip():
            print("Error: Amount cannot be empty.")
            return
        
        amount = float(amount_input)
        if amount < 0:
            print("Error: Amount cannot be negative.")
            return
        
        category = input("Enter expense category: ")
        if not category.strip():
            print("Error: Category cannot be empty.")
            return
        
        date = input("Enter expense date (YYYY-MM-DD): ")
        if not date.strip():
            print("Error: Date cannot be empty.")
            return

        expense = {
            "name": name,
            "amount": amount,
            "category": category,
            "date": date,
        }
        expenses.append(expense)
        save_expenses()
        print("Expense added successfully.")
    except ValueError:
        print("Error: Please enter a valid amount (must be a number).")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("Expenses:")
    for expense in expenses:
        print(f"Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

def view_total_spending():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Spending: {total}")

def view_expenses_by_category():
    category = input("Enter category to filter: ")
    filtered_expenses = [expense for expense in expenses if expense['category'] == category]
    if not filtered_expenses:
        print("No expenses found for the specified category.")
        return

    print(f"Expenses in category '{category}':")
    for expense in filtered_expenses:
        print(f"Name: {expense['name']}, Amount: {expense['amount']}, Date: {expense['date']}")

def delete_expense():
    name = input("Enter the name of the expense to delete: ")
    for expense in expenses:
        if expense['name'] == name:
            expenses.remove(expense)
            save_expenses()
            print("Expense deleted successfully.")
            return
    print("Expense not found.")

def view_expenses_by_date():
    date = input("Enter date to filter (YYYY-MM-DD): ")
    filtered_expenses = [expense for expense in expenses if expense['date'] == date]
    if not filtered_expenses:
        print("No expenses found for the specified date.")
        return

    print(f"Expenses on {date}:")
    for expense in filtered_expenses:
        print(f"Name: {expense['name']}, Amount: {expense['amount']}, Category: {expense['category']}")

# Sample expense
# expense = {
#     "name": "Groceries",
#     "amount": 100,
#     "category": "Food",
#     "date": "2023-10-01"
# }
# expenses.append(expense)

load_expenses()
# Main menu loop
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. View Expenses by Category")
    print("5. Delete Expense")
    print("6. View Expenses by Date")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total_spending()
    elif choice == "4":
        view_expenses_by_category()
    elif choice == "5":
        delete_expense()
    elif choice == "6":
        view_expenses_by_date()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please choose a valid option.")



save_expenses()


