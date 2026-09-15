from utils.welcome import welcome, handle_restart
from utils.record_expense import record_expense
from utils.clear_screen import clear_terminal
from utils.update_data import update_data
from utils.handle_history import handle_history
from utils.handle_analytics import handle_analytics
from utils.handle_expense_deletion import handle_expense_deletion

clear_terminal()

user_action = welcome()
valid_actions = ["1", "2", "3", "4", "5"]

while user_action not in valid_actions:
  clear_terminal()
  print(f"'{user_action}' is invalid. Try [1-4] for valid actions\n")
  user_action = welcome()

clear_terminal()

while True:
  if user_action == "1":
    """
    Record New Expense
    """
    title, description, category, amount = record_expense()  
    new_entry = {
      "title": title,
      "description": description,
      "category": category,
      "amount": amount,
    }
    clear_terminal()
    update_data(new_entry)
    user_action = handle_restart()

  elif user_action == "2":
    """
    View and filter History
    """
    clear_terminal()
    handle_history()
    user_action = handle_restart()

  elif user_action == "3":
    """
    Spending Analytics
    """
    clear_terminal()
    handle_analytics()
    user_action = handle_restart()

  elif user_action == "4":
    """
    Delete Expense
    """
    clear_terminal()
    handle_expense_deletion()
    user_action = handle_restart()

  elif user_action == "5":
      """
      Export Expenses to file
      """
      clear_terminal()
      print("WIP...")
      print("Exporting expenses to a file wip")
      user_action = handle_restart()

  elif user_action == "y":
    clear_terminal()
    user_action = welcome()

  elif user_action == "n":
    print("Exitted the program. Goodbye!")
    break

  else:
    clear_terminal()
    user_action = welcome()
