print("Simple Loan Calculator")

while True:
    while True:
        try:
            principle_amount = float(input("\nEnter amount to be borrowed: "))
            if principle_amount < 0:
                print("Principle amount cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            interest_rate = float(input("Enter annual interest rate (%): "))
            if interest_rate < 0:
                print("Interest Rate cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            loan_duration = int(input("How many months would you like to pay your debt: "))
            if loan_duration < 0:
                print("Loan duration cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_gain_interest = 0
    month_no = 1
    i = 0
    remaining_balance = principle_amount
    monthly_amount = principle_amount / loan_duration

    while loan_duration != i:
        print(f"Total amount borrowed: {principle_amount}")
        print(f"Loan duration: {loan_duration} Months")

        monthly_principal_payment = principle_amount / loan_duration
        monthly_interest = remaining_balance * (interest_rate / 100)
        monthly_due = monthly_principal_payment + monthly_interest
        remaining_balance -= monthly_principal_payment

        print(f"\nMonth No: {month_no}")
        print(f"Monthly amount: {monthly_amount:.2f}")
        print(f"Interest Rate: {interest_rate}")
        print(f"Monthly Interest: {monthly_interest:.2f}")
        print(f"Monthly Due: {monthly_due:.2f}")
        print(f"Remaining Balance: {remaining_balance:.2f}\n")

        total_gain_interest += monthly_interest
        month_no += 1
        i += 1

    total_to_pay = principle_amount + total_gain_interest

    print(f"Total Gain Interest: {total_gain_interest:.2f}")
    print(f"Total Amount To Pay: {total_to_pay:.2f}")

    user_continue = input("Would you like to calculate another loan? (Y/N):").upper()
    if user_continue == "Y":
        continue
    elif user_continue == "N":
        print("Exiting program. Thank you!")
        break
    else:
        print("Invalid input, please type Y or N.")