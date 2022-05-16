# Function to determine price of a melon
def get_price(type, imported, quantity, month):
    if (month == "june" or month == "july" or month == "august"):
        price = 5
        if (type == "casabas" or type == "ogen"):
            price = price + 1
        elif (type == "square"):
            price = price * 2

        if (imported == True):
            price = price * 1.5
    else:
        print("Sorry, we are out of season. Please come back later.")
        return

    return price * quantity

type = input("What type of melon do you wish to buy? ")
imported = input("Do you wish to have your melon imported? ")
if imported == "yes":
    imported == True
else:
    imported == False

month = input("What month is it? ")
quantity = int(input("How many melons do you wish to buy? "))
print(get_price(type, imported, quantity, month))
