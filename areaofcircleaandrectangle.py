"""6. Write a program that has following menu:
Enter 1 to find the area of rectangle.
Enter 2 to find the area of circle.
Values for length and width of a rectangle and value of a radius of
circle will be entered through keyboard. """

option=input("""select an option
1.area_of_circle
2.area_of_rectangle""")
if option=="1":
    radius=int(input("enter the radius="))
    print(3.14*radius**2)
elif option=="2":
    length=float(input("enter the length="))
    width=float(input("enter the width="))
    print(length*width)
else:
    print("no result")
