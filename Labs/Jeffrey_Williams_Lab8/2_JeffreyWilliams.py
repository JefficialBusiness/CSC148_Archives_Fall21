file = open("election.txt")
wordlist = []  # List of words
length_list = {}  # Dictionary of words and their corresponding lengths
wordcount = {}  # Dictionary of words and their corresponding counts
values = []  # List of numbers in the word list and their following word

for line in file:
    line = line.lower()
    for word in line.split():
        wordlist.append(word)  # Adds each word from the file into the word list
        # Checks for punctuation in each word and removes them if found
        for letter in word:
            if letter in ",!.?:;-'()[]`/""":
                word = word.replace(letter, "")

        # Word counter
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

        length_list[word] = len(word)  # Adds length of word to dictionary for word and length

# List of numbers in word list with the word following it
for word in wordlist:
    if word.isnumeric():
        values.append("%s %s" % (str(word), wordlist[wordlist.index(word) + 1]))

# List of sorted words by length
sorted_word = sorted(length_list.items(), key=lambda item: item[1], reverse=True)

# Dictionary of all battleground states and candidates with the corresponding number of times mentioned
states_candidates = {word: count for word, count in wordcount.items() if word in ["pennsylvania", "georgia", "biden",
                                                                                  "trump", "nevada", "north carolina",
                                                                                  "arizona"]}

# Print all desired results
print(wordlist)
print(sorted_word)
print(states_candidates)
print(values)

file.close()
