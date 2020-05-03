"""Question 6,7,8
Module related to find past life of the person in astrology 

This module contains function to compute and return past life of the person in astrology 
"""

import random
predicted_past_life = {}
def get_past_life(name):
    """Module level function to compute and return return past life of the person in astroloy by take name as argument

    """ 
    
    past_life_list = ["You were a mathematician in your past life",
    "You were a animal in your past life",
    "You were a doctor in your past life",
    "You were a poet in your past life",
    "You were a politician in your past life",
    "you were a bird in your past life",
    "you were a teacher in your past life",
    "you were a artist in your past life",
    "you were a singer in your past life",
    "you were a sports person in your past life"]

    rand_num_for_name = random.randrange(0, 9)
    
    if name in predicted_past_life:
        past_life = predicted_past_life.get(name)
    else:
        past_life = past_life_list[rand_num_for_name]
        predicted_past_life[name] = past_life
        
    return past_life
    
# Code for question 6 and 7
# Obtain user input for name
try_again = "1"
print("\nKnow about your past life by your name\n")
while(try_again == "1"):
    name = (str)(input("\nPlease enter your name to know about your past life : "))

    if(name == ""):
        print("\nSorry we cann't predict about your past life, because you doesn't enter any name")
    else:
        name = name.upper()
        past_life = get_past_life(name)
        print("\n{} {}".format(name,past_life))
    try_again = (str)(input("\nPlease enter 1 if you want to try again otherwise enter any key : "))
print("\nThank you...")


import random
predicted_next_life = {}
def get_next_life(name):
    """Module level function to compute and return return next life of the person in astroloy by take name as argument

    """ 
    
    next_life_list = ["You will be a animal in your next life",
    "You will be a doctor in your next life",
    "You will be a storts person in your next life",
    "You will be a bird in your next life"]

    rand_num_for_name = random.randrange(0, 3)
    
    if name in predicted_next_life:
        next_life = predicted_next_life.get(name)
    else:
        next_life = next_life_list[rand_num_for_name]
        predicted_next_life[name] = next_life
        
    return next_life

# Code for question 8
# Obtain user input for name
try_again = "1"
print("\n\nKnow about your next life by your name\n")
while(try_again == "1"):
    name = (str)(input("Please enter your name to know about your next life : "))

    if(name == ""):
        print("\nSorry we cann't predict about your next life, because you doesn't enter any name")
    else:
        name = name.upper()
        next_life = get_next_life(name)
        print("\n{} {}".format(name,next_life))
    try_again = (str)(input("\nPlease enter 1 if you want to try again otherwise enter any key : "))
print("\nThank you...")