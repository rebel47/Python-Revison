# # WAP using function to find the greatest of three numbers

# def greatNum(a,b,c):
#     if a>b:
#         if a>c:
#             print(a)
#         else:
#             print(c)
#     else:
#         if b>c:
#             print(b)
#         else:
#             print(c)

# greatNum(4,16,8)
# a,b,c = map(int,input("Enter 3 numbers: ").split(" "))
# greatNum(a,b,c)

# # WAP to convert celcius to fahreheit

# # (0°C × 9/5) + 32 = 32°F
# def convertCel(c):
#     return (c*9/5)+32

# c = int(input("Enter the Celcius: "))
# print(convertCel(c))

# # How do you prevent a python print() function to print a new line at the end
# print("Hello",end=" ")
# print("World",end="")

# # WAP a recursive function to calculate the sum of first n natural numbers
# def calSum(n):
#     if n==0:
#         return 0
#     return n+calSum(n-1)
# n = int(input("Enter a number: "))
# print(calSum(n))

# # Write a python function to print first n lines of the following patter:

# def myPattern(n):
#     for i in range(n):
#         print("*"*(n-i))
# n = int(input("Enter a number and I'll you a magic: "))
# myPattern(n)

# # Write a python function which converts inches to cms
# def myConvCm(inch):
#     return inch*2.54
# inch = int(input("Enter the length in inches: "))
# print(f"{myConvCm(inch)} cm")

# # Write a python function to remove a given word from a string and strip it at the same time
# def removeAndSplit(text, change):
#     newText = text.replace(change,"")
#     return newText.strip()
# text = "              Ayaz is a good     "
# change = input("Enter the word that you want to remove: ")
# print(removeAndSplit(text,change))

# # Write a python function to print multiplication table of a given number
# def myTable(n):
#     for i in range(1,11):
#         print(f"{n}X{i}={n*i}")
# n = int(input("Enter a number and I'll make it's table: "))
# myTable(n)