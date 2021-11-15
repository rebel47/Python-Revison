# # Sets in Python

# a = {1,2,3,4,5}
# print(a)
# print(type(a))
# a = {1,2,3,4,5,1}# Set is a collection non repeatitive elements, so it will ignore 1
# print(a)

# Empty Set

# Important : This syntax will create an empty dictionary and not a empty set
# a = {}
# print(type(a))

# # An empty set can be created using the below syntax:
# b = set()
# print(type(b))

# SET METHODS

# a = set() # empty set
# a.add(1)
# a.add(2)
# a.add(3)
# a.add(5)
# a.add((4,5,6))
# # a.add({4:5}) #CANNOT ADD LIST AND DICTIONARY IN SET ONLY TUPLES ARE ALLOWED
# print(a)

# print(len(a))# print the length of this set

# a.remove(5) # Remove 5 from set b
# # a.remove(15) # Throws an error while trying to remove 15(which is not present in the set)
# print(a)

# print(a.pop())