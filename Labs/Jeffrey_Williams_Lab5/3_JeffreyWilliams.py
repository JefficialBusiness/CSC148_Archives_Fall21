# This program takes 10 inputs from the user (numbers) and checks for the maximum odd number

# Variables to track iterations, odd number totals, and maximum odd number
count = 0
oddNumberCount = 0
maximum = 0

# Executes following code until 10 numbers are recorded
while count < 10:
    count = count + 1
    number = int(input("Enter a number: "))
    if number % 2 != 0:  # Checks if the number is odd by seeing if it can be divided with no remainder
        oddNumberCount = oddNumberCount + 1
        if number > maximum:  # Checks if number is larger to record the largest odd number
            maximum = number

# Checks if there are any odd numbers recorded, reports back how many, or if none were entered
if oddNumberCount > 0:
    print("Maximum odd number:", maximum)
else:
    print("You have not entered any odd numbers.")
