# Problem Set 1
# Name: Jeffrey Williams
# Time Spent: 1:30
# Last Modified: Oct 10, 2021

"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Jeffrey Williams 5030143
Date:   Oct 10, 2021
"""

import ps11_a1

# Prompts user for currency type and amount inputs to store as variables
currency_from = str.lower(input("Enter the 3-letter code for the currency you want to convert from: "))
currency_to = str.lower(input("Enter the 3-letter code for the currency you want to convert to: "))
amount = int(input("Enter the amount you wish to convert: "))

# Takes inputs for currency types and amounts and produces output based on what is entered
if (currency_from == "usd") and (currency_to == "eur"):
    output = ps11_a1.usd_to_eur(amount)
    print("For %.2f USD, you can get %.4f EUR." % (amount, output))

elif (currency_from == "eur") and (currency_to == "usd"):
    output = ps11_a1.eur_to_usd(amount)
    print("For %.2f EUR, you can get %.4f USD." % (amount, output))

elif (currency_from == "usd") and (currency_to == "aud"):
    output = ps11_a1.usd_to_aud(amount)
    print("For %.2f USD, you can get %.4f AUD." % (amount, output))

elif (currency_from == "aud") and (currency_to == "usd"):
    output = ps11_a1.aud_to_usd(amount)
    print("For %.2f AUD, you can get %.4f USD." % (amount, output))

elif (currency_from == "usd") and (currency_to == "jpy"):
    output = ps11_a1.usd_to_jpy(amount)
    print("For %.2f USD, you can get %.4f JPY." % (amount, output))

elif (currency_from == "jpy") and (currency_to == "usd"):
    output = ps11_a1.jpy_to_usd(amount)
    print("For %.2f JPY, you can get %.4f USD." % (amount, output))

elif (currency_from == "usd") and (currency_to == "php"):
    output = ps11_a1.usd_to_php(amount)
    print("For %.2f USD, you can get %.4f PHP." % (amount, output))

elif (currency_from == "php") and (currency_to == "usd"):
    output = ps11_a1.php_to_usd(amount)
    print("For %.2f PHP, you can get %.4f USD." % (amount, output))
