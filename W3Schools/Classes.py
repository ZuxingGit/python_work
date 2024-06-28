# class MyClass:
#   x = 5

# print(MyClass)
# p1 = MyClass()
# print(p1.x)


# Create a class named Person, use the __init__() function to assign values for name and age:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)


# The string representation of an object WITHOUT the __str__() function:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)
# print(p1)


# The string representation of an object WITH the __str__() function:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)
# print(p1)


# Insert a function that prints a greeting, and execute it on the p1 object:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()


# Use the words mysillyobject and abc instead of self:
# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
# p1.age = 40
# print(p1.age)
# del p1.age
# # print(p1.age) # AttributeError: 'Person' object has no attribute 'age'
# del p1
# print(p1) # NameError: name 'p1' is not defined

