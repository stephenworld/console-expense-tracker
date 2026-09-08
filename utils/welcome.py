from utils.clear_screen import clear_terminal
ACTIONS = [ "Record New Expense","View & Filter History","Spending Analytics","Export Data","Import Data", ]

def welcome():
  print("Spendr: \nA lightweight terminal expense tracker built to log, categorize, and analyze your daily spending without the bloat.\n")

  for idx, action in enumerate(ACTIONS):
    print(f"{idx+1}. {action}")

  print()
  return input("Selcet an action: ")


def handle_restart():
  res = input("\nWould you like to do anything else? (y/n): ").strip().lower()
  if res == "y":
    clear_terminal()
    welcome()
  else:
    exit()