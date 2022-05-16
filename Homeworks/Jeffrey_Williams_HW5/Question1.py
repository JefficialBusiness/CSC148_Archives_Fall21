# Problem Set 1
# Name: Jeffrey Williams
# Time Spent: 0:15
# Last Modified: Dec 7, 2021

def main():
    print(finddigits(15))
    print(finddigits(105))
    print(finddigits(15105))


def finddigits(number):
    """Function returns number of digits in a given number"""
    if number < 10:
        return 1
    else:
        return 1 + finddigits(number // 10)


main()
