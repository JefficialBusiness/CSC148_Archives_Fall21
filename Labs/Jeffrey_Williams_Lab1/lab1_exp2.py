# Print out the instruction messages and ask the user to input two numbers
num1 = int(input("This program computes the sum of two input integers. Now please enter the first integer:"))
num2 = int(input("Please enter the second integer:"))

# Compute the sum of the input integers
sum = num1 + num2

# Print out the result 
print("The sum of {} and {} is {}".format(num1, num2, sum))