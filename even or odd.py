a = int(input("enter first numbers:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a >= b and a >= c):
    print ("first number is largest",a)
elif(b >= c):
    print ("second number is largest",b)
else:
    print ("third number is largest",c)