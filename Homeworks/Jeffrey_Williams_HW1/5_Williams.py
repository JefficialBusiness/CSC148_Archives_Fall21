# This program calculates and prints the remaining balance of a mortgage owed to the bank after 6 months

r = 0.002  # Represents Interest Rate in proper decimal form
c = 2000  # Represents Monthly Payment
t = 200000  # Represents total amount owed at month m
m = 0  # Represents month

for m in range(0, 6):  # Repeats below process until six months are reached, per the given range
    t = t + (t * r) - c  # Calculates interest payment and adds to total balance. Subtract monthly payment

# Presents projected remaining balance to user
print("After 6 months, your total mortgage owed to the bank will be $", t)
