from utils.welcome import welcome, handle_restart
from utils.record_expense import record_expense
from utils.clear_screen import clear_terminal
from utils.update_data import update_data
clear_terminal()

user_action = welcome()
valid_actions = ["1", "2", "3", "4", "5"]

while user_action not in valid_actions:
  clear_terminal()
  print(f"'{user_action}' is invalid. Try [1-5] for valid actions\n")
  user_action = welcome()

clear_terminal()


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
  handle_restart()

elif user_action == "2":
  pass

