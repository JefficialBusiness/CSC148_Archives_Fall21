def input_heights():
    # Initialize lists to create
    info = []
    names = []
    heights = []

    # Code runs (asks for user imput) until "done" is entered as name
    while True:
        name = input("Enter the name of a person: ")
        if name == "done":
            break
        height = int(input("Enter the height of that person: "))

        # Adds individual input values to the appropriate lists
        names.append(name)
        heights.append(height)
        info = [list(i) for i in zip(names, heights)]  # Zips name/height to inner list and adds to new list

    return info


print(input_heights())
