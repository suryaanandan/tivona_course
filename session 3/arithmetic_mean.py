def get_arithmetic_mean(number_list):
    sum = 0.0
    for iteration in number_list:
        sum = sum + iteration
    arithmetic_mean = sum / len(number_list) 
    return arithmetic_mean

size = int(input("Please enter number_list size between 1 to 100 : "))
next_chance=0

while (((size < 1) or (size > 100)) and next_chance < 2):
    size = (int)(input("\nInvalid size please enter list size with in 1 to 100 : "))
    next_chance = next_chance +1

if(((next_chance == 2)) and ((size<1) or (size>100))):
    print("\nSorry invalid input. Entered invalid input 3 times")

else:
    number_list = []
    for iteration in range(size):
        list_value = int(input("Enter integer number as list element : "))
        number_list.append(list_value)

    arithmetic_mean = get_arithmetic_mean(number_list)
    print("\nArithmetic mean : ")
    print(arithmetic_mean)