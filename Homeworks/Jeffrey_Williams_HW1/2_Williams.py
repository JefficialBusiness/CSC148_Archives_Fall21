# This program asks a person for their first name and age

# Asks user to input name and age
name = input("Hey, what is your name? ")
age = int(input("What is your age? "))

# Performs series of concatenations according to age value and prints
if (age >= 20) and (age <= 22):
    age = age ** 2
    print(name, age)
elif (age >= 25) and (age <= 30):
    age = age ** 0.5
    print(name, age)
elif age >= 35:
    print(name, "American University")
