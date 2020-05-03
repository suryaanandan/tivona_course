def get_professional_tax(salary):
    if(salary <=10000):
        professinal_tax = 0
    else:    
        professinal_tax =  (0.25 / 100) * salary
    return professinal_tax
salary = int(input("Please enter your  monthly salary : "))
professinal_tax = get_professional_tax(salary)
print("your professinal tax is : ")
print(professinal_tax)