# Dictionary for mountains
mountains = {"Mount Everest": 8445, "K2": 8611, "Kangchenjunga": 8586, "Lhoste": 8616, "Makalu": 8516}
# Dictionary for mountains, sorted in descending order by their heights
alphabetical_order = {mountain: height for mountain, height in sorted(mountains.items())}
mountains_ft_m = {mountain: [height, height*3.28] for mountain, height in mountains.items()}


# Prints the names of each mountain.
for mountain, height in mountains.items():
    print(mountain)

print()
# Prints the heights of each mountain, in meters.
for mountain, height in mountains.items():
    print("%i meters" % height)

print()
# Prints information about each mountain, in a ranked format based on height
for mountain, height in alphabetical_order.items():
    print("%s is %i meters tall" % (mountain, height))

print()
# Prints only the elevation of each mountain in meters
for mountain, [meter, feet] in mountains_ft_m.items():
    print("%i meters" % meter)

print()
# Prints only the elevation of each mountain in feet
for mountain, [meter, feet] in mountains_ft_m.items():
    print("%.2f feet" % feet)

print()
# Prints statements of elevation of each mountain in both meters and feet
for mountain, [meter, feet] in mountains_ft_m.items():
    print("%s is %i meters tall, or %.2f feet tall." % (mountain, meter, feet))