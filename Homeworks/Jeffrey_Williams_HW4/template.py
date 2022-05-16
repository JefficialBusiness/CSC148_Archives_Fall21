import csv


# name: get_data_list
# param: FILE_NAME <str> - the file's name you saved for the stock's prices
# brief: get a list of the stock's records' lists
# return: a list of lists <list>

def get_data_list(filename):
    thelist = []
    with open(filename) as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in file:
            thelist.append(row)

    return thelist


# name: get_monthly_averages
# param: data_list <list> - the list that you will process
# brief: get a list of the stock's monthly averages and their corresponding dates
# return: a dictionary

def get_monthly_averages(data_list):
    # Initialize variables for start and end year (years we want to focus on)
    start = 2014
    end = 2018

    # Initialize dictionaries we are to use to store data for each month
    target_dict = {}
    data_withtuples = {}

    # Index the list, skipping the headers
    for day in data_list[1:]:
        data = day[0].split(',')
        year = data[0][:4]
        month = data[0][5:7]
        volume = float(data[6])
        close = float(data[5])
        date = ("%s-%s" % (year, month))
        data_withtuples[date] = []
        data_withtuples[date].append((close, volume))

        # Uses the target_dict to close window on particular group of years,
        # Call the function to calculate monthly averages for the lists of tuples
        for key, value in data_withtuples.items():
            if start <= int(key[:4]) <= end:
                target_dict[date] = calculate_monthly_average(value)

    for day in data_list[1:]:
        data = day[0].split(',')
        year = data[0][:4]
        month = data[0][5:7]
        # Specification for volume and close (MAY NEED TO CHANGE AS NEEDED DEPENDING ON .CSV CHART FORMAT)
        volume = float(data[6])
        close = float(data[5])
        date = ("%s-%s" % (year, month))
        data_withtuples[date].append((close, volume))

    monthly_averages = {}

    # Call the function to calculate monthly averages for the lists of tuples
    for key, value in data_withtuples.items():
        monthly_averages[key] = calculate_monthly_average(value)

    print("All Data:", data_withtuples)
    print("Monthly Averages for Target Years: ", target_dict)
    print("All Monthly Averages: ", monthly_averages)
    return target_dict


# name: calculate_monthly_average
# param: listoftuples, a list of tuples given, which represents the stock data for each individual day for a month
# brief: compute the average monthly price
# return: average number from calculation (int)

def calculate_monthly_average(listoftuples):
    product = 0
    volumesum = 0

    for close, volume in listoftuples:
        product = product + (close * volume)
        volumesum = volumesum + volume

    average = product / volumesum

    return average


# name: print_info
# param: monthly_average_list <list> - the list that you will process
# brief: print the top 6 and bottom 6 months for Google stock
# return: None

def print_info(datadictionary):
    # Create new dictionaries sorting the top and bottom 6 months
    best = dict(sorted(datadictionary.items(), key=lambda item: item[1], reverse=True)[:6])
    worst = dict(sorted(datadictionary.items(), key=lambda item: item[1])[:6])

    # Opens file
    file = open(write_file, "w")
    file.write("The 6 best months:")

    # Prints the best 6 months in the file
    for key, value in best.items():
        file.write("\n")
        file.write("%s, %.2f" % (key, value))

    file.write("\n")
    file.write("")
    file.write("\n")
    file.write("The 6 worst months:")

    # Prints the worst 6 months in the file
    for key, value in worst.items():
        file.write("\n")
        file.write("%s, %.2f" % (key, value))

    file.close()


# Assignment of table to analyze and text file to record information
filename = 'GOOG.csv'
write_file = "monthly_averages.txt"

thelist = get_data_list(filename)  # Call get_data_list function to get the data list, save the return in data_list
get_monthly_averages(thelist)  # Call get_monthly_averages function with the data_list from above, save
# monthly_average_list return

monthly_averages = get_monthly_averages(thelist)
print_info(monthly_averages)  # Call print_info function with the monthly_average_list from above
