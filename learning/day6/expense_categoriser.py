"""
Expense Categorizer - Islamic Spending Categories
Foundation for Mizaan balanced spending tracker

Quranic Foundation: Surah Al-Furqan 25:67
"And those who, when they spend, are neither extravagant nor niggardly,
but hold a medium way between those extremes."

Author: Kyle Burns
Date: Oct 2025
"""

# TODO: Function 1 - Display Islamic spending categories
def display_categories():
    """
    Display the four Islamic spending categories from research.
    
    Categories:
    1. Daruriyyat (Essentials) - Food, shelter, basic clothing, healthcare
    2. Hajiyyat (Needed) - Transportation, communication, modest comfort
    3. Tahsiniyyat (Improvements) - Quality upgrades, halal entertainment
    4. Israf (Wasteful) - Excessive spending, brand obsession, impulse buys
    """
    # Your code here
    print("\n📊 Islamic Spending Categories:")
    print("─" * 50)
    print("1. Daruriyyat (Essentials)")
    print("   - Food, shelter, basic clothing, healthcare \n")
    print("2. Hajiyyat (Needed)")
    print("   - Transportation, communication, modest comfort \n")
    print("3. Tahsiniyyat (Improvements)")
    print("   - Quality upgrades, halal entertainment \n")
    print("4. Israf (Wasteful)")
    print("   - Excessive spending, brand obsession, impulse buys \n")



# TODO: Function 2 - Get expense details from user
def get_expense_details():
    """
    Prompt user for expense amount and description.
    Validate that amount is a valid number.
    
    Returns:
        dict: Expense with amount and description
    """
    # Your code here
    pass


# TODO: Function 3 - Let user select category
def select_category():
    """
    Display category options and get user's choice.
    Validate the choice is 1, 2, 3, or 4.
    
    Returns:
        str: Category name (Daruriyyat, Hajiyyat, etc.)
    """
    # Your code here
    pass


# TODO: Function 4 - Display expense summary
def display_summary(expenses):
    """
    Show all entered expenses grouped by category.
    Calculate totals for each category.
    
    Args:
        expenses (list): List of expense dictionaries
    """
    # Your code here
    pass


# TODO: Main program loop
def main():
    """
    Main program that ties everything together.
    Loop until user is done entering expenses.
    """
    print("=" * 50)
    print("Islamic Expense Categorizer")
    print("Building toward Mizaan - Balanced Spending Tracker")
    print("=" * 50)
    print()
    
    # Your code here
    # 1. Create empty list for expenses
    # 2. Loop while user wants to continue
    # 3. Display categories
    # 4. Get expense details
    # 5. Get category selection
    # 6. Add to list
    # 7. Ask if they want to add another
    # 8. Display summary
    pass


# Run the program
if __name__ == "__main__":
    main()