# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# def x(a, b, c):
#     return a + b + c
# print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2) # mydoubler = lambda a : a * 2, it's a function
print(mydoubler(11))
mytripler = myfunc(3) # mytripler = lambda a : a * 3, it's a function
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.
