# x = 5
# y = "John"
# print(x)
# print(y)

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

# Casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0
# print(x)
# print(y)
# print(z)

# Get the Type
# x = 5
# y = "John"
# print(type(x))
# print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes
# x = "John"
# # is the same as
# y = 'John'
# print(x == y)

# # Case-Sensitive
# # Variable names are case-sensitive
# a = 4
# A = "Sally"
# # A will not overwrite a
# print(a)
# print(A)

# # Many Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# # One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# # Unpack a Collection
# # If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# # output multiple variables, separated by a comma
# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# # For numbers, the + character works as a mathematical operator
# x = 5
# y = 10
# print(x + y)

# # try to combine a string and a number with the + operator
# x = 5
# y = "John"
# # print(x + y)
# print(x, y)

# # Global Variables
# # Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# # Global variables can be used by everyone, both inside of functions and outside.
# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# # If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

# # The global Keyword
# # Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# # To create a global variable inside a function, you can use the global keyword.
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


# # Also, use the global keyword if you want to change a global variable inside a function.
# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

