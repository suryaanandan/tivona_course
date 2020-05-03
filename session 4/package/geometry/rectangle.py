"""Question 1-b
Module related to rectangle

This module contains functions related to rectangle such as functions to find area and perimeter of a rectangle.
"""

def get_rect_area(length, width):
    """Module level function to compute and return area of a rectangle.        
    """
    length = (str)(length)
    width = (str)(width)
    if((length.isnumeric()) and (length.isnumeric())):
        length = (float)(length)
        width = (float)(width)
        area = length * width
    else:
        area = "Invalid input, length and width must be numeric value"
    return area

def get_rect_perimeter(length, width):
    """Module level function to compute and return perimeter of a rectangle.
    """
    length = (str)(length)
    width = (str)(width)
    if((length.isnumeric()) and (length.isnumeric())):
        length = (float)(length)
        width = (float)(width)
        perimeter = 2 * (length + width)
    else:
        perimeter = "Invalid input, length and width must be numeric value"
    return perimeter




