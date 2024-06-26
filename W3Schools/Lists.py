# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry"))
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# # Change the second value by replacing it with two new values:
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# # Change the second and third value by replacing it with one value:
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# # Insert "watermelon" as the third item:
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# # To add an item to the end of the list, use the append() method
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# # To append elements from another list to the current list, use the extend() method
# # Add the elements of tropical to thislist:
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# # Add elements of a tuple to a list
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# # Remove "banana":
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# Print all items in the list, one by one:
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# Loop through the index numbers
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# Print all items, using a while loop to go through all the index numbers
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# A short hand for loop that will print all items in a list:
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)
# --------------------------------
# With list comprehension you can do all that with only one line of code:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # newlist = [x if x != "banana" else "orange" for x in fruits]
# newlist = ['orange' if x == 'banana' else x for x in fruits]
# print(newlist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# Sort the list based on how close the number is to 50:
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# Case sensitive sorting can give an unexpected result:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # thislist.sort()
# thislist.sort(key=str.lower)
# print(thislist)

# Reverse the order of the list items:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# Make a copy of a list with the list() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)