"""Question 5
Module related to random integers

This module contains function to compute and return the list of random integers

"""

import random

def get_random_integers(size):
    """Module level function to compute and return a list of random integers. The length of list is to be provided as an argument      
    """
    random_num_list = []*size
    for iteration in range(size):
        random_num_list.append(random.randrange(1, 100))   
    return random_num_list

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
    random_num_list = []*size

    # Test for the function get_random_integers
    random_num_list = get_random_integers(size)

    print("Random numbers list : ")
    print(random_num_list)




