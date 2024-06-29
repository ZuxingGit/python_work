# If you use the global keyword, the variable belongs to the global scope:
# def myfunc():
#   global x
#   x = 300
#   print(x)
# myfunc()
# print(x)


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
# x = 300
# def myfunc():
#   global x
#   x = 200
# myfunc()
# print(x)

# If you use the nonlocal keyword, the variable will belong to the outer function:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())