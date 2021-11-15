# dictionary = {
#     "Fast": "In a quick manner",
#     "Fast": "In a very quick manner", # since Fast is repeating so the lastest value to the Fast will be shown
#     "Harry": "Programming God",
#     "Ayaz": "The greatest of all time",
#     "Marks": [1,2,3,4],
#     "number": (5,6,6),
#     "anotherDict":{"Zeera":"Rice"}

# }

# print(dictionary["anotherDict"])
# print(dictionary["Ayaz"])
# print(dictionary["Fast"])
# dictionary["number"] = (5,7,8)
# print(dictionary["number"])
# print(dictionary["Marks"])
# print(dictionary["anotherDict"]["Zeera"])

# print(dictionary)


# # Dictionary Methods

# myDict = {
#     "Fast": "In a quick manner",
#     "Harry": "Programming God",
#     "Ayaz": "The greatest of all time",
#     "Marks": [1,2,3,4],
#     "number": (5,6,6),  
#     "anotherDict":{"Zeera":"Rice"},
#     1:2

# }

# print(type(myDict.keys())) # the type is dict_keys
# print(list(myDict.keys())) # now I have type cast the dict_keys to the list 
# print(myDict.values()) # print the keys of the dictionary
# print(myDict.items()) # Print the (key, value) for all contents of the dictionary
# print(myDict)
# updateDict={
#     "Lovish":"Friend",
#     "Dilip":"Friend",
#     "Chopra":"Friend",
#     "Ayaz":"The Greatest of All Time"
# }
# myDict.update(updateDict) # update the dictionary by adding key-value pair from updateDict
# print(myDict)

# print(myDict.get("Ayaz")) # Print value associtated with the "Ayaz"
# print(myDict["Ayaz"]) # Print value associtated with the "Ayaz"

# # The difference between .get and [] syntax in Dictionaries?
# print(myDict.get("Ayaz2")) # Returns None as Ayaz2 is not present in the dictionary
# print(myDict["Ayaz2"]) # throws an error as Ayaz2 is not present in the dictionary

