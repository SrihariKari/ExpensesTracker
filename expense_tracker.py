import csv
import os

FILE_NAME = "expenses.csv"

expenses = []
monthly_budget = 0


# Load expenses from CSV file
def load_expenses():
    global expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"]),
                    "description": row["description"]
                })


# Save expenses to CSV file
def save_expenses():
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["date", "category", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

    print("Expenses saved successfully!")


# Add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/etc): ")

    try:
        amount = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount.")
        return

    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")


# View expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")
    for exp in expenses:
        if not all(k in exp for k in ("date", "category", "amount", "description")):
            print("Incomplete expense entry found.")
            continue

        print(f"Date: {exp['date']}")
        print(f"Category: {exp['category']}")
        print(f"Amount: {exp['amount']}")
        print(f"Description: {exp['description']}")
        print("--------------------")


# Set budget
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter monthly budget: "))
        print("Budget set successfully!")
    except ValueError:
        print("Invalid budget value.")


# Track budget
def track_budget():
    if monthly_budget == 0:
        print("Please set a budget first.")
        return

    total_expense = sum(exp["amount"] for exp in expenses)

    print(f"\nTotal Expenses: {total_expense}")
    print(f"Monthly Budget: {monthly_budget}")

    if total_expense > monthly_budget:
        print("⚠ You have exceeded your budget!")
    else:
        remaining = monthly_budget - total_expense
        print(f"You have {remaining} left for the month.")


# Menu
def menu():
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            set_budget()

        elif choice == "4":
            track_budget()

        elif choice == "5":
            save_expenses()

        elif choice == "6":
            save_expenses()
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please try again.")


# Main Program
if __name__ == "__main__":
    load_expenses()
    menu()