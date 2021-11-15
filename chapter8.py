# Fuctions and Recursions

# def greet(name):
#     print(f"Good Day, {name}")

# name = input("Enter the name: ")
# greet(name)

# # Sum function

# def mySum(num1, num2):
#     return num1+num2
# print(mySum(6,6))

# # Default Parameter Value

# def greet(name="Unknown"):
#     print(f"Hello {name}, Welcome to the planet Alphinos.")

# greet("Supreme Commander")
# greet() #since no arguments passed here, so default parameter will be used

# RECURSION

# # factorial
# # using function
# def myFact(n):
#     fact = 1

#     for i in range(1,n+1):
#         fact = fact*i
#     return fact   

# n =  int(input("Enter a number: "))
# print(myFact(n))

# # Using Recursion
# def myFactorial(n):
#     if n==1 or n==0:
#         return 1
#     return n*myFactorial(n-1)

# n = int(input("Enter a number: "))
# print(myFactorial(n))


