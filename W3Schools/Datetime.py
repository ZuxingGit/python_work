import datetime

x = datetime.datetime.now()
print(x)
# Return the year and name of weekday:
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%C"))
print(x.strftime("%%"))

# x = datetime.datetime(2020, 5, 17)
# print(x)

# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))