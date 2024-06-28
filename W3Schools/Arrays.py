# cars = ["Ford", "Volvo", "BMW"]
# print(cars)
# print(type(cars))
# print(len(cars))

# for x in cars:
#     print(x)

# cars.append("Honda")
# print(cars)

# # cars.pop(1)
# # print(cars)

# cars.remove("Volvo")
# print(cars)

# # Sort the list descending:
# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort(reverse=True)
# print(cars)

# Sort the list by the length of the values:
# A function that returns the length of the value:
# def myFunc(e):
#   return len(e)
# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
# cars.sort(key=myFunc)
# print(cars)

# Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
# def myFunc(e):
#   return e['year']
# cars = [
#   {'car': 'Ford', 'year': 2005},
#   {'car': 'Mitsubishi', 'year': 2000},
#   {'car': 'BMW', 'year': 2019},
#   {'car': 'VW', 'year': 2011}
# ]
# cars.sort(key=myFunc)
# print(cars)

# Sort the list by the length of the values and reversed:
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)