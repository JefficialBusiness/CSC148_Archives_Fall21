# This program gives us the sum of all even values in a Fibonacci sequence with values no greater than given amount
import time

# Defines function for finding even sum for sequence with a given limit parameter
def fib_even_sum(limit):
    # Establishes variable to record sum, and numbers a and b that get added together
    sum = 0
    a = 1
    b = 1
    # Following code for as long as maximum value has not been met
    while (b < limit):
        c = a + b  # Establishes next number c by adding a and b
        # Assigns new values to a and b to continue sequence
        b = a
        a = c
        # Checks if each number is even and adds even numbers to sum variable
        if c % 2 == 0:
            sum = sum + c
    # Prints sum of all even values in sequence
    print("Sum of all even values in sequence that does not exceed %.d: %.d." % (limit, sum))

# Starts timer to measure length of time to get result, calls function with limit of 4000000
start = time.time()
fib_even_sum(4000000)
end = time.time()
print("Time taken to get result: ", (end - start))
