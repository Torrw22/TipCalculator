import emoji

def calculate_tip(total_bill, tip_percentage):
    tip_amount = total_bill * (tip_percentage / 100)
    return tip_amount

def main():
    print("Welcome to the Tip Calculator " + emoji.emojize(":money_with_wings:"))

    try:
        total_bill = float(input("Enter the total bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage you want to leave (e.g., 15): "))

        if total_bill < 0 or tip_percentage < 0:
            print("Invalid input! Amounts and percentages must be positive.")
        else:
            tip = calculate_tip(total_bill, tip_percentage)
            total_amount = total_bill + tip

            print("\nCalculating tip...\n")
            print(f"Total bill amount: ${total_bill:.2f}")
            print(f"Tip amount ({tip_percentage}%): ${tip:.2f}")
            print(f"Total amount with tip: ${total_amount:.2f} " + emoji.emojize(":money_bag:"))

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()