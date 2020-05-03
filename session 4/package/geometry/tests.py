"""Question 2 and 3
Module related to Circle and rectange

This module call functions in module circle and rectanges to find area, circumference of a circle and area, perimeter of a rectangle.
"""

import circle
radius = 5
area = circle.get_circle_area(radius)
print("\nRadius = ", radius)
print("\nArea of circle : ")
print(round(area,3))

# Test for the function get_circle_circumference in module cirle
circumference = circle.get_circle_circumference(radius)
print("\nCircumference of circle : ")
print(round(circumference,3))

# Test for the function get_circle_area in module circle with different radius
radius = 12
area = circle.get_circle_area(radius)
print("\nRadius = ", radius)
print("\nArea of circle : ")
print(round(area,3))

# Test for the function get_circle_circumference in module cirle
circumference = circle.get_circle_circumference(radius)
print("\nCircumference of circle : ")
print(round(circumference,3))


import rectangle
length = 5
width = 4
area = rectangle.get_rect_area(length, width)
print("\nLength = 5 and width = 4")
print("\nArea of rectangle : ")
print(round(area,3))

# Test for the function get_rect_perimeter in module rectangle
perimeter = rectangle.get_rect_perimeter(length, width)
print("\nPerimeter of rectangle : ")
print(round(perimeter,3))

# Test for the function get_rect_area in module rectangle with different length and width

length = 5
width = 6
area = rectangle.get_rect_area(length, width)
print("\nLength = 5 and width = 6")
print("\nArea of rectangle : ")
print(round(area,3))

# Test for the function get_rect_perimeter in module rectangle
perimeter = rectangle.get_rect_perimeter(length, width)
print("\nPerimeter of rectangle : ")
print(round(perimeter,3))
# Test for the function get_circle_area and get_circle_circumference function in module circle with non-numeric value

print("\nTesting get_circle_area and get_circle_circumference function in module circle with non-numeric parameter")
radius = "hello"
area = circle.get_circle_area(radius)
print("\nRadius = ", radius)
if(area.isnumeric()):
    print("\nArea of circle : ")
    print(round(area,3))
else:
    print(area)

# Test for the function get_circle_circumference in module cirle
circumference = circle.get_circle_circumference(radius)
if(area.isnumeric()):
    print("\nCircumference of circle : ")
    print(round(circumference,3))
else:
    print(circumference)

print("\nTesting get_rect_area and get_rect_perimeter in module rectangle with non-numeric value")

# Test for the function get_rect_area in module rectangle 

length = "lenth value"
width = "width_value"
area = rectangle.get_rect_area(length, width)
print("\nlength = ", length)
print("\nwidth = ", width)
if(area.isnumeric()):
    print("\nArea of rectangle : ")
    print(round(area,3))
else:
    print(area)


# Test for the function get_rect_perimeter in module rectangle
perimeter = rectangle.get_rect_perimeter(length, width)
if(perimeter.isnumeric()):
    print("\nperimeter of rectangle : ")
    print(round(perimeter,3))
else:
    print(perimeter)
