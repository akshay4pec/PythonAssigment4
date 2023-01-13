# to print the prime numebers in a range 
a = int(input('Enter the lower limit of the range : '))
b = int(input('Enter the upper limit of the range : '))

for i in range(a,b+1):
    if(i == 1):
        continue
    prime = 1

    for j in range(2 , i):
        if(i%j == 0):
            prime = 0
            break
    if(prime == 1):
        print( i , end = " ")
        print(" ")
    
