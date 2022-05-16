# Problem Set 1
# Name: Jeffrey Williams
# Time Spent: 2:00
# Last Modified: Nov 5, 2021

def raw_input(outstanding, ann_int_rate, min_rate):
    """This function takes input from the user of their credit card's outstanding balance, monthly interest rate, and
    monthly payment rate and calculates the payments and remaining balances for a period of 12 months."""
    # Initialize variables for month, total amount paid
    month = 1
    total_paid = 0
    # Adjusts interest rate for a monthly basis
    mon_int_rate = ann_int_rate / 12

    # Code runs while 12 months have now yet been reached
    while month <= 12:
        # Assigns variables for payment information and balances by performing calculations
        min_payment = round((min_rate * outstanding), 2)
        total_paid = round((total_paid + min_payment), 2)
        int_payment = round((mon_int_rate * outstanding), 2)
        principal = round((min_payment - int_payment), 2)
        outstanding = round((outstanding - principal), 2)

        # Prints out all information regarding the information calculated above
        print()  # Empty row for better organization
        print("Month: ", month)
        print("Minimum Monthly Payment: ", min_payment)
        print("Interest Paid: ", int_payment)
        print("Principal Paid: ", principal)
        print("Remaining Balance: ", outstanding)

        # Increases/proceeds to next month by increment of 1
        month = month + 1

    # Prints total amount paid
    print()
    print("Remaining Balance after 12 Months: ", outstanding)
    print("Total Amount Paid after 12 Months: ", total_paid)


# Input from user as parameters for the function
outstanding = float(input("Enter the outstanding balance on your credit card: "))
ann_int_rate = float(input("Enter the annual credit card interest rate as a decimal: "))
min_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))

raw_input(outstanding, ann_int_rate, min_rate)
