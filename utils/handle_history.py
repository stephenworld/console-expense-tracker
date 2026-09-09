actions = ["Show all transactions", "Filter by category", "Filter by amount range", "Search by title"]

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
    Show all transactions
    """
    print("Showing all transactions...")
  elif user_action == "2":
    """
    Filter by category
    """
    print("Filtering by category...")
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
