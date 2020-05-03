"""Question 1-a
Module related to Circle

This module contains functions related to circle such as functions to find area of a circle and circumference of a circle.
"""
PI = 3.14 # value of Pie

def get_circle_area(radius):
    """Module level function to compute and return area of a circle.        
    """
    radius = (str)(radius)
    if(radius.isnumeric()):
        radius = (float)(radius)
        area = PI * (radius * radius)
    else:
        area = "Invalid input, radius must be numeric value"
    return area

def get_circle_circumference(radius):
    """Module level function to compute and return circumference of a circle.
    """
    radius = (str)(radius)
    if(radius.isnumeric()):
        radius = (float)(radius)
        circumference = 2 * PI * radius
    else:
        circumference = "Invalid input, radius must be numeric value"
    return circumference




