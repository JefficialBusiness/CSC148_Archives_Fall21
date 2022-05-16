# Problem Set 1
# Name: Jeffrey Williams
# Time Spent: 3:30
# Last Modified: Dec 13, 2021

def main():
    print(ispal("GATTAG"))
    print(ispal("class"))
    print(find_palindrome("alice.txt"))


def ispal(theword):
    """Function checks if a string is a palindrome"""
    if len(theword) <= 1:
        return True
    else:
        if theword[0] == theword[len(theword) - 1]:
            return ispal(theword[1:-1])
        else:
            return False


def find_palindrome(filename):
    """Function opens a text file, establishes a list of its words and utilizes the ispal() function to look for
    palindromes in the file"""
    newlist = []
    file = open(filename, "r")
    reading = file.read()
    listofwords = reading.split()
    for word in listofwords:
        # Adds word to list if it meets palindrome requirements, is larger than length of 1 and not already in list
        if ispal(word) and len(word) > 1 and (word not in newlist):
            newlist.append(word)
    file.close()
    return newlist


main()
