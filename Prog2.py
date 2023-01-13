#Program to print all the numbers in a range divisible by a given number.

r1 = int(input("Enter the Lower Range: "))
r2 = int(input("Enter the Upper Limit: "))
n = int(input("Enter the Number : "))

for i in range (r1,r2 + 1):
    if(i%n == 0):
        print(i)