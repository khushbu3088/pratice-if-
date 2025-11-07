"""7. Write a program that has following menu:

Enter 1 to find out whether the entered number is even or odd.
Enter 2 to find out whether the entered number is positive or
negative."""


num=int(input("enter the num="))
option=input("""select an option
1.even_odd
2.positive or negative""")

if option=="1":
    if(num%2==0):
        print(num,"even")
    else:
        print(num,"odd")
elif option=="2":
    if(num>0):
     print("positive")
    elif (num<0):
        print("negative")
    else:
        print("zero")
else:
    print("invalid num")
        

    
