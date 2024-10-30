import json
import os
from datetime import datetime

# File for storing financial data
FINANCE_FILE = 'finance_data.json'

# Load finance data from file
def load_data():
    if os.path.exists(FINANCE_FILE):
        with open(FINANCE_FILE, 'r') as file:
            return json.load(file)
    return {"balance": 0.0, "transactions": []}

# Save finance data to file
def save_data(data):
    with open(FINANCE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add income or expense
def add_transaction(data, amount, category, transaction_type):
    transaction = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount,
        "category": category,
        "type": transaction_type
    }
    data["transactions"].append(transaction)
    if transaction_type == "income":
        data["balance"] += amount
    elif transaction_type == "expense":
        data["balance"] -= amount
    save_data(data)
    print(f"{transaction_type.capitalize()} of {amount} added to {category}.")

# View all transactions
def view_transactions(data):
    if not data["transactions"]:
        print("No transactions recorded.")
        return
    print("\n--- Transactions ---")
    for t in data["transactions"]:
        type_sign = "+" if t["type"] == "income" else "-"
        print(f'{t["date"]}: {type_sign}${t["amount"]} ({t["category"]})')

# View balance
def view_balance(data):
    print(f'\nCurrent Balance: ${data["balance"]:.2f}')

# View summary by category
def view_summary(data):
    if not data["transactions"]:
        print("No transactions to summarize.")
        return
    summary = {}
    for t in data["transactions"]:
        if t["category"] not in summary:
            summary[t["category"]] = 0
        summary[t["category"]] += t["amount"] if t["type"] == "income" else -t["amount"]

    print("\n--- Summary by Category ---")
    for category, amount in summary.items():
        print(f'{category}: ${amount:.2f}')

# Command line interface
def main():
    data = load_data()

    while True:
        print("\n--- Personal Finance Tracker Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. View Summary by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter category for income (e.g., Salary, Freelance): ")
            add_transaction(data, amount, category, "income")

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter category for expense (e.g., Groceries, Rent): ")
            add_transaction(data, amount, category, "expense")

        elif choice == '3':
            view_balance(data)

        elif choice == '4':
            view_transactions(data)

        elif choice == '5':
            view_summary(data)

        elif choice == '6':
            print("Goodbye! Stay on top of your finances!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
