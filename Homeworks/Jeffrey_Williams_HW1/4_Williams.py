# This program stores a person's name and repeats a greeting n times

import random


def multi_hello(xxx, n):
    for i in range(n):  # Allows the below line of code to run for any given range n
        print("Hello, ", xxx)  # Prints statement according to assigned range in loop


# Call function, assigning a name and a random number between 1 and 10 to parameter n
multi_hello("Jeff", random.randint(1, 10))
