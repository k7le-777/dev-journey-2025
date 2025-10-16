"""
Zakat Calculator - Islamic Wealth Purification
Foundation for Mizaan zakat calculation feature

Quranic Foundation: Surah At-Tawbah 9:103
"Take from their wealth a charity to purify and cleanse them"

Nisab Thresholds:
- Gold: 85 grams
- Silver: 595 grams

Rate: 2.5% (one-fortieth) on wealth held for one lunar year

Author: Kyle Burns
Date: OCT 2025
"""

# Constants for nisab calculation
GOLD_NISAB_GRAMS = 85
SILVER_NISAB_GRAMS = 595
ZAKAT_RATE = 0.025 

# TODO: Function 1 - Display zakat introduction
def display_introduction():
    """
    Display explanation of zakat and its importance.
    Educate user about nisab and zakatable wealth.
    """
    print("\n" + "=" * 60)
    print("UNDERSTANDING ZAKAT - The Third Pillar of Islam")
    print("=" * 60)

    print("\n📖 What is Zakat?")
    print("Zakat is obligatory charity - one of the five pillars of Islam.")
    print("It is a responsibility every Muslim must fulfill once they reach")
    print("the nisab threshold and their wealth remains above it for one")
    print("full lunar year (hawl).")

    print("\n💰 What is Nisab?")
    print("Nisab is the minimum amount of wealth a Muslim must possess")
    print("before zakat becomes obligatory.")


    print("\nNisab thresholds:")
    print(f"  • Gold: {GOLD_NISAB_GRAMS}g (approximately)")
    print(f"  • Silver: {SILVER_NISAB_GRAMS}g (approximately)")

    print("\nIf your total wealth is below nisab, zakat is not obligatory.")
    print("Once your wealth stays above nisab for one lunar year (hawl),")
    print("you must pay 2.5% of your total zakatable wealth.")

    print("\n📚 Quranic Foundation")
    print("Surah Al-Baqarah 2:110:")
    print("'And establish prayer and give zakat...'")
    print()
    print("This ayah highlights that zakat is both a spiritual act of")
    print("worship and a practical form of social welfare in Islam.")

    print("\n✅ What Assets are Zakatable?")
    print("  • Cash and savings (in bank accounts)")
    print("  • Gold and silver (jewelry, coins, bullion)")
    print("  • Investment assets (stocks, shares, bonds)")
    print("  • Trade goods (business inventory)")
    print("  • Agricultural produce and livestock")
    print("  • Rental income and wealth-generating assets")

    print("\n❌ What is NOT Zakatable?")
    print("  • Primary residence (home you live in)")
    print("  • Personal transportation (your car)")
    print("  • Clothing and furniture")
    print("  • Tools needed for work")

    print("\nNote: These items only become zakatable if held for resale")
    print("or investment purposes.")
    
    print("\n" + "=" * 60)

# TODO: Function 2 - Get current gold/silver prices
def get_metal_prices():
    """
    Get current gold and silver prices per gram.
    For now, allow manual input (API integration later).
    
    Returns:
        dict: {'gold_price': float, 'silver_price': float}
    """
    # Your code here
    while True:
        try:
            gold_price = float(input("Enter current gold price per gram (£): "))
            if gold_price > 0:
                break
            else:
                print("Price must be positive!")
        except ValueError:
            print("Invalid input! Please enter a number.")
    while True:
        try:
            silver_price = float(input("Enter current silver price per gram (£): "))
            if silver_price > 0:
                break
            else:
                print("Price must be positive!")
        except ValueError:
            print("Invalid input! Please enter a number.")

    return {
        "gold_price": gold_price,
        "silver_price": silver_price
    }


# TODO: Function 3 - Calculate nisab threshold
def calculate_nisab(gold_price, silver_price):
    """
    Calculate nisab threshold using current metal prices.
    Use lower threshold (silver) as it's more charitable.
    
    Args:
        gold_price: Price per gram of gold
        silver_price: Price per gram of silver
    
    Returns:
        dict: {'gold_nisab': float, 'silver_nisab': float, 'nisab_used': float}
    """
    # Your code here
    gold_nisab = GOLD_NISAB_GRAMS * gold_price
    silver_nisab = SILVER_NISAB_GRAMS * silver_price

    nisab_used = min(gold_nisab, silver_nisab)

    return {
        "gold_nisab": gold_nisab,
        "silver_nisab": silver_nisab,
        "nisab_used": nisab_used
    }



# TODO: Function 4 - Get user's zakatable assets

def get_positive_number(prompt, allow_zero=False):
    while True:
        try:
            value = float(input(prompt))
            if value > 0 or (allow_zero and value >= 0):
                return value
            else:
                print("Must be positive!" if not allow_zero else "Must be zero or positive!")
        except ValueError:
            print("Invalid! Enter a number.")

def get_zakatable_assets():
 
    print("\n" + "=" * 60)
    print("ENTER YOUR ZAKATABLE ASSETS")
    print("=" * 60)
    print("Enter 0 for assets you don't have")
    print("All amounts in GBP (£)\n")

    assets = {}

    print("💵 Cash & Savings")
    assets["cash"] = get_positive_number("  Amount in savings/checking: £", allow_zero=True)

    print("\n🥇Gold")
    assets["gold_grams"] = get_positive_number("  Gold in grams (0 if none): ", allow_zero=True)

    print("\n🪙Silver")
    assets["silver_grams"] = get_positive_number("  Silver in grams (0 if none): ", allow_zero=True)

    print("\n💼 Business Inventory & Merchandise")
    assets["business_inventory"] = get_positive_number("  Amount in inventory/merchandise: £", allow_zero=True)

    print("\n📈 Halal Stocks & Investments")
    assets["investments"] = get_positive_number("  Amount in stocks/investments (strictly Halal): £", allow_zero=True)

    print("\n💰 Money Owed To You")
    assets["receivable_debts"] = get_positive_number("  Amount owed to you (receivable debts): £", allow_zero=True)

    return assets



# TODO: Function 5 - Calculate total zakatable wealth
def calculate_total_wealth(assets, gold_price, silver_price):
   
    gold_value = assets["gold_grams"] * gold_price
    silver_value = assets["silver_grams"] * silver_price

    total = (
        assets["cash"] +
        gold_value +
        silver_value +
        assets["business_inventory"] +
        assets["investments"] +
        assets["receivable_debts"]
    )

    return total



# TODO: Function 6 - Calculate zakat due
def calculate_zakat(total_wealth, nisab):
    """
    Determine if zakat is due and calculate amount.
    
    Args:
        total_wealth: Total zakatable wealth
        nisab: Nisab threshold
    
    Returns:
        dict: {'is_due': bool, 'zakat_amount': float}
    """
    if total_wealth >= nisab:
        zakat_amount = total_wealth * ZAKAT_RATE
        return {
            "is_due": True,
            "zakat_amount": zakat_amount
        }
    else:
        return {
            "is_due": False,
            "zakat_amount": 0.0
        }
    



# TODO: Function 7 - Display results
def display_results(assets, total_wealth, nisab, zakat_result):
    """
    Display comprehensive zakat calculation results.
    Show breakdown, educational info, and next steps.
    
    Args:
        assets: Dictionary of all assets
        total_wealth: Total zakatable wealth
        nisab: Nisab threshold used
        zakat_result: Zakat calculation result
    """
    # Your code here
    pass


# TODO: Main program
def main():
    """
    Main program flow for zakat calculator.
    """
    print("=" * 60)
    print("ZAKAT CALCULATOR - Islamic Wealth Purification")
    print("=" * 60)
    
    # Your code here:
    # 1. Display introduction
    # 2. Get metal prices
    # 3. Calculate nisab
    # 4. Get user's assets
    # 5. Calculate total wealth
    # 6. Calculate zakat
    # 7. Display results
    pass


# Run the program
if __name__ == "__main__":
    main()