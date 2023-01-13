n = int(input("Enter the range of pattern: "))
for col in range(n):
    for row in range(col):
        print("* ", end = " ")
    print(" ")

for col in range(n,0,-1):
    for row in range(col):
        print("* ", end = " ")
    print(" ")