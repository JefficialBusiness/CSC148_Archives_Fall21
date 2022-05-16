# lecture 5 demo codes
# compute area of a circle based on user input

import math
radius = input("please enter a radius. ")
print(type(radius))
R = float(radius)
area = round((R**2)*math.pi,2)
print("the area of your circle is: ", area)