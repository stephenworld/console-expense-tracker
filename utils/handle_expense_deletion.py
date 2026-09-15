from utils.handle_history import show_all_expenses
from utils.handle_history import fetch_expenses
import json

json_file = "data.json"

def delete_expense(ID):
  try:
    with open(json_file, "r") as f:
      data = json.load(f)
  except FileNotFoundError:
    data = {}

  if ID in data:
    del data[ID]
    with open(json_file, "w") as f:
      json.dump(data, f, indent=2)
    print(f"Expense with ID: {ID} has been successfully deleted")
  else:
    print(f"Expense with ID: {ID} doesn't exist")

def handle_expense_deletion():
  show_all_expenses()
  expenses = fetch_expenses()
  if len(expenses) < 1:
    print("No expenses found.")
    return

  expense_id = input("\nEnter the ID of the expense you want to delete: ").strip()

  if expense_id not in expenses:
    print(f"Expense with ID: {expense_id} doesn't exist")
    return

  confirm = input(f"Are you sure you want to delete expense {expense_id}? (y/N): ").strip().lower()
  if confirm not in ["y", "yes"]:
    print("Deletion cancelled.")
    return

  delete_expense(expense_id)
  return



