# try:
#     print(x)
# except:
#     print("An exception occurred")


# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")


# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# Try to open and write to a file that is not writable:
# # f = open("W3Schools/new/demofile.txt")
# try:
#   f = open("W3Schools/new/demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")


# Raise an error and stop the program if x is lower than 0:
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


# Raise a TypeError if x is not an integer:
x = "hello"
if not isinstance(x, int):
  raise TypeError("Only integers are allowed")