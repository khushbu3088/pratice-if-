cost_price=float(input("enter the cost_price="))
selling_price=float(input("enter the selling_price="))
if selling_price>cost_price:
    print("profit")
elif cost_price>selling_price:
    print("loss")
else:
    print("no profit or no loss")
