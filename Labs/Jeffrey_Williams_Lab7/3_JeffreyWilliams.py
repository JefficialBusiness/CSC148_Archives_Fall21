def reverse_list(word_list):
    # Initialize variables for first and last index to swap between
    first_index = 0
    last_index = (len(word_list) - 1)
    while first_index < last_index:
        a = word_list[first_index]  # Assigns variable to store value of first index before replacing
        word_list[first_index] = word_list[last_index]  # Swap variables, first with last
        word_list[last_index] = a  # Swap last variable with stored value of first variable

        # "Close in" on list, move on to next pair to swap symmetrically
        first_index = first_index + 1
        last_index = last_index - 1

    return word_list


thelist = ["coding", "is", "absolutely", "haha", "wee", "fun", "woo", "why"]

print(reverse_list(thelist))
