def less_than_five(word_list):
    # Creates new list containing all words from word_list that have a length less than 5
    new_words = [word for word in word_list if len(word) < 5]
    return new_words


def less_than_five_filter(word):
    return len(word) < 5


thelist = ["hello", "does", "this", "haha", "wee", "work", "wooooo"]
filtered_list = list(filter(less_than_five_filter, thelist))
print(less_than_five(thelist))
print(filtered_list)
