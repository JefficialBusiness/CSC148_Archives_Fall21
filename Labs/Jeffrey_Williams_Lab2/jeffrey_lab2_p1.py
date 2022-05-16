# Take input of height and convert from one metric to another

height_in = input("What is your height in inches? ")
conv_cm = float(height_in)*2.54  # Conversion to cm

print("Your height in centimeters is: ", str(conv_cm), ".")


height_cm = input("What is your height in centimeters? ")
conv_in = float(height_cm)/2.54  # Conversion to in

print("Your height in inches is: ", str(conv_in), ".")

