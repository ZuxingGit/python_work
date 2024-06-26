# Check if "banana" is present in the set:
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)
# print("banana" not in thisset)

# Add an item to a set, using the add() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# Add elements from tropical into thisset:
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# Add elements of a list to at set:
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# Remove "banana" by using the remove() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)

# Remove "banana" by using the discard() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)

# Remove a random item by using the pop() method:
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x)
# print(thisset)

# The clear() method empties the set:
# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# The del keyword will delete the set completely:
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# Join set1 and set2 into a new set:
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# # set3 = set1.union(set2)
# set3 = set1 | set2
# print(set3)

# Join multiple sets with the union() method:
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# # myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 | set4
# print(myset)

# Join a set with a tuple:
# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)
# print(z)

# The update() method inserts the items in set2 into set1:
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# # The update() method inserts all items from one set into another.
# # changes the original set, and does not return a new set.
# print(set1)

# # Join set1 and set2, but keep only the duplicates:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set1)
# print(set3)

# # Use & to join two sets:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set1)
# print(set3)

# # Keep the items that exist in both set1, and set2:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection_update(set2)
# print(set1)
# print(set3)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

# # Keep all items from set1 that are not in set2:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)

# # Use - to join two sets:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

# # Use the difference_update() method to keep the items that are not present in both sets:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

# # Keep the items that are not present in both sets:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# Use ^ to join two sets:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)

# Return True if no items in set x is present in set y:
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}
# z = x.isdisjoint(y)
# print(z)

# # Return True if all items in set x are present in set y:
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# # z = x.issubset(y)
# z = x <= y
# print(z)

# # Return True if all items set y are present in set x:
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# # z = x.issuperset(y)
# z = x >= y
# print(z)

# Use ^= as a shortcut instead of symmetric_difference_update():
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x ^= y
# print(x)

