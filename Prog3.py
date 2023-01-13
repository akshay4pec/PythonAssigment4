import math

a = int(input("Enter the 1st side : "))
b = int(input("Enter the 2nd side : "))
c = int(input("Enter the 3rd side : "))

if(a+b>c and b+c>a and c+a>b):
    print("The triangle is possible !")
else:
    print("The triangle in not possible !")

print("\n")

s = (a+b+c)/2
b = s*(s-a)*(s-b)*(s-c)
print("Area of the entered triangle is : ", math.sqrt(b) , " sq. units ")
