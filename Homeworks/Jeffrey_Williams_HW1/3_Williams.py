# This program calculates the sum of even numbers smaller than 20

sum = 0  # Add variable to store the sum of all numbers, start at 0
for x in range(0, 20):  # Phases through following code for the range of 1 to 20, or 20 times
    if x % 2 == 0:  # Checks if the number is even by seeing if divisible by 2 with no remainder
        sum = sum + x  # For every number proven even, add it to the sum until range is reached

print(sum)  # Prints the final number stored in variable "sum"
