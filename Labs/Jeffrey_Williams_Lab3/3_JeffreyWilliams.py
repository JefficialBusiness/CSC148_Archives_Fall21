# This program determines the discounted price of an item at a discount store after a certain amount of weeks

def new_price(initial_price, num_week):
    if num_week == 3:  # Checks for week number
        initial_price = initial_price - (initial_price * 0.25)  # Deduction for determining discounted price
        print(initial_price)  # Prints adjusted variable assigned to initial_price
    elif num_week == 4:
        initial_price = initial_price - (initial_price * 0.50)
        print(initial_price)
    elif num_week >= 5:  # Checks for week number to be equal or greater than 5, per discount policy
        initial_price = initial_price - (initial_price * 0.75)
        print(initial_price)
    else:  # Runs if num_week is something other than specified above (less than 3)
        print(initial_price)


# Call function with example price and week span
new_price(100, 5)
