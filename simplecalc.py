"""8. WAP that implements the simple calculator that has following menu:
Enter 1 to find the True division of 2 numbers.
Enter 2 to find the square of a number.
Enter 3 to find the cube of a number."""


option=input("""select a option
1.div of 2 num
2.square of num
3.cube of num""")
if option=="1":
    a=int(input("enter a="))
    b=int(input("enter b="))
    print(a/b,"div of 2")
elif option=="2":
    num=int(input("enter the num"))
    print(num**2)
elif option=="3":
    num=int(input("enter the num"))
    print(num**3)
