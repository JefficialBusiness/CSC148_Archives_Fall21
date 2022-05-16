# This program computes height in inches, as well as feet and inches using functions from module height.py
import height

# Assignment of values to variables needed for calculation
height_in_inches = 67
feet = 5
inches = 7

# Prints conversion of height from inches to feet and inches, invoking functions from height module
print("Height (ft, in):", height.get_feet(height_in_inches), "feet and", height.get_inches_left(height_in_inches),
      "inches.")

# Prints conversion of height from feet and inches to inches, invoking function from height module.
print("Height in inches:", height.to_inches(feet, inches), "inches.")
