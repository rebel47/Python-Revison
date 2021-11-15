# # WAP to print multiplication table of a given number using for loop
# # Using While Loop
# n = int(input("Enter a number: "))
# i =1
# while i<=10:
#     print(f"{i}   {n} * {i} = {n*i}")
#     i = i+1

# # Using For Loop

# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# # WAP to greet all the person names stored in a list l1 and which starts with s
# l1 = ["Harry Potter","Sohan Kumar","Sachin Kumar","Rahul Singh","mikush singh","sunny deol"]
# for name in l1:
#     name = name.upper()
#     if name.startswith("S"):
#         name = name.title() # this will convert upper case to pascal case 
#         print("Congratulations",name)


# # WAP to find whether a given number is prime or not

# n  = int(input("Enter a number: "))

# for i in range(2,n):
#     if n%i==0:
#         print("The number is not Prime")
#         break
# else:
#     print("This is a Prime number")

# # WAP to find the the sum of first n natural numbers using while loop

# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i<=n:
#     sum = sum +i
#     i =i+1
    
# print(f"Sum of first {n} natural number is: {sum}")

# # Using for loop
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum =  sum+i
# print(f"The sum of first {n} natural number is: {sum}")



# # WAP to calculate the factorial of a given number using for loop

# n = int(input("Enter a number: "))
# fact = 1

# for i in range(1,n+1):
#     fact = fact*i

# print(fact)

# Using while loop

# n= int(input("Enter a number: "))

# fact = 1
# i = 1
# while i<=n:
#     fact = fact*i
#     i =i+1
# print(fact)

# # WAP to print multiplication table of n using for loop in reversed order

# n =  int(input("Enter a number: "))
# for i in reversed(range(1,11)):
#     print(f"{n}X{i}={n*i}")

# # WAP to print the following star pattern
# # *
# # **
# # ***
# # ****
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print("*"*i)


# # WAP to print the following star pattern
# #    *
# #   ***
# #  *****
# # *******

# n = int(input("Enter a number: "))
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     print("*"*(2*i+1),end="")
#     print(""*(n-i-1),)

# # WAP to print the following star pattern
# # ***
# # * *
# # ***
# n =  int(input("Enter a number: "))
# for i in range(n):
#     print("*")
#     print("")

