#to reverese a string 

a = input("Enter a string : ")
str = ""
for i in a:
    str = i + str
print(str)