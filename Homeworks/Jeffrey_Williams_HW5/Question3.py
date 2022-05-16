# Problem Set 3
# Name: Jeffrey Williams
# Time Spent: 5:30
# Last Modified: Dec 12, 2021

import turtle


def triangle(length):
    """Function draws one triangle"""
    board.forward(length)  # draw base
    board.left(120)
    board.forward(length)
    board.left(120)
    board.forward(length)
    board.left(120)


def sierpinski(length, order):
    """Function draws a Sierpinski Triangle given parameters of length and order."""
    if order == 0:
        triangle(length)

    else:
        sierpinski(length / 2, order - 1)
        board.forward(length / 2)
        sierpinski(length / 2, order - 1)
        board.right(180)
        board.forward(length / 2)
        board.right(180)
        board.left(60)
        board.forward(length / 2)
        board.right(60)
        sierpinski(length / 2, order - 1)
        board.left(60)
        board.right(180)
        board.forward(length / 2)
        board.right(180)
        board.right(60)


# Ask user for input
order = int(input("Enter the length of the triangle's sides: "))
length = int(input("Enter the order: "))

board = turtle.Turtle()
sierpinski(order, length)
turtle.done()  # Keeps turtle drawing open
