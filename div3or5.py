#3. WAP to test a whether a number is divisible by 3 or 5 or both.

num=int(input("enter the num="))
if num%3==0 and num%5==0:
    print("div by 3 and div by 5")
elif num%3==0:
    print(" div by 3")
elif  num%5==0:
    print("div by 5")
