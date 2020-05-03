"""Question 9
Module related to convertion of temperature from fahrenheit to Celsius

This module contains function to compute and return list of celsius equavalent to given list of fahrenheit

"""


def get_celsius(fahrenheit_list):
    """Module level function to compute and return list of celsius equavalent to given list of fahrenheit  
    """
    celsius_list = []*size

    for fahrenheit in fahrenheit_list:
        celsius = ( (fahrenheit - 32) * 5) /9 
        celsius_list.append(round(celsius,3))  
    return celsius_list

# Obtain user input for list size
size = int(input("Please enter value for list size from 1 to 100: "))

# Check input is valid or not. If input is invalid get to get another time
next_chance=0
while (((size < 1) or (size > 100)) and next_chance < 2):
    size = (int)(input("\nInvalid size please enter list size with in 1 to 100 : "))
    next_chance = next_chance +1

if(((next_chance == 2)) and ((size<1) or (size>100))):
    print("\nSorry invalid input. Entered invalid input 3 times")

else:
    fahrenheit_list = []*size
    celsius_list = []*size

    for iteration in range(size):
        list_value = float(input("Enter temperature in fahrenheit : "))
        fahrenheit_list.append(list_value)

    # Test for the function get_celsius
    celsius_list = get_celsius(fahrenheit_list)

    print("1 Fahrenheit = -17.2222 celsius")

    print("\nTemperature is fahrenheit : ")
    print(fahrenheit_list)

    print("\nTemperature is celsius : ")
    print(celsius_list)

