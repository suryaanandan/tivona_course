"""Question 8
Module related to convertion distance from miles to Kilometers

This module contains function to compute and return list of Kilometers equavalent to given list of miles

"""


def get_kilometers(miles_list):
    """Module level function to compute and return list of Kilometers equavalent to given list of miles  
    """
    kilometers_list = []*size

    for miles in miles_list:
        kilometer = miles * 1.6
        kilometers_list.append(round(kilometer,3))  
    return kilometers_list

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
    miles_list = []*size
    kilometers_list = []*size

    for iteration in range(size):
        list_value = float(input("Enter distance in miles greater than 0 : "))
        miles_list.append(list_value)

    # Test for the function get_kilometers
    kilometers_list = get_kilometers(miles_list)

    print("1 miles = 1.6 kilometer")

    print("\nDistance is miles : ")
    print(miles_list)

    print("\nDistance is kilometer : ")
    print(kilometers_list)

