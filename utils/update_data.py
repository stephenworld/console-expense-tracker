import json
json_file = "data.json"

def update_data(new_values):
  try:
      with open(json_file, "r") as file:
          data = json.load(file)
  except FileNotFoundError:
      data = {}

  # Automatically generate the next ID
  if data:
      """Extract all keys, convert them to integers, find the max, and add 1"""
      next_id_int = max(int(key) for key in data.keys()) + 1
  else:
      # If the file was empty, start at 1
      next_id_int = 1

  """Format the integer as a 3-digit zero-padded string (e.g., 2 becomes "002")"""
  new_id = f"{next_id_int:03d}"

  # Add the new entry and save it
  data[new_id] = new_values

  with open(json_file, "w") as file:
      json.dump(data, file, indent=2)

  print()
  print(f"Successfully added \"{new_values['title']}\" with automatically generated ID: {new_id}")
