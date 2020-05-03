"""Question 4 and 5
Module related to average of numeric values in list

This module contains function to compute and return average of numeric values in list

"""

#code for question 4-a
def get_average(number_list):
    """Module level function to compute and return average of numeric values in list
    """
    sum = 0.0
    numeric_count = 0
    for iteration in range(len(number_list)):
        iteration = (str)(number_list[iteration])
        #if(iteration.isdigit()):
        try:
            iteration = (float)(iteration)
            sum = sum + iteration
            numeric_count = numeric_count + 1
        except ValueError:
            continue
    if(numeric_count == 0):
        print("\nsum of {} numeric values in list = {} ".format(numeric_count, sum))
        average = 0
    else:
        print("\nsum of {} numeric values in list = {} ".format(numeric_count, sum))
        average = sum / numeric_count
    return average


#code for question 4-b
# Code to seek user input of 4 values and call the get_average function and print the average computed.
number_list = []
size = 4 # list size assigned as 4
print("List size = ", size)
for iteration in range(size):
    list_value = (str)(input("Enter numeric value as list element : "))
    number_list.append(list_value)

# Test for the function get_average
average = get_average(number_list)
print("Average =  {}".format(round(average,3)))
size = int(input("Please enter value for list size between 1 to 100 : "))

next_chance=0
while (((size < 1) or (size > 100)) and next_chance < 2):
    size = (int)(input("\nInvalid size please enter list size with in 1 to 100 : "))
    next_chance = next_chance + 1

if(((next_chance == 2)) and ((size<1) or (size>100))):
    print("\nSorry invalid input. Entered invalid input 3 times")

else:

    # Obtain user input for list values
    number_list = []
    iteration = 0
    while (iteration < size):
        list_value = (str)(input("Enter  value for list element : "))
        number_list.append(list_value)
        iteration = iteration + 1

    # Test for the function get_average
    average = get_average(number_list)
print("Average =  {}".format(round(average,3)))