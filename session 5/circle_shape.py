# Question 1,2

import math
import random
class  Circle(object):
 
    def __init__(self, radius, area, circumference):
        self.radius = radius
        self. area = area
        self.circumference = circumference


    def get_circle_area(self, radius):
        """Module level function to compute and return area of a circle.        
        """
        self.radius = (str)(self.radius)
        self.radius = (float)(self.radius)
        self.area = math.pi * (self.radius * self.radius)
        self.area = round(self.area,2)
        return self.area

    def get_circle_circumference(self, radius):
        """Module level function to compute and return circumference of a circle.
        """
        self.radius = (str)(radius)
        self.radius = (float)(self.radius)
        self.circumference = 2 * math.pi * self.radius
        self.circumference = round(self.circumference,2)
        return self.circumference

    def __str__(self):
        num_of_digits = (str)(self.area)
        if(len(num_of_digits) <7):
            print("Radius = {}  \t\tArea = {}  \t\t\tCircumference = {}".format(self.radius, self.area, self.circumference))
        else:
            print("Radius = {}  \t\tArea = {}  \t\tCircumference = {}".format(self.radius, self.area, self.circumference))

# Tests for the class Circle
circle_list = list()
print("\n100 objects are created for Circle class. Area and circumference of circle is calculated with different radius")
for iteration in range(100):
    radius = random.randrange(1,50)
    circle_list.append(Circle(radius,0.0,0.0))
    circle_list[iteration].get_circle_area(radius)
    circle_list[iteration].get_circle_circumference(radius)
    circle_list[iteration].__str__()
