from utils.handle_history import fetch_expenses
from utils.clear_screen import clear_terminal
actions = ["View total spend", "Breakdown by category",]

def handle_analytics():
  for idx, action in enumerate(actions):
    print(f"{idx+1}. {action}")
    pass

  user_action = input("Select an action: ").strip()

  while user_action not in ["1", "2"]:
    print(f"'{user_action}' is an invalid action. Try [1-2] for valid actions\n")
    user_action = input("Select an action [1-2]: ").strip()

  if user_action == "1":
    """
    Show total spending
    """
    calculate_total_spending()
  elif user_action == "2":
    """
    Show breakdown by category
    """
    calculate_by_category()


def calculate_total_spending():
  """
  Show total spending
  """
  expenses = fetch_expenses()
  if not expenses:
    print("No expenses found.")
    return

  total_amount_spent = sum(expense['amount'] for expense in expenses.values())
  total_expenses = len(expenses)

  clear_terminal()
  print("-" * 60)
  print("Showing total spendings")
  print("-" * 60)

  print(f"Total spending: {total_amount_spent}")
  print(f"Total expenses: {total_expenses}")

def calculate_by_category():
  expenses = fetch_expenses()
  total_amount_spent = sum(expense['amount'] for expense in expenses.values())

  if not expenses:
    print("No expenses found.")
    return

  category_totals = {}
  for expense in expenses.values():
    category = expense['category']
    amount = expense['amount']
    if category in category_totals:
      category_totals[category] += amount
    else:
      category_totals[category] = amount

  clear_terminal()

  print("Spending Breakdown by Category:")
  print("-" * 60)
  print(f"{'Category':<30} {'Total Amount':<15}")
  print("-" * 60)
  for category, total in category_totals.items():
    print(f"{category:<30} {total:<15}")

  print("-" * 60)
  print(f"{"Total spending:":<30} {total_amount_spent:<30}")
  print("-" * 60)
