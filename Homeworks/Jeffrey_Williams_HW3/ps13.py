# Problem Set 3
# Name: Jeffrey Williams
# Time Spent: 5:30
# Last Modified: Nov 7, 2021

"""
Processing Data: Grades

This program processes grade information from a CSV file in order to calculate statistics, rank each student based on
their grade, and curve the grades via the square root.
"""

import csv
import math

with open('Grades.csv', newline="") as f:
    reader = csv.reader(f)
    data = list(reader)


def calculate_stats(the_list):
    """This function takes a list of numbers and calculates the mean, standard deviation, and the range by following
    the appropriate formulas for each number."""
    print("Statistics: ")

    # Finding the mean through mean formula: adding the sum of numbers and dividing by number of elements in list
    sum = 0
    for number in the_list:
        sum = sum + number
    the_mean = round(float(sum / len(the_list)), 2)
    print("Mean: ", the_mean)

    # Finding the standard deviation by following the standard deviation formula
    std_dev = 0
    for number in the_list:
        std_dev = std_dev + ((number - the_mean) ** 2)  # Add each number in list minus mean, squared
    std_dev = std_dev / len(the_list)  # Divide above calculation by number of elements in list
    std_dev = math.sqrt(std_dev)  # Take the square root of above calculation to get final result
    print("Standard deviation: ", round(std_dev, 2))

    # Finding the range of the list by sorting, subtract largest number at the end from smallest at the beginning
    the_list.sort()
    the_range = the_list[len(the_list) - 1] - the_list[0]
    print("Range: ", the_range)


def rank(grades):
    """This function takes a table (format: student, grade) and ranks the students based on their grades."""
    print("Grades, sorted by rank: ")

    # Swaps position of elements (grade and name) to sort in the order of grade percentages
    for grade in grades:
        a = grade[0]
        b = grade[1]
        grade[1] = a
        grade[0] = b

    grades.sort(reverse=True)  # Sorts the list of grades in the numerical order of grade

    # Swaps position of elements back to original and prints the list, which is now in numerical order based on grade
    for i in grades:
        c = i[0]
        d = i[1]
        i[0] = d
        i[1] = c
        print(i)


def curve_grades(grades):
    """This function curves a list of grades in the particular format (name, grade) by taking the square root of the
    original grade, returning the curved grade alongside the original."""
    print("Curved Grades: ")

    for i in grades:  # Iterate through each student/grade
        i[0] = i[0] + ": Original = " + i[1]  # Adds original grade to first index of the inner list + specifies orig.
        # Takes the original grade and curves it by taking the square root and multiplying by 10, create new value
        i[1] = float(i[1])
        curve = round((math.sqrt(i[1]) * 10), 2)
        i[1] = "Curved = " + str(curve)  # Specifies/adds curved grade to the list, replace index position of old grade.
        print(i)  # Prints curved grades.


# data[1:len(data)] = ignores the first column in the csv that just labels the values ("student", "grade")
calculate_stats([float(i[1]) for i in data[1:len(data)]])
print()
rank(data[1:len(data)])
print()
curve_grades(data[1:len(data)])
