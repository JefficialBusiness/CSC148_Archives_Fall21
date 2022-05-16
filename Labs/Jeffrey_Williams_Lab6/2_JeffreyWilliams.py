def unique(the_list):
    """Returns: the number of unique elements in a list"""
    unique_list = []  # Create new list for unique numbers
    unique_numbers = 0  # Default number of unique numbers as 0
    # Code runs for each number in the_list
    for i in the_list:
        # Adds numbers from the_list not already in unique_list to keep track, increase count for each unique number
        if i not in unique_list:
            unique_numbers = unique_numbers + 1
            unique_list.append(i)

    return unique_numbers  # Return count of unique numbers


print(unique([5, 6, 7, 9, 9, 9]))
