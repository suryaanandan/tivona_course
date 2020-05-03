def get_largest_number(number_1, number_2, number_3):
    if (number_1 >= number_2) and (number_1 >= number_3):
        largest_number = number_1
    elif (number_2 >= number_1) and (number_2 >= number_3):
        largest_number = number_2
    else:
        largest_number = number_3
    return largest_number

number_1 = float(input("Please enter value for number 1 : "))
number_2 = float(input("Please enter value for number 2 : "))
number_3 = float(input("Please enter value for number 3 : "))
largest_number = get_largest_number(number_1, number_2, number_3)
print("Largest number is : ")
print(largest_number)