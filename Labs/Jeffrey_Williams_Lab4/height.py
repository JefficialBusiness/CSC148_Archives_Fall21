"""This module shows off three functions for converting height between
height_in_inches and feet_and_inches. It also shows how to use variables to represent constants: values given a name
in order to remember them better."""

# constant
inches_per_foot = 12


def to_inches(feet, inches):
    inches_only = (feet * inches_per_foot) + inches
    return inches_only

def get_feet(height_in_inches):
    feet_comp = height_in_inches // inches_per_foot
    return feet_comp

def get_inches_left(height_in_inches):
    inches_comp = height_in_inches % inches_per_foot
    return inches_comp
