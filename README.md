# python-capstone-finance-tracker
# Python Capstone Finance Tracker

A command-line personal finance tracker built in Python that allows users to log expenses, categorize them, and view financial summaries.

## Project Description

This personal finance tracker is a console-based application that helps users manage their expenses by:
- Adding expenses with descriptions, categories, and amounts
- Viewing all recorded expenses organized by category
- Displaying financial summaries with totals per category
- Handling invalid inputs gracefully with comprehensive error handling
- Providing a user-friendly menu-driven interface

## How to Run the Script

1. **Prerequisites**: Ensure you have Python 3.6 or higher installed on your system.

2. **Download**: Clone this repository or download the `finance_tracker.py` file.

3. **Run the program**:
   ```bash
   python finance_tracker.py
   ```
   or
   ```bash
   python3 finance_tracker.py
   ```

4. **Follow the menu**: Use the numbered menu options to navigate through the application.

## Program Features

### Menu Options
1. **Add Expense**: Record a new expense with description, category, and amount
2. **View All Expenses**: Display all expenses organized by category
3. **View Summary**: Show total spending per category and overall total
4. **Exit**: Close the application

### Input Validation
- Handles empty inputs for descriptions and categories
- Validates numeric input for amounts
- Prevents negative amounts
- Graceful error handling for unexpected inputs

## Python Concepts Demonstrated

This project showcases the following core Python programming concepts:

### Data Types and Variables
- **Strings**: Used for expense descriptions and categories
- **Floats**: Used for monetary amounts
- **Integers**: Used for menu choices and validation
- **Booleans**: Used in control flow logic

### Data Structures
- **Dictionaries**: Main data storage with categories as keys
- **Lists**: Store multiple expenses per category
- **Tuples**: Store individual expenses as (description, amount) pairs

### Control Structures
- **If/Elif/Else statements**: Menu logic and input validation
- **While loops**: Main program loop and input validation loops
- **For loops**: Iterating through expenses and categories

### Functions
- **Function definition and calls**: Modular code organization
- **Parameters and arguments**: Data passing between functions
- **Return statements**: Getting validated input from functions
- **Docstrings**: Function documentation

### String Operations
- **String methods**: `.strip()` for input cleaning
- **String formatting**: f-strings for output formatting
- **String validation**: Checking for empty inputs

### Exception Handling
- **Try-except blocks**: Handling ValueError, KeyboardInterrupt
- **Multiple exception types**: Different error scenarios
- **Graceful error recovery**: Continuing program execution after errors

### Built-in Functions
- **input()**: Getting user input
- **print()**: Displaying output
- **float()**: Type conversion
- **int()**: Type conversion
- **sum()**: Calculating totals
- **len()**: Checking data existence

### Advanced Concepts
- **List comprehensions**: Efficient data processing
- **Dictionary methods**: `.items()` for iteration
- **Conditional expressions**: Inline logic
- **Main guard**: `if __name__ == "__main__"`

## Sample Usage

```
Welcome to the Personal Finance Tracker!

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: 1

Enter expense description: Lunch at restaurant
Enter category: Food
Enter amount: 25.50
Expense added successfully.

What would you like to do?
1. Add Expense
2. View All Expenses
3. View Summary
4. Exit
Choose an option: 3

Summary:
------------------------------
Food: $25.50
------------------------------
Total Expenses: $25.50
```

## File Structure

```
python-capstone-finance-tracker/
│
├── finance_tracker.py    # Main application file
└── README.md            # Project documentation
```

## Future Enhancements

Potential improvements for this project could include:
- Data persistence (saving to/loading from files)
- Date tracking for expenses
- Budget setting and tracking
- Expense editing and deletion
- Data export functionality
- Graphical user interface

## Author

This project demonstrates fundamental Python programming concepts through a practical, real-world application suitable for beginners learning Python programming.
