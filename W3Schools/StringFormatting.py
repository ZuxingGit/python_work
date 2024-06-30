# # Add a placeholder for the price variable:
# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# # Display the price with 2 decimals:
# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)


# # Display the value 95 with 2 decimals:
# txt = f"The price is {95:.2f} dollars"
# print(txt)


# # Perform a math operation in the placeholder, and return the result:
# txt = f"The price is {20 * 59} dollars"
# print(txt)


# # Add taxes before displaying the price:
# price = 59
# tax = 0.25
# txt = f"The price is {price + (price * tax)} dollars"
# print(txt)


# # Return "Expensive" if the price is over 50, otherwise return "Cheap":
# price = 49
# txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
# print(txt)


# # You can execute functions inside the placeholder:
# fruit = "apples"
# txt = f"I love {fruit.upper()}"
# print(txt)


# # you can create your own functions and use them:
# def myconverter(x):
#   return x * 0.3048
# txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
# print(txt)


# # Use a comma as a thousand separator:
# price = 59000
# txt = f"The price is {price:,} dollars"
# print(txt)

# # Converts a value into the corresponding Unicode character
# # use :c
# txt = 66
# print(f"Unicode character: {txt:c}")


# #Use "d" to convert a number, in this case a binary number, into decimal number format:
# txt = f"We have {0b101:d} chickens."
# print(txt)


# #Use "e/E" to convert a number into scientific number format (with an upper-case E):
# txt = f"We have {5:e} chickens."
# print(txt)
# txt = f"We have {5:E} chickens."
# print(txt)


# #Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
# txt = f"The price is {45:.2f} dollars."
# print(txt)

# #without the ".2" inside the placeholder, this number will be displayed like this:
# txt = f"The price is {45:f} dollars."
# print(txt)


# #Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
# x = float('inf')
# txt = f"The price is {x:F} dollars."
# print(txt)

# #same example, but with a lower case f:
# txt = f"The price is {x:f} dollars."
# print(txt)


# # general format
# price = 45
# txt = f"The price is {price:g} dollars."
# print(txt)


# #Use "o" to convert the number into octal format:
# txt = f"The octal version of 10 is {10:o}"
# print(txt)


# #Use "x" to convert the number into Hex format:
# txt = f"The Hexadecimal version of 255 is {255:x}"
# print(txt)

# #Use "X" to convert the number into upper-case Hex format:
# txt = f"The Hexadecimal version of 255 is {255:X}"
# print(txt)


# :n is used to format numbers with a specific number of digits
txt = f"The number is: {5:0>2}"
print(txt)


#Use "%" to convert the number into a percentage format:
txt = f"You scored {0.25:%}"
print(txt)

#Or, without any decimals:
txt = f"You scored {0.25:.2%}"
print(txt)


price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))


# add multiple placeholders
quantity = 3
itemno = 567
price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


# refer to the same value more than once
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# use named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))