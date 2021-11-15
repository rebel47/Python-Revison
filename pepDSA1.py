'''
1. You've to check whether a given number is prime or not.
2. Take a number "t" as input representing count of input numbers to be tested.
3. Take a number "n" as input "t" number of times.
4. For each input value of n, print "prime" if the number is prime and "not prime" otherwise.

Constraints

1 

Format

Input

A number t
A number n
A number n
.. t number of times

Output

prime
not prime
not prime
.. t number of times

Example

Sample Input

5
13
2
3
4
5

Sample Output

prime
prime
prime
not prime
prime
'''

# t= int(input())
# n = []
# for i in range(t):
#     data=int(input())
#     n.append(data)
# # print(len(n))
# # print(n)
# for x in n:
#     for j in range(2,x):
#         if x%j==0:
#             print(f"{x} is not prime number")
#             break
#     else:
#         print(f"{x} is prime number")

# Second Approach
# t= int(input())
# for i in range(t):
#     count = 0
#     n = int(input())
#     j =2
#     while j<n:
#         if  n%j==0:
#             count +=1
#             break
#         j+=1
#     if count ==0:
#         print("prime")
#     else:
#         print("not prime")


# WAP to print all prime numbers between two given numbers by user

# low=int(input())
# high=int(input())
# #write your code here
# for i in range(low,high+1):
    
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# # Second Approach

# low=int(input())
# high=int(input())
# for i in range(low,high+1):
#     count=0
#     div=2
#     while div*div<=i:
#         if(i%div==0):
#             count+=1
#             break
#         div+=1
#     if(count==0):
#         print(i)


# # Fibonacci Series

# n = int(input())
# a =0    
# b=1
# for i in range(n):
#     print(a)
#     temp = a+b
#     a =b
#     b = temp 


# # Count the number of digits in a number

# def count(n):
#     a = len(str(n))
#     print(a)

# def main():
#     n = int(input())
#     count(n)
# main()

# # Digits of a number
# def listIn(n):
#     res = [int(x) for x in str(n)]
#     for i in res:
#         print(i)

# n = int(input())
# listIn(n)

# # Digits of a number in reverse order
# def listIn(n):
#     res = [int(x) for x in str(n)]
#     for i in res[::-1]:
#         print(i)

# n = int(input())
# listIn(n)

# a = [1,2,3,4,5,6,7,8]
# print(type(str(a)))
# t = int(input())
# new = a[-t:]
# for i in reversed(new):
#     p=0
#     a.insert(p,i)
#     p = p+1
#     a.pop(-p)
# print(a)
# print(res)
# a.pop(-1)
# print(a)

def rotate(n,k):
    a = [int(x) for x in str(n)]
    new = a[-k:]
    for i in reversed(new):
        p=0
        a.insert(p,i)
        p = p+1
        a.pop(-p)
    for j in a:
        print(j,end="")

def main():
    n = int(input())
    k = int(input())
    rotate(n,k)

if __name__=="__main__":
    main()