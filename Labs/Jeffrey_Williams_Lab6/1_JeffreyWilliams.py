def lesser_than(the_list, value):
    """This function returns: number of elements in the list strictly less than the value."""
    num_elements = 0  # Sets a value of elements less than provided number to return to user
    # Runs code below for all numbers in the list
    for i in the_list:
        # If each number in the list is less than the value given, the count of lesser numbers increases
        if i < value:
            num_elements = num_elements + 1

    return num_elements


print(lesser_than([1, 2, 3, 4, 5, 6, 7, 9], 7))
