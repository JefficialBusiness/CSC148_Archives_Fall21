def has_duplicates(the_list):
    """This function checks for duplicates in a list, returning True if any exist and False otherwise"""
    duplicates = 0  # Default number of unique numbers as 0
    original = []
    for i in the_list:
        if i not in original:
            original.append(i)

    if original != the_list:
        return True
    else:
        return False


print(has_duplicates(["man", "man", "I", "hope", "this", "works"]))