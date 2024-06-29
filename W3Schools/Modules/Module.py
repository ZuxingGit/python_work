# import mymodule

# # mymodule.greeting("Jonathan")
# a = mymodule.person1["age"]
# print(a)


# import mymodule as mx

# a = mx.person1["age"]
# print(a)


# import platform

# x = platform.system()
# print(x)


# List all the defined names belonging to the platform module:
# import platform
# import mymodule as mx

# x = dir(platform)
# print(x)
# x = dir(mx)
# print(x)


# Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"])