from utils.clear_screen import clear_terminal
actions = ["Show all expenses", "Filter by category", "Filter by amount range", "Search by title"]

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
  print(f"Showing Expenses in Categorys\n")

  all_expenses = fetch_expenses()
  


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
    print("Filtering by amount range...")
  elif user_action == "4":
    """
    Search by title
    """
    print("Searching by title...")
