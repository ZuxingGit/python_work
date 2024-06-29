import re

# Search the string to see if it starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")


#Check if the string ends with "Spain":
# txt = "The rain in Spain"
# x = re.findall("Spain\Z", txt)
# print(x)
# if x:
#   print("Yes, there is a match!")
# else:
#   print("No match")


# # Split the string only at the first occurrence:
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())

# https://www.w3schools.com/python/python_regex.asp#sub