def merge_lists(list1, list2):
    """This function sorted numbers of the merged list in ascending order"""
    merge_list = []  # Create new list with all numbers sorted
    for i in range(len(list2)):
        for j in range(len(list1)):
            # Checks which value is greatest at first index in either list, appends smallest number to keep in order
            if list1[0] < list2[0]:
                merge_list.append(list1.pop(0))
            else:
                merge_list.append(list2.pop(0))

    # Checks whichever list has remaining numbers and adds those to the end
    merge_list.extend(list1)
    merge_list.extend(list2)

    return merge_list


print(merge_lists([1, 3, 5], [2, 7, 8]))
