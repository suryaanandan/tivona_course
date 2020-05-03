PI = 3.14 # value of Pie

def get_circle_area(radius):
    area = PI * (radius * radius)
    return area

def get_circle_circumference(radius):
    circumference = 2 * PI * radius
    return circumference

radius = float(input("Please enter radius of a circle: "))
area = get_circle_area(radius)
print("Area of circle : ")
print(area)

circumference = get_circle_circumference(radius)
print("Circumference of circle : ")
print(circumference)
