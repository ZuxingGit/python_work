# https://www.w3schools.com/python/python_tuples.asp
# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# # One item tuple, remember the comma:
# thistuple = ("apple",)
# print(type(thistuple))
# #NOT a tuple, it's a str
# thistuple = ("apple")
# print(type(thistuple))

# Using the tuple() method to make a tuple:
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# Return the third, fourth, and fifth item:
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# This example returns the items from index -4 (included) to index -1 (excluded)
# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# Convert the tuple into a list to be able to change it:
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# Convert the tuple into a list, add "orange", and convert it back into a tuple:
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# Create a new tuple with the value "orange", and add that tuple:
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y
# print(thistuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# The del keyword can delete the tuple completely:
# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a tuple:
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# Assign the rest of the values as a list called "red":
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# Add a list of values the "tropic" variable:
# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (green, *tropic, red) = fruits
# print(green)
# print(tropic)
# print(red)

# Print all items by referring to their index number:
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# Print all items, using a while loop to go through all the index numbers:
# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# Join two tuples:
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# Multiply the fruits tuple by 2:
# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)

# Return the number of times the value 5 appears in the tuple:
# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.count(5)
# print(x)

# Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)