import random


def scramble(the_list):
    """This function scrambles the input word"""
    scramble_words = []  # Creates a new list for scrambled words
    # Goes through each word in the list of words
    for word in the_list:
        # Goes through each letter i in the word
        for i in range(len(word) - 1, 0, -1):
            # Assigns a random index variable j to pop from a random index in the word
            j = random.randint(0, len(word) - 1)
            # Modifies word by replacing original index value with random index value (got stuck, can't get to work
            # properly)
            word = word.replace(word[i], word[j])

        scramble_words.append(word)

    return scramble_words


print(scramble(['hello', 'does', 'it', 'work']))
