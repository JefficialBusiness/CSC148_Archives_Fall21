the_portfolio = [("25-Jan-2001", 43.50, 25, 'CAT', 92.45), ("25-Jan-2001", 42.80, 50, 'DD', 51.19),
                 ("25-Jan-2001", 42.10, 75, 'EK', 34.87), ("25-Jan-2001", 37.58, 100, 'GM', 37.58)]


def findtotalpurchaseprice(portfolio):
    # Initialize variables for whole portfolio total and block number to print
    total = 0
    blocknum = 1

    # Iterate through all blocks in portfolio
    for block in portfolio:
        # Multiply share index with purchase price index, add to sum
        totalpurchaseprice = (block[1] * block[2])
        total = total + totalpurchaseprice
        # Print total purchase price (product of indexes) for each block
        print("Total Purchase Price for Block %i: %.2f" % (blocknum, (block[1] * block[2])))
        blocknum = blocknum + 1

    print("The total purchase price of the entire portfolio is: %.2f" % total)


def findtotalshare(portfolio):
    # Initialize variable for block to print
    blocknum = 1

    # Iterate through all blocks in portfolio
    for block in portfolio:
        totalpurchaseprice = block[2] * block[1]  # Multiply share index with purchase price, create new prod variable
        totalcurrentprice = block[2] * block[4]  # Multiply share index with current price, create new prod variable
        # Print out information for each block for total purchase price and current price to show differences
        print("Block: %i - Total Purchase Price: %.2f. Total Current Price: %.2f." % (blocknum, totalpurchaseprice,
                                                                                      totalcurrentprice))
        blocknum = blocknum + 1


findtotalpurchaseprice(the_portfolio)
print()
findtotalshare(the_portfolio)
