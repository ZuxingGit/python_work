# https://www.w3schools.com/python/python_strings.asp


# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

# Strings are Arrays
# remember that the first character has the position 0
# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#     print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# --------------------slicing---------------------------------------------------
# b = "Hello, World!"
# print(b[2:5])
# print(b[:5])
# print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
# b = "Hello, World!"
# print(b[-5:-2])

# --------------------Modify Strings--------------------------------------------
# a = "Hello, World!"
# print(a.upper())
# print(a.lower())
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"
# a = "Hello, World!"
# print(a.replace("H", "J"))
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# --------------------String Concatenation--------------------------------------
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# --------------------String Format---------------------------------------------
# F-Strings
# age = 36
# txt = f"My name is John, and I am {age}"
# print(txt)

# Placeholders and Modifiers
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)
# txt = f"The price is {20 * 59} dollars"
# print(txt)

# --------------------Escape Characters-----------------------------------------
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# --------------------String Methods--------------------------------------------
# capitalize() Converts the first character to upper case
# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x)

# txt = "python is FUN!"
# x = txt.capitalize()
# print (x)

# txt = "36 is my age."
# x = txt.capitalize()
# print (x)

# center()    Returns a centered string
# txt = "banana"
# x = txt.center(20)
# print(x)
# x = txt.center(20, "O")
# print(x)

# encode()    Returns an encoded version of the string
# txt = "My name is Ståle"
# x = txt.encode()
# print(x)
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

# find()    Searches the string for a specified value and returns the position of where it was found
# txt = "Hello, welcome to my world."
# # x = txt.find("welcome")
# x = txt.find("e", 5, 10)
# print(x)

# format()    Formats specified values in a string
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt1)
# print(txt2)
# print(txt3)

# x = float('inf')
# txt = "The price is {:F} dollars."
# print(txt.format(x))
# #same example, but with a lower case f:
# txt = "The price is {:f} dollars."
# print(txt.format(x))

#Use "o" to convert the number into octal format:
# txt = "The octal version of {0} is {0:o}"
# print(txt.format(10))

# #Use "x" to convert the number into Hex format:
# txt = "The Hexadecimal version of {0} is {0:x}"
# print(txt.format(255))
# #Use "X" to convert the number into upper-case Hex format:
# txt = "The Hexadecimal version of {0} is {0:X}"
# print(txt.format(255))

#Use "%" to convert the number into a percentage format:
# txt = "You scored {:%}"
# print(txt.format(0.25))

# #Or, without any decimals:
# txt = "You scored {:.0%}"
# print(txt.format(0.25))

# isascii()    Returns True if all characters in the string are ascii characters
# txt = "Company123"
# x = txt.isascii()
# print(x)

# isdecimal()    Returns True if all characters in the string are decimals
# a = "\u0030" #unicode for 0
# b = "\u0047" #unicode for G

# print(a.isdecimal())
# print(b.isdecimal())

# isdigit()    Returns True if all characters in the string are digits
# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for ²

# print(a.isdigit())
# print(b.isdigit())

# isidentifier()    Returns True if the string is an identifier
# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

# isprintable()    Returns True if all characters in the string are printable
# txt = "Hello! Are you #1?"
# txt = "Hello!\nAre you #1?"
# x = txt.isprintable()
# print(x)

# isspace()    Returns True if all characters in the string are whitespaces
# # txt = "   "
# txt = "   s   "
# x = txt.isspace()
# print(x)

# istitle()    Returns True if the string follows the rules of a title
# txt = "Hello, And Welcome To My World!"
# x = txt.istitle()
# print(x)

# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# isupper()    Returns True if all characters in the string are upper case
# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)

# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"
# print(a.isupper())
# print(b.isupper())
# print(c.isupper())

# join()    Joins the elements of an iterable to the end of the string
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)
# print(x)

# ljust()    Returns a left justified version of the string
# txt = "banana"
# x = txt.ljust(20)
# print(x, "is my favorite fruit.")

# txt = "banana"
# x = txt.ljust(20, "+")
# print(x)