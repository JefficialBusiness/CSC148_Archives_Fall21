# This program takes a social security numbers and outputs each number times itself in individual lines
def plot(s):
    for digit in s:  # Phases through each digit in the provided number
        print(digit, end=":")  # Separates digit from repeated digits first with a colon
        for j in range(int(digit)):  # Executes print statement below based on value of the individual digit
            print(digit, end="")
        print()


s = input("Enter social security number: ")  # Prompts user to input social security number for output of digits
plot(s)
