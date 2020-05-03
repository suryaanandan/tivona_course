"""Question 6
Module related to random integers

This module contains function to compute and return the list of random integers with in range of min and max values

"""

import random

def get_random_integers(size, min = 1, max =100):
    """Module level function to compute and return a list of random integers with in range of min and max values. min and max variable is optional   
    """
    random_num_list = []*size
    for iteration in range(size):
        random_num_list.append(random.randrange(min, max))  
    print("\nMin = ", min, " Max = ", max)
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
    
    # Obtain user input for list min value
    min = input("Please enter value for min value in list between 1 to 99 but its optional element: ")
    if(min != ""):
        min = (int)(min)
        invalid_min = True
        while(((min <1) or (min > 99)) and (invalid_min == True)):
            min = input("\nInvalid min value please enter min value between 1 to 99 but its optional element: ")   
            if(min == ""):   
                invalid_min = False
            else:
                min = (int)(min)

    # Obtain user input for list max value
    min = (str)(min)
    if(min == ""):
        max = input("Please enter value for max value in list between 1 to 100 but its optional element: ")
    else:
        max = input("Please enter value for max value in list between {} to 100 but its optional element: ".format(min))
    
    if((max != "") and (min != "")):
        min = (int)(min)
        max = (int)(max)
        invalid_max = True
        while((((max <=min) or (max>100))) and (invalid_max == True)):
            max = input("\nInvalid max value please enter max value between {} to 99 but its optional element: ".format(min))
            if(max == ""):
                invalid_max = False
            else:
                max = (int)(max)

    # Test for the function get_random_integers
    min = (str)(min)
    max = (str)(max)
    if((min == "") and (max != "")):
        print("\nSorry invalid input, middle element alone connot be default element")
    else:
        if((min != "") and (max == "")):
            min = (int)(min)
            random_num_list = get_random_integers(size, min)
        elif((min == "") and (max == "")):
            random_num_list = get_random_integers(size)
        elif((min != "") and (max != "")):
            min = (int)(min)
            max = (int)(max)
            random_num_list = get_random_integers(size, min,max)

        print("Random numbers list : ")
        print(random_num_list)

