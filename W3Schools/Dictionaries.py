# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # print(thisdict)
# print(thisdict["brand"])

# Duplicate values will overwrite existing values:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)
# print(len(thisdict))

# String, int, boolean, and list data types:
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict)
# print(type(thisdict))

# Using the dict() method to make a dictionary:
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.keys()
# print(x)    #before the change
# thisdict["color"] = "white"
# print(x)    #after the change
# print(thisdict.values())
# print(type(x))

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change
# print(type(x))

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x) #after the change
# print(type(x))

# Add a new item to the original dictionary, and see that the items list gets updated as well:
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["color"] = "red"
# print(x) #after the change

# # Check if "model" is present in the dictionary:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change the "year" to 2018:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)
# thisdict.update({"year": 2020})
# print(thisdict)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   print(x, y)

# Make a copy of a dictionary with the copy() method:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# Make a copy of a dictionary with the dict() method:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# for x, obj in myfamily.items():
#     print(x)
#     for y in obj:
#         print(y + ':', obj[y])

# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# Get the value of the "model" item:
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.setdefault("model", "Bronco")
# print(x)

# Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.setdefault("color", "white")
# print(x)
# print(car)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car['model']
)