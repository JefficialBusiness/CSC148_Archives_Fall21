import csv

filename = 'table.csv'


def getList(filename):
    thelist = []
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in file:
            thelist.append(row)

    return thelist


thelist = getList(filename)
print(thelist)
