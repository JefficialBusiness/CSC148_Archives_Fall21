# Problem Set 2
# Name: Jeffrey Williams
# Time Spent: 2:30
# Last Modified: Nov 6, 2021

def latin_square(order_square, top_left):
    """This function takes input from the user and prints a Latin Square based on the values provided"""
    print("The Latin Square is: ")
    # Nested for loops to create a square of numbers the height and width of the square order number
    for i in range(0, order_square):
        for j in range(0, order_square):
            top_left_new = top_left + i + j - 1  # Create new top left variable with iters., subtract to get row on top
            row = top_left_new % order_square + 1
            print(row, end=" ")
        print("")  # Creates new row, starts blank


order_square = int(input("Please input the order of square: "))
top_left = int(input("Please input the top left number: "))
latin_square(order_square, top_left)
