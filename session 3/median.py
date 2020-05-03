"""Question 3
Module related to median

This module contains function to compute and return the median for the values contained in the given list

"""

def get_median(number_list):
    """Module level function to compute and return the median for the values contained in the given list       
    """
    size = len(number_list) 
    mid = int(size / 2)
    if((size % 2) == 0):
        median = (number_list[mid-1] + number_list[mid])/ 2
    else:
        median = number_list[mid]
    return median

# Obtain user input for list size
size = (int)(input("Please enter value for list size between 1 to 100 : "))

# Check input is valid or not. If input is invalid get to get another time
next_chance=0
while (((size < 1) or (size > 100)) and next_chance < 2):
    size = (int)(input("\nInvalid size please enter list size with in 1 to 100 : "))
    next_chance = next_chance +1

if(((next_chance == 2)) and ((size<1) or (size>100))):
    print("\nSorry invalid input. Entered invalid input 3 times")

else:
    # Obtain user input for list values
    number_list = []
    for iteration in range(size):
        list_value = int(input("Enter integer value as list element : "))
        number_list.append(list_value)

    # Sorting the list
    number_list.sort()

    # Test for the function get_median
    median = get_median(number_list)
    print("Median : ")
    print(median)




