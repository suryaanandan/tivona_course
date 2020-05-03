def get_selling_price(list_price, discount_percentage=0,binding_type="HB"):
    
    if binding_type == "HB":
        discount = 0
    else:
        discount = list_price * discount_percentage / 100
    
    selling_price = list_price - discount
    return selling_price
list_price=float(input("enter the list_price :"))
discount_percentage=float(input("enter the discount_percentage :"))
binding_type=str(input("enter the binding_type :"))
y=get_selling_price(list_price, discount_percentage,binding_type)
print("Selling price for the list price :",y)