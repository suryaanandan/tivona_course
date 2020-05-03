def get_selling_price(book_price, discount_percentage = 10):
    selling_price = book_price - (book_price * discount_percentage / 100)        
    return selling_price
    
book_price = (int)(input("Please enter book price greater than 0 : "))

while(book_price <= 0):
    book_price = (int)(input("Invalid input, Please enter book price greater than 0 : "))
    
discount_percentage = input("Please enter discount percentage but it's optional only : ")

if(discount_percentage == ""):
    print("\nYou didn't enter any dicount percent, so default value is taken for discount_percentage")
    selling_price = get_selling_price(book_price)

    print("\nSelling price of book with {} percent discount = {} ".format(10,selling_price))

else:

    discount_percentage = (int)(discount_percentage)
    selling_price = get_selling_price(book_price, discount_percentage)
    print("\nSelling price of book with {} percent discount = {}".format(discount_percentage,selling_price))









