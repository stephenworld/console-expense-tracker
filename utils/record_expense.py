
def record_expense():
  print("-" * (60 - 2))
  print("Record a New Expense".upper())
  print("Enter the transaction details below:")
  print("-" * (60 - 2))

  title = input("Title (e.g., Coffee, Fuel): ").strip().title()
  while title == "":
      print("REQUIRED FIELD")
      title = input("Title (e.g., Coffee, Fuel): ").strip().title()

  description = input("Description or note (optional): ").strip().capitalize()

  category = input("Category (e.g., Transportation, Shopping): ").strip().title()
  while category == "":
        print("REQUIRED FIELD")
        category = input("Category (e.g., Transportation, Shopping): ").strip().title()
  
  amount = input("Amount spent: ").strip()
  while type(amount) is not int:
    try:
        amount = int(amount)
    except ValueError:
      print("REQUIRED FIELD (e.g., 5000, 2000)")
      amount = input("Amount spent: ").strip()

  return title, description, category, amount