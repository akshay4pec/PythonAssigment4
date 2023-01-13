n = 6
for col in range(n):
    for row in range(col):
        print(chr(ord("A") + row ), end = " ")
    print(" ")