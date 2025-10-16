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

GOLD_NISAB_GRAMS = 85
SILVER_NISAB_GRAMS = 595
ZAKAT_RATE = 0.025 


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
    print("Once your wealth stays above nisab for one full lunar year (hawl),")
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


def get_metal_prices():
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


def calculate_nisab(gold_price, silver_price):
    gold_nisab = GOLD_NISAB_GRAMS * gold_price
    silver_nisab = SILVER_NISAB_GRAMS * silver_price
    nisab_used = min(gold_nisab, silver_nisab)
    return {
        "gold_nisab": gold_nisab,
        "silver_nisab": silver_nisab,
        "nisab_used": nisab_used
    }


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

    print("\n🪙 Silver")
    assets["silver_grams"] = get_positive_number("  Silver in grams (0 if none): ", allow_zero=True)

    print("\n💼 Business Inventory & Merchandise")
    assets["business_inventory"] = get_positive_number("  Amount in inventory/merchandise: £", allow_zero=True)

    print("\n📈 Halal Stocks & Investments")
    assets["investments"] = get_positive_number("  Amount in stocks/investments (strictly Halal): £", allow_zero=True)

    print("\n💰 Money Owed To You")
    assets["receivable_debts"] = get_positive_number("  Amount owed to you (receivable debts): £", allow_zero=True)

    return assets


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


def calculate_zakat(total_wealth, nisab):
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


def display_results(assets, total_wealth, nisab, zakat_result, gold_price, silver_price):
    print("\n" + "=" * 60)
    print("ZAKAT CALCULATION RESULTS")
    print("=" * 60)

    print("\n📊 YOUR ZAKATABLE ASSETS")
    print("-" * 60)

    gold_value = assets["gold_grams"] * gold_price
    silver_value = assets["silver_grams"] * silver_price

    print(f"💵 Cash & Savings: £{assets['cash']:.2f}")

    if assets["gold_grams"] > 0:
        print(f"🥇 Gold: {assets['gold_grams']:.2f}g × £{gold_price:.2f}/g = £{gold_value:.2f}")
    else:
        print(f"🥇 Gold: £0.00")
    
    if assets["silver_grams"] > 0:
        print(f"🪙 Silver: {assets['silver_grams']:.2f}g × £{silver_price:.2f}/g = £{silver_value:.2f}")
    else:
        print(f"🪙 Silver: £0.00")
    
    print(f"💼 Business Inventory: £{assets['business_inventory']:.2f}")
    print(f"📈 Halal Investments: £{assets['investments']:.2f}")
    print(f"💰 Receivable Debts: £{assets['receivable_debts']:.2f}")

    # Total Wealth
    print("\n" + "-" * 60)
    print(f"📈 TOTAL ZAKATABLE WEALTH: £{total_wealth:.2f}")
    print("-" * 60)
    # Nisab Info
    print(f"\n💎 Nisab Threshold Used: £{nisab:.2f}")
    print(f"   (Based on {SILVER_NISAB_GRAMS}g silver at £{silver_price:.2f}/g)")
    print(f"   Note: Using silver nisab as it's more charitable")

    # Zakat Result
    print("\n" + "=" * 60)
    if zakat_result["is_due"]:
        print("✅ ZAKAT IS DUE")
        print("=" * 60)
        print(f"\n💚 Your Zakat Amount: £{zakat_result['zakat_amount']:.2f}")
        print(f"   (2.5% of £{total_wealth:.2f})")
        
        # Educational content
        print("\n📖 What This Means:")
        print("   • You have met the nisab threshold")
        print("   • Zakat is obligatory (fard) on this wealth")
        print("   • Ensure this wealth has been in your possession")
        print("     for one full lunar year (hawl)")
        
        print("\n🎯 Next Steps:")
        print("   1. Verify the hawl (lunar year) requirement is met")
        print("   2. Distribute your zakat to eligible recipients")
        print("   3. Make intention (niyyah) for the sake of Allah")
        
        print("\n💡 Eligible Recipients (Quran 9:60):")
        print("   • The poor and needy")
        print("   • Those employed to collect zakat")
        print("   • Those whose hearts are to be reconciled")
        print("   • Those in bondage (freeing slaves/captives)")
        print("   • Those in debt")
        print("   • In the cause of Allah")
        print("   • The wayfarer (stranded traveler)")
        
        print("\n📅 Reminder:")
        print("   Set a date to calculate and pay zakat annually")
        print("   Many Muslims choose Ramadan for increased reward")
        
    else:
        print("ℹ️  ZAKAT NOT DUE")
        print("=" * 60)
        print(f"\nYour wealth (£{total_wealth:.2f}) is below the")
        print(f"nisab threshold (£{nisab:.2f})")
        
        difference = nisab - total_wealth
        print(f"\nYou would need £{difference:.2f} more to reach nisab")
        
        print("\n📖 What This Means:")
        print("   • Zakat is not obligatory on your current wealth")
        print("   • Continue building your savings Islamically")
        print("   • Voluntary charity (sadaqah) is always encouraged")
        
        print("\n💚 Consider Sadaqah:")
        print("   Even though zakat is not due, voluntary charity")
        print("   (sadaqah) is highly rewarded in Islam:")
        print("   'Charity does not decrease wealth' - Prophet ﷺ")
    
    print("\n" + "=" * 60)
    print("Alhamdulillah - May Allah accept your obedience")
    print("=" * 60 + "\n")


def main():
    """
    Main program flow for zakat calculator.
    """
    print("=" * 60)
    print("ZAKAT CALCULATOR - Islamic Wealth Purification")
    print("=" * 60)
    print("\n" + "=" * 60)
    print("ZAKAT CALCULATOR")
    print("Islamic Wealth Purification - Third Pillar of Islam")
    print("=" * 60)
    print("\nBismillah - In the name of Allah, the Most Merciful")

    display_introduction()
    input("\nPress Enter to begin calculation...")

    print("\n" + "=" * 60)
    print("STEP 1: CURRENT GOLD & SILVER PRICES")
    print("=" * 60)
    print("\nEnter today's market prices for gold and silver per gram.")
    print("You can find these at: kitco.com, goldprice.org, etc.")

    prices = get_metal_prices()
    nisab_info = calculate_nisab(prices["gold_price"], prices["silver_price"])

    print(f"\n✓ Nisab calculated:")
    print(f"  Gold nisab: £{nisab_info['gold_nisab']:.2f}")
    print(f"  Silver nisab: £{nisab_info['silver_nisab']:.2f}")
    print(f"  Using: £{nisab_info['nisab_used']:.2f} (lower threshold)")

    input("\nPress Enter to continue...")

    print("\n" + "=" * 60)
    print("STEP 2: YOUR ZAKATABLE ASSETS")
    print("=" * 60)
    print("\nWe'll now collect information about your zakatable wealth.")
    print("Remember: Only count wealth held for one full lunar year.")

    input("\nPress Enter when ready...")

    assets = get_zakatable_assets()
    total_wealth = calculate_total_wealth(
        assets, 
        prices["gold_price"], 
        prices["silver_price"]
    )

    print(f"\n✓ Total wealth calculated: £{total_wealth:.2f}")

    input("\nPress Enter to see your results...")

    zakat_result = calculate_zakat(total_wealth, nisab_info["nisab_used"])

    display_results(
        assets,
        total_wealth,
        nisab_info["nisab_used"],
        zakat_result,
        prices["gold_price"],
        prices["silver_price"]
    )

    print("\n🤲 JazakAllahu Khairan for using this calculator")
    print("May Allah accept your zakat and purify your wealth\n")


if __name__ == "__main__":
    main()