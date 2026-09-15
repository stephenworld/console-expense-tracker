# Spendr 💰

An offline-first, terminal-based expense tracker engineered for speed and simplicity. Log transactions, analyze spending by category, and manage your finances directly from your terminal without complicated setups.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Storage](#data-storage)
- [Contributing](#contributing)
- [License](#license)

## Features

✅ **Record Expenses** - Quickly log new transactions with title, description, category, and amount  
✅ **View History** - Display all recorded expenses with detailed information  
✅ **Filter Expenses** - Filter transactions by category, amount range, or title  
✅ **Spending Analytics** - View total spending and category-based breakdown  
✅ **Offline-First** - All data is stored locally in JSON format, no internet required  
✅ **Cross-Platform** - Works on Windows, macOS, and Linux  
✅ **Auto-Generated IDs** - Expenses are automatically assigned unique identifiers  
✅ **Input Validation** - Robust validation for all user inputs

## Requirements

- Python 3.7 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/console-expense-tracker.git
cd console-expense-tracker
```

2. Ensure Python is installed:

```bash
python --version
```

3. Run the application:

```bash
python main.py
```

## Usage

### Starting the Application

```bash
python main.py
```

You'll be greeted with a welcome screen showing five main options:

```
Spendr:
A lightweight terminal expense tracker built to log, categorize, and
analyze your daily spending without the bloat.

1. Record New Expense
2. View & Filter Expenses
3. Spending Analytics
4. Delete Expense
5. Export Expenses
```

### Option 1: Record New Expense

Enter the following details for each transaction:

- **Title**: Short name for the expense (e.g., "Coffee", "Groceries")
- **Description**: Optional details or notes about the transaction
- **Category**: Expense category (e.g., "Transportation", "Shopping", "Food")
- **Amount**: Numeric value spent (must be greater than 0)

Example:

```
Title: Coffee
Description: Espresso at the local cafe
Category: Food
Amount: 5
```

### Option 2: View & Filter Expenses

Browse your spending history with multiple filtering options:

- **Show all expenses** - Display all recorded transactions
- **Filter by category** - View expenses for a specific category
- **Filter by amount range** - Find expenses within a price range
- **Filter by title** - Search for specific expenses by name

### Option 3: Spending Analytics

Analyze your spending patterns:

- **View total spend** - See total amount spent and number of expenses
- **Breakdown by category** - Get a detailed breakdown of spending by category

### Option 4: Delete Expense

Remove unwanted or incorrect expense entries:

- View your expense history
- Select an expense by its ID
- Confirm deletion to remove the entry permanently

### Option 5: Export Expenses     # Main entry point and application loop
├── README.md                       # Project documentation
├── data.json                       # Auto-generated file storing all expenses
└── utils/
    ├── welcome.py                  # Welcome screen and restart handling
    ├── record_expense.py           # Expense input and validation
    ├── update_data.py              # Save expenses to data.json
    ├── handle_history.py           # View and filter expenses
    ├── handle_analytics.py         # Spending analytics
    ├── handle_expense_deletion.py  # Delete expense functionality
    └── clear_screen.py    ll be prompted to continue or exit. Press `n` to exit the application.

## Project Structure

```
console-expense-tracker/
├── main.py                    # Main entry point and application loop
├── README.md                  # Project documentation
├── data.json                  # Auto-generated file storing all expenses
└── utils/
    ├── welcome.py             # Welcome screen and restart handling
    ├── record_expense.py       # Expense input and validation
    ├── update_data.py          # Save expenses to data.json
    ├── handle_history.py       # View and filter expenses
    ├── handle_analytics.py     # Spending analytics
    └── clear_screen.py         # Cross-platform terminal clearing
```

## Data Storage

All expenses are stored in a `data.json` file in the application root directory. Each expense record contains:

```json
{
  "001": {
    "title": "Coffee",
    "description": "Morning coffee",
    "category": "Food",
    "amount": 5
  },
  "002": {
    "title": "Gas",
    "description": "",
    "category": "Transportation",
    "amount": 50
  }
}
```

**Note**: The `data.json` file is created automatically on first use. Make sure to back up this file regularly to avoid losing your expense data.

## Code Review Summary

### Strengths

- **Modular Architecture**: Well-organized code split into logical utility modules
- **Input Validation**: Robust validation for required fields and numeric inputs
- **Cross-Platform Support**: Uses platform-agnostic code for terminal operations
- **Simple Data Model**: JSON-based storage is lightweight and portable
- **Auto-ID Generation**: Automatically generates unique identifiers for expenses
- **User-Friendly**: Clear prompts and error messages guide users

### Recommendations for Future Enhancement
Complete data export functionality (CSV, PDF, Excel)
- Add date/timestamp tracking for expenses
- Add expense edit capabilities
- Include monthly/yearly spending reports
- Add category management (create, delete, rename)
- Implement recurring expense tracking
- Add password protection for sensitive data
- Include data visualization (charts, graphs)
- Add budget setting and alerts
- Include data visualization (charts, graphs)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License. See the LICENSE file for more details.
