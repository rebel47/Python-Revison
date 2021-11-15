# # WAP to display a user entered name followed by Good Afternoon using input() function

# a  = input("Enter your good name: ")
# print(f"Good Afternoon, {a}") # f string is used in the print function

# WAP to fill in a letter template given below with name and date

# letter = ''' Dear <|NAME|>,
#                     You are selected!
#                     <|DATE|>'''
# name = input("Enter the Name: ")
# x = letter.replace("<|NAME|>",name)
# import datetime
# today = datetime.datetime.today()
# tada = str(today)
# b = x.replace("<|DATE|>", tada)
# print(b)



# ANOTHER WAY TO CODE THIS PROBLEM
# import datetime
# today = datetime.datetime.today()
# name =  input("Enter the Candidate Name:")
# print(f'''Dear {name},          #We can also use string.replace function to done this task
#         You are Selected!
#         {today: %B %d, %Y}''')

# # WAP to detect double spaces in a string

# a  = "Hello my  lady I  am Ayaz  Alam  and  I am  here to  protect  you"
# print(a.find("  "))
# print(a)
# a = a.replace('  ',' ')
# print(a)

# # WAP t format the following letter using escape sequence charaacters

# letter = "Dear Harry,\n\tThis Python course is nice.\n\t Thanks!"
# print(letter)


# # Slicing

# name = "Ayaz Alam is learning python right now."

# print(name[-2])
# print(name[-8:-1])
# print(name[::-1])
# print(name[::-2])
# print(name[::2])

# print(len(name))
# print(name.endswith('lam'))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.find("python")) # find only the first occurence in the string
# print(name.count("a")) # We can also count string using this




