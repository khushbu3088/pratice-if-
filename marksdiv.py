"""5. The marks obtain by a student in 5 different subjects are input
through keyboard. The student gets the division as per the following
rules:
Percentage above or equal to 60- first division
Percentage between 50 and 59- second division
Percentage between 40 and 49 – third division
Percentage below 40- fails. """


m1=float(input("enter the marks of student="))
m2=int(input("enter the marks of student="))
m3=int(input("enter the marks of student="))
m4=int(input("enter the marks of student="))
m5=int(input("enter the marks of student="))

if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40:
    avg=(m1+m2+m3+m4+m5)/5

    if avg>=60:
     print("first division")
    elif avg>50 and marks<59:
     print("second division")
    elif avg>40 and marks<49:
     print("third division")
else:
    print("fails")
