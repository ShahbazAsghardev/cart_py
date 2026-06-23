cart=[]
def addtocart(items):
    total=0
    for price in items:
        total+=price
    return total
item=int(input("enter the number of items you have bought:"))
for i in range(item):
    price=int(input("enter the price of itmes"))
    cart.append(price)
totalammount=addtocart(cart)
print("the total ammountis:",totalammount)
discount=totalammount*10/100
if totalammount>555:
    print("you have got discount after discount the total ammount is:",discount)
else:
    print("yuo have no discount so total ammount is:",totalammount)