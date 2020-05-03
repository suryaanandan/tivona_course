"""Question 4
Module related to mode

This module contains function to compute and return the mode for the values contained in the given list

"""

def get_mode(number_list):
    """Module level function to compute and return the mode for the values contained in the given list       
    """
    size = len(number_list) 
    mode = 0
    maxCount = 0
 
    for outer in range(size):
        count = 0
        for inner in range(size):
            if(number_list[inner] == number_list[outer]):
                count = count + 1
            if(count >= maxCount):
                maxCount = count
                mode = number_list[outer]

    return mode

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

    # Test for the function get_mode
    mode = get_mode(number_list)
    print("Mode : ")
    print(mode)




