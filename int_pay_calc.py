def main():
    print(" Monthly Payment Loan Calculator")
    print("")

    principal = float(input("Enter the Loan Amount: "))
    april = float(input("Enter the Annual Interest Rate: "))
    years = float(input("Enter the Amount of Years: "))

    monthly_interest_rate = april / 1200
    amount_of_months = years * 12
    montly_payment = principal * monthly_interest_rate / \
        (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print("The Monthly Payment for the Loan is: %.2f " % montly_payment)


main()
