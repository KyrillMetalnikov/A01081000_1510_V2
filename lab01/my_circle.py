"""
    This program finds the area and circumference of a circle of a radius inputted by user and then area and
    circumference of the same radius except doubled.
"""
PI = 3.14159
radius = 0

radius = float(input("input a radius (positive numbers only)"))  # takes user input, converts to float and stores it
circumference = 2 * PI * radius
print("the circumference of the circle is " + str(circumference))
area = PI * radius * radius
print("the area of the circle is " + str(area))

double_radius = radius * 2

double_circumference = 2 * PI * double_radius
circumference_difference = double_circumference / circumference
print("If we double the radius, the circumference becomes " + str(circumference_difference) + ' times bigger')

double_area = PI * double_radius * double_radius
area_difference = double_area / area
print("if we double the radius, the area becomes " + str(area_difference) + ' times bigger')
