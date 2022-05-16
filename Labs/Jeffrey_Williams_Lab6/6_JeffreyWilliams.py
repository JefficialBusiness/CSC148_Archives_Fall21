def return_index(the_list, target):
    """This function returns index of given target value given integers, or adds where it would be if inserted in order
    if it is not in the list"""
    index_value = 0  # Sets a value for the index number to print to user
    for i in range(len(the_list)):
        # Checks if target is in list, and returns which index value that target number is in
        if target in the_list:
            index_value = the_list.index(target)
        # If target is not in the list, it adds value to the end of list and sorts to get index if in numerical order
        else:
            the_list.insert(len(the_list), target)
            the_list = sorted(the_list)
            index_value = the_list.index(target)
        return index_value


print(return_index([1, 3, 5, 6], 5))
print(return_index([1, 3, 5, 7], 6))
