# # WAP to create a dictionary of hindi words with values as their english translation. Provide user with an option to look it up!

# hindiDict ={
#     "kela":"Banana",
#     "mirchi":"chilli",
#     "baigan":"bringal",
#     "bhindi":"lady finger",
#     "mithai":"sweets",
# }
# print("Options are: ", hindiDict.keys())
# n = input("Enter a hindi word in english: ")

# # print("The meaning of your word is: ",hindiDict[n])
# # Below line will not throw error if the key is not present in the dictionary
# print("The meaning of your word is: ",hindiDict.get(n))

# # WAP to input eight numbers from the user and display all the unique numbers(once)

# n1 = int(input("Enter a number 1: "))
# n2 = int(input("Enter a number 2: "))
# n3 = int(input("Enter a number 3: "))
# n4 = int(input("Enter a number 4: "))
# n5 = int(input("Enter a number 5: "))
# n6 = int(input("Enter a number 6: "))
# n7 = int(input("Enter a number 7: "))
# n8 = int(input("Enter a number 8: "))

# a = {n1,n2,n3,n4,n5,n6,n7,n8}
# print(a)
# print(type(a))

# # CAN WE HAVE SET WITH A VALUE 18(INT) AND "18"(STR) AS A VALUES IN IT?
# a = {18,"18","9",34}
# print(a) # SO THE ANSWER IS YES WE CAN 18 AS INTEGER AND 18 AS STRING AT THE SAME TIME IN A SET

# # What will be the length of the following set s

# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s)) # length will 2 20 and 20.0 will considered as same 

# s = {} is the type of dictionary and to create a empty set: s = set()

# CREATE AN EMPTY DICTIONARY. ALLOW 4 FRIENDS TO ENTER THEIR FAVOURITE LANGUAGE AS VALUES AND USE KEYS AS THEIR NAMES, ASSUME THAT THE NAMES ARE UNIQUE

# langDict = {}

# a = input("Enter you favourite language Ayaz: ")
# b = input("Enter you favourite language George: ")
# c = input("Enter you favourite language Matt: ")
# d = input("Enter you favourite language Alif: ")
# langDict['Ayaz'] = a
# langDict['George'] = b
# langDict['Matt'] = c
# langDict['Alif'] = d

# print(langDict)

# Let's take name and favourite language from user itself

# langDict = {}
# name1, lang1 = input("Enter your name and your Favourite language name: ").split()
# name2, lang2 = input("Enter your name and your Favourite language name: ").split()
# name3, lang3 = input("Enter your name and your Favourite language name: ").split()
# name4, lang4 = input("Enter your name and your Favourite language name: ").split()

# langDict[name1] = lang1
# langDict[name2] = lang2
# langDict[name3] = lang3
# langDict[name4] = lang4

# print(langDict)

# # IMPORTANT: IF NAME OF TWO STUDENT ARE NAME/KEY THEN LATEST LANGUAGE/VALUE WILL BE PRINTED
# # IMPORTANT: IF LANGUAGE/VALUE OF TWO STUDENT ARE SAME THEN IT WILL CREATE NO ISSUE AND IT WILL PRINT THE SAME VALUE/LANGUAGES ACCORDING TO THE KEY/NAME

# Can you change teh values inside a list which is contained in a set

# s = {8,7,12,"Harry",[1,2]}# first of all you cannot store list inside set because set is not hashable


