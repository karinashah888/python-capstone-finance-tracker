#!/usr/bin/env python3
"""
Personal Finance Tracker
A command-line application for tracking personal expenses with categorization.
"""

def print_welcome():
    """Print welcome message when the program starts."""
    print("Welcome to the Personal Finance Tracker!")
    print()

def add_expense(expenses_data):
    """
    Add a new expense to the expenses dictionary.
    
    Args:
        expenses_data (dict): Dictionary storing expenses by category
    """
    try:
        # Get expense description
        description = input("Enter expense description: ").strip()
        if not description:
            print("Description cannot be empty.")
            return
        
        # Get category
        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty.")
            return
        
        # Get amount with exception handling
        while True:
            try:
                amount_input = input("Enter amount: ").strip()
                if not amount_input:
                    print("Amount cannot be empty.")
                    continue
                
                amount = float(amount_input)
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue
        
        # Store expense as tuple (description, amount)
        expense = (description, amount)
        
        # Add to dictionary - if category doesn't exist, create new list
        if category not in expenses_data:
            expenses_data[category] = []
        
        expenses_data[category].append(expense)
        print("Expense added successfully.")
        print()
        
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_expenses(data):
    """
    Display all expenses organized by category.
    
    Args:
        data (dict): Dictionary containing expenses by category
    """
    if not data:
        print("No expenses recorded yet.")
        print()
        return
    
    print("All Expenses:")
    print("-" * 40)
    
    for category, expenses in data.items():
        print(f"Category: {category}")
        for description, amount in expenses:
            print(f"  - {description}: ${amount:.2f}")
        print()

def view_summary(data):
    """
    Display summary of total expenses by category.
    
    Args:
        data (dict): Dictionary containing expenses by category
    """
    if not data:
        print("No expenses recorded yet.")
        print()
        return
    
    print("Summary:")
    print("-" * 30)
    
    total_overall = 0
    
    for category, expenses in data.items():
        # Calculate total for category using sum() and list comprehension
        category_total = sum(amount for description, amount in expenses)
        print(f"{category}: ${category_total:.2f}")
        total_overall += category_total
    
    print("-" * 30)
    print(f"Total Expenses: ${total_overall:.2f}")
    print()

def display_menu():
    """Display the main menu options."""
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")

def get_menu_choice():
    """
    Get and validate menu choice from user.
    
    Returns:
        int: Valid menu choice (1-4)
    """
    while True:
        try:
            choice = input("Choose an option: ").strip()
            if not choice:
                print("Please enter a choice.")
                continue
            
            choice_num = int(choice)
            if choice_num not in [1, 2, 3, 4]:
                print("Please enter a number between 1 and 4.")
                continue
            
            return choice_num
            
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            return 4

def main():
    """Main program loop."""
    # Initialize expenses dictionary
    expenses = {}
    
    # Print welcome message
    print_welcome()
    
    # Main program loop
    while True:
        try:
            display_menu()
            choice = get_menu_choice()
            print()
            
            if choice == 1:
                add_expense(expenses)
            elif choice == 2:
                view_expenses(expenses)
            elif choice == 3:
                view_summary(expenses)
            elif choice == 4:
                print("Goodbye!")
                break
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()