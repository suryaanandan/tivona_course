def simple_interest(p,r,t):
    return p*r*t/100
p=float(input("enter the principal amount :"))
r =float(input("enter the rate of interest :"))
t=float(input("enter the time period :"))
y=simple_interest(p,r,t)
print("simple_interest of principal amount :",y)