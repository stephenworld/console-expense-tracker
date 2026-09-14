from utils.clear_screen import clear_terminal
actions = ["Show all expenses", "Filter by category", "Filter by amount range", "Filter by title"]

def fetch_expenses():
  """
  Fetch all expenses from the data.json file
  """
  import json
  json_file = "data.json"

  try:
      with open(json_file, "r") as file:
          data = json.load(file)
  except FileNotFoundError:
      data = {}

  return data

def show_all_expenses():
  """
  Show all expenses
  """
  clear_terminal()
  print("Showing All Expenses:\n")
  expenses = fetch_expenses()
  print("-"*60)
  print(f"{'ID':<5} {'Title':<25} {'Category':<25}")
  print("-"*60)
  for expense in expenses:
    print(f"{expense:<5} {expenses[expense]['title']:<25} {expenses[expense]['category']:<25}")

def show_expenses_by_category():
  """
  Show expenses filtered by category
  """
  clear_terminal()
  print(f"Showing Expenses by Categories\n")

  all_expenses = fetch_expenses()
  if not all_expenses:
    print("No expenses found.")
    return
  
  categories = []

  for expense in all_expenses:
    category = all_expenses[expense]['category']
    if category not in categories:
      categories.append(category)

  print("-"*60)
  print(f"{'ID':<5} {'Title':<15} {'Category':<25} {'Amount':<10}")
  print("-"*60)

  for category in categories:
    for exp_id, details in all_expenses.items():
      if details['category'] == category:
        print(f"{exp_id:<5} {details['title']:<15} {details['category']:<25} {details['amount']:<10}")

def show_expenses_by_amount_range():
  """
  Show expenses filtered by amount
  """
  clear_terminal()
  print(f"Showing Expenses by Amount\n")
  
  all_expenses = fetch_expenses()
  if not all_expenses:
    print("No expenses found.")
    return

  print("-"*60)
  print(f"{'ID':<5} {'Title':<15} {'Category':<25} {'Amount':<10}")
  print("-"*60)

  sorted_expenses_by_amount = sorted(all_expenses.items(), key=lambda x: x[1]['amount'])

  for ex_id, expense in sorted_expenses_by_amount:
    print(f"{ex_id:<5} {expense['title']:<15} {expense['category']:<25} {expense['amount']:<10}")

def show_expenses_by_amount_title():
  """
  Show expenses filtered by title
  """
  clear_terminal()
  print(f"Showing Expenses by Title\n")
  
  all_expenses = fetch_expenses()
  if not all_expenses:
    print("No expenses found.")
    return

  print("-"*60)
  print(f"{'ID':<5} {'Title':<15} {'Category':<25} {'Amount':<10}")
  print("-"*60)

  sorted_expenses_by_amount = sorted(all_expenses.items(), key=lambda x: x[1]['title'])

  for ex_id, expense in sorted_expenses_by_amount:
    print(f"{ex_id:<5} {expense['title']:<15} {expense['category']:<25} {expense['amount']:<10}")


def handle_history():
  """
  View and filter History
  """

  for idx, action in enumerate(actions):
    print(f"{idx+1}. {action}")

  user_action = input("\nSelect an action: ").strip()

  while user_action not in ["1", "2", "3", "4"]:
    print(f"'{user_action}' is invalid. Try [1-4] for valid actions\n")
    user_action = input("Select an action [1-4]: ").strip()

  if user_action == "1":
    """
    Show all expenses
    """
    show_all_expenses()

  elif user_action == "2":
    """
    Filter by category
    """
    show_expenses_by_category()

  elif user_action == "3":
    """
    Filter by amount range
    """
    show_expenses_by_amount_range()
  elif user_action == "4":
    """
    Search by title
    """
    show_expenses_by_amount_title()
