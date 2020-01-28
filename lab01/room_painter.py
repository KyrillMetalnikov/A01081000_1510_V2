"""
This program finds the area and the surface area of a circle based on user input of a radius
"""
import math
COVERAGE = 400

length = float(input("Input the length of the room in feet"))
width = float(input("Input the width of the room in feet"))
height = float(input("Input the height of the room in feet"))
coats = float(input("Input the number of coats you wish to paint"))

# calculates total surface area by adding the areas of 4 walls and the ceiling
surface_area = (2 * width * height) + (2 * length * height) + (length * width)

# calculates how many cans of paint are needed, and rounds up to know how many user needs to buy
coverage_needed = surface_area * coats
cans_of_paint_required = math.ceil(coverage_needed / COVERAGE)

print("You will need to buy " + str(cans_of_paint_required) + " cans of paint")
