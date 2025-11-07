#4. WAP to find the greatest of three numbers entered through
#keyboard.
a=float(input("enter the num1="))
b=float(input("enter the num2="))
c=float(input("enter the num3="))
if  a>b and a>c:
    print("a is the greatest value")
elif b>a and b>c:
    print("b is the greatest value")
elif c>a and c>b:
    print("c is the greatest value")
elif a==b and a>c:
    print("a,b>c")
elif b==c and b>a:
    print("b,c>a")
elif a==b and b==c:
    print("a=b=c")
