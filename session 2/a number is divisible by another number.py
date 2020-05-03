def is_divisible(a, b):
    if (a % b == 0):
        divisible = True
    else:
        divisible = False
    return divisible

a = int(input("Please enter first number : "))
b = int(input("Please enter the secound number  : "))
divisible = is_divisible(a, b)
print("Is divisible : ")
print(divisible)
