a = int(input("enter first numbers:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter fourth number:"))

if(a >= b and a >= c and a >= d):
    print("first number is largest",a)
elif(b >= c and b >= d):
    print("second number is largest",b)
elif(c >= b and c >= d):
    print("third is the largest",c)
else:
    print("fourth is the largest",d)