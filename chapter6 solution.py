# # WAP to find greatest of four numbers entered by the users

# n1 =  int(input("Enter first number: "))
# n2 =  int(input("Enter second number: "))
# n3 =  int(input("Enter third number: "))
# n4 =  int(input("Enter fourth number: "))

# if(n1>n2):
#     f1 = n1
# else:
#     f1 =n2

# if(n3>n4):
#     f2 = n3
# else:
#     f2 =n4
# if(f1>f2):
#     print(str(f1)+" is the greatest number")
# else:
#     print(str(f2)+" is the greatest number")

# print("Thanks for using me, It was a great pleasure serving you")


# # WAP to find out whether a student is pass or fail, if it requires total 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

# mark1 = int(input("Enter the marks for subject 1: "))
# mark2 = int(input("Enter the marks for subject 2: "))
# mark3 = int(input("Enter the marks for subject 3: "))

# if mark1 > 33 and mark2 > 33 and mark3 >33:
#     if (mark1+mark2+mark3)/300*100>=40:
#         print("You have Passed the exam")
#     else:
#         print("Your total marks is not above 40%, so you have failed the exam")
# else:
#     print("You have failed the exam, due to less than 33% marks in of the subjects")


# # A spam comment is define as a text containing following keywords:
# # "make a lot of money","buy now","subcribe this","click this". WAP to detect these spams
# comment = input("Enter the comments: ")
# spam = False
# if("make a lot of money"in comment):
#     spam = True
# elif("buy now"in comment):
#     spam = True
# elif("subcribe this"in comment):
#     spam = True
# elif("click this"in comment):
#     spam = True
# else:
#     spam= False

# if(spam):
#     print("This comment is Spam")
# else:
#     print("This comment is not Spam")


# # WAP to find whether a given username contains less than 10 characters or not

# name =  input("Enter a username: ")
# if len(name)<10:
#     print("Username contains less than 10 characters")
# else:
#     print("Username contains more than 10 characters")

# # WAP which finds out whether a given name is present in a list or not

# a = ["Ayaz","Alam","Tibah","Meraj","Sana","Atifa"]

# text =  input("Enter you name: ")

# if text in a :
#     print("Yes your name is present in the list")
# else:
#     print("No your name is not present in the list")


# # WAP to calculate the grade of a student from his marks from the following scheme:
# # 90-100 -> Excellent
# # 80-90 -> A
# # 70-80 -> B
# # 60-70 -> C
# # 50-60 -> D
# # <50 -> F

# marks =  int(input("Enter your marks: "))

# if marks> 90 and marks<=100:
#     print("Excellent")
# elif marks> 80 and marks<=90:
#     print("A")
# elif marks> 70 and marks<=80:
#     print("B")
# elif marks> 60 and marks<=70:
#     print("C")
# elif marks> 50 and marks<=60:
#     print("D")
# elif marks< 50:
#     print("F")
# else:
#     print("Error")


# # WAP to find out whether a given post is talking about "Harry" or not

# post = input("Enter the post here: ")

# post =  post.lower()

# if "harry" in post:
#     print("Yes the post is talking harry")

# else:
#     print("No, the post is not talking about harry")
