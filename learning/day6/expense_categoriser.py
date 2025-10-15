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

    while True:
        amount_text = input("Enter amount (£): ") 
        
        try:
            amount_number = float(amount_text)
            if amount_number > 0:
                break
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid amount! Please enter a number.")

    description = input("Enter description: ")

    expense = { 
        "amount": amount_number,
        "description": description
    }
    return expense
    
# TODO: Function 3 - Let user select category
def select_category():

    while True:
        print("\nSelect category:")
        print("1. Daruriyyat (Essentials)")
        print("2. Hajiyyat (Needed)")
        print("3. Tahsiniyyat (Improvements)")
        print("4. Israf (Wasteful)")
        
        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == "1": return "Daruriyyat"
        elif choice == "2": return "Hajiyyat"
        elif choice == "3": return "Tahsiniyyat"
        elif choice == "4": return "Israf"
        else: print("Invalid choice. Enter 1,2,3 or 4.")


# TODO: Function 4 - Display expense summary
def display_summary(expenses):
    
    print("\n" + "=" * 50)
    print("EXPENSE SUMMARY - Islamic Categories")
    print("=" * 50)

    categories = ["Daruriyyat", "Hajiyyat", "Tahsiniyyat", "Israf"]

    grand_total = 0
    israf_total = 0

    for category in categories:
        print(f"\n📊 {category}:")
        category_total = 0
        has_expenses = False

        for expense in expenses:
            if expense["category"] == category:
                has_expenses = True
                print(f"  • £{expense['amount']:.2f} - {expense['description']}")
                category_total += expense["amount"]

        if not has_expenses:
            print("  (No expenses in this category)")

        print(f"  Total: £{category_total:.2f}")

        grand_total += category_total
        if category == "Israf":
            israf_total = category_total

    print("\n" + "=" * 50)
    print(f"TOTAL SPENDING: £{grand_total:.2f}")
    print("=" * 50)

    if israf_total > 0:
        print("\n⚠️  WARNING: Wasteful spending detected!")
        print(f"You spent £{israf_total:.2f} on Israf (wasteful) items.")
        print("Consider redirecting this to savings or charity.")
        print("Quran 17:26 - 'Do not spend wastefully'")


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
    print("\nQuranic Foundation: Surah Al-Furqan 25:67")
    print("'Those who, when they spend, are neither")
    print("extravagant nor niggardly, but hold a medium")
    print("way between those extremes.'")
    print("=" * 50)

    
    # Your code here
    # 1. Create empty list for expenses
    # 2. Loop while user wants to continue
    # 3. Display categories
    # 4. Get expense details
    # 5. Get category selection
    # 6. Add to list
    # 7. Ask if they want to add another
    # 8. Display summary
    expenses = []

    while True:
        display_categories

        expense = get_expense_details()
        category = select_category()

        expense["category"] = category
        expenses.append(expense)
        print(f"\n✓ Added: £{expense['amount']:.2f} - {expense['description']} ({category})")

        another = input("\nAdd another expense? (y/n): ")
        if another.lower() != "y":
            break
    
    display_summary(expenses)

# Run the program
if __name__ == "__main__":
    main()