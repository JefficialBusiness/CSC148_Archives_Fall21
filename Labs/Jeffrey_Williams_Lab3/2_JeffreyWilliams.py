# This program prints a random number of greetings ("Hi")
import random


def rand_hi(name):
    for i in range(random.randint(1, 10)):  # Loops print statement below for the range of a random number from 1-10
        print("Hi,", name)


rand_hi("Jeff")
