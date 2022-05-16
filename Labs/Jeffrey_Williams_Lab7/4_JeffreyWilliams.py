def dot_product(u, v):
    sum = 0  # Initialize variable for sum to return

    # Iterates through one of the lists (doesn't matter due to same length)
    for number in range(len(v)):
        sum = sum + (u[number] * v[number])  # For each index in one list, multiply with corresponding index in other

    return sum


print(dot_product([1, 2, 1], [1, 4, 3]))
