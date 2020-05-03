
'''Write a function to compute and return the circumference of a circle'''
def get_circumference_circle(radius):
    pi=3.141
    circle = 2*pi*radius
    return circle
radius = eval(input("Please enter circumference as an int or float: "))

circle_of_circumference = get_circumference_circle(radius)
print(circle_of_circumference)