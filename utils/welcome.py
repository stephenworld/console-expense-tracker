from utils.clear_screen import clear_terminal
ACTIONS = [ "Record New Expense","View & Filter Expenses","Spending Analytics", "Delete Expense", "Export to .txt" ]

def welcome():
  print("Spendr: \nA lightweight terminal expense tracker built to log, categorize, and analyze your daily spending without the bloat.\n")

  for idx, action in enumerate(ACTIONS):
    print(f"{idx+1}. {action}")

  print()
  return input("Select an action: ")


def handle_restart():
  res = input("\nWould you like to do anything else? (y/n): ").strip().lower()
  while res not in ["y", "n"]:
    clear_terminal()
    print(f"'{res}' is an invalid action. Try [y/n] for valid actions")
    res = input("Would you like to do anything else? (y/n): ").strip().lower()
  return res