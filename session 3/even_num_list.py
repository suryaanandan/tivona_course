"""Question 7
Module related to even numbers list

This module contains function to compute and return a list of even numbers

"""

import random
def get_even_num_list(size):
    """Module level function to compute and return a list of even numbers. The size of the list is to be given as an argument to the function  
    """
    list_value = random.randrange(1, 100)
    if((list_value % 2) != 0):
        list_value = list_value + 1

    even_num_list = []*size

    for iteration in range(size):
        even_num_list.append(list_value)  
        list_value = list_value + 2 
    return even_num_list

# Obtain user input for list size
size = int(input("Please enter value for list size between 1 to 100 : "))

# Check input is valid or not. If input is invalid get to get another time
next_chance=0
while (((size < 1) or (size > 100)) and next_chance < 2):
    size = (int)(input("\nInvalid size please enter list size with in 1 to 100 : "))
    next_chance = next_chance +1

if(((next_chance == 2)) and ((size<1) or (size>100))):
    print("\nSorry invalid input. Entered invalid input 3 times")

else:
    even_num_list = []*size

    # Test for the function get_even_num_list
    even_num_list = get_even_num_list(size)

    print("Even numbers list starts from random number : ")
    print(even_num_list)
