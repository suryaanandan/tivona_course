# Question 3,4

import random
class  Rectangle(object):
 
    def __init__(self, length, width, area, perimeter):
        """
        Rectangle object takes 4 arguments
        """

        self.length = length
        self. width = width
        self.area = area
        self.perimeter = perimeter

    def get_rect_area(self, length, width):
        """Module level function to compute and return area of a rectangle.        
        """
        self.length = (str)(self.length)
        self.width = (str)(self.width)
        self.length = (float)(self.length)
        self.width = (float)(self.width)
        self.area = self.length * self.width
        self.area = round(self.area,2)
        return self.area

    def get_rect_perimeter(self, length, width):
        """Module level function to compute and return perimeter of a rectangle.
        """
        self.length = (str)(self.length)
        self.width = (str)(self.width)
        self.length = (float)(self.length)
        self.width = (float)(self.width)
        self.perimeter = 2 * (self.length + self.width)
        self.perimeter = round(self.perimeter,2)
        return self.perimeter

    def __str__(self):
        num_of_digits_area = (str)(self.area)
        num_of_digits_width = (str)(self.width)

        if((len(num_of_digits_width) == 6) and (len(num_of_digits_width) == 4)):
            print("Length = {}  \t\tWidth = {}  \t\tArea = {}\tPerimeter = {}".format(self.length, self.width, self.area, self.perimeter))
        elif(len(num_of_digits_area) <= 4):
            print("Length = {}  \t\tWidth = {}  \t\tArea = {}\t\t\t\t\tPerimeter = {}".format(self.length, self.width, self.area, self.perimeter))
        else:
            print("Length = {}  \t\tWidth = {}  \t\tArea = {}\t\t\t\tPerimeter = {}".format(self.length, self.width, self.area, self.perimeter))

        
# Tests for the class Circle
ractangle_list = list()
print("\n100 objects are created for rectangle class. Area and perimeter of rectangle is calculated with different length and width")
for iteration in range(100):
    length = random.randrange(1,50)
    width = random.randrange(1,50)
    ractangle_list.append(Rectangle(length, width, 0.0, 0.0))
    ractangle_list[iteration].get_rect_area(length, width)
    ractangle_list[iteration].get_rect_perimeter(length, width)
    ractangle_list[iteration].__str__()
