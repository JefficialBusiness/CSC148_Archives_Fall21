def remove_adjacent(num_list):
    indexnumber = 0  # Initialize variable for iterating through list index

    # Code runs until index variable is the same as the length of number list (iterates through all numbers)
    while indexnumber != len(num_list):
        # If first index number is the same as previous index number, remove adjacent index number until not equal
        if num_list[indexnumber] == num_list[indexnumber-1]:
            num_list.remove(num_list[indexnumber-1])
            indexnumber = indexnumber - 1  # Iterate backwards one step until number is singular in list
        else:
            indexnumber = indexnumber + 1  # Iterate forwards to look for more similarities

    return num_list


print(remove_adjacent([1, 2, 2, 2, 3, 3, 4]))
