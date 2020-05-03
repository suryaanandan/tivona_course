def get_selling_price(book_name): 
    if(book_name == "Programming with problem solving with python"):
        selling_price = 699 - (699 * 10 / 100)
    elif(book_name == "Concept of programming language"):
        selling_price = 899 - (899 * 10 / 100)
    elif(book_name == "Information Theory and coding"):
        selling_price = 599 - (599 * 10 / 100)
    elif(book_name == "Web programming building internet"):
        selling_price = 999 - (999 * 10 / 100)
    else:
        selling_price = 0
    return selling_price
    
print("The Books available in shop")
print("1. Python Crash Course ")
print("2. Core Java Advanced ") 
print("3. Data structure and Algorithms in Java ")      
print("4. Learning Web Design: A Beginner’s Guide ")
book_name = input("Please enter the  book name : ")

selling_price = get_selling_price(book_name)
if(selling_price == 0):
    print("\nBook not is  available in shop")
else:
    print("Selling price of book is : ")
    print(selling_price)