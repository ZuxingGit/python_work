# f = open("W3Schools/FileHandling/demofile.txt", "r")
# # print(f.read())
# # print(f.read(5))
# print(f.readline())
# print(f.readline())


# f = open("W3Schools/FileHandling/demofile.txt", "r")
# for x in f:
#   print(x)
# f.close()


# f = open("W3Schools/FileHandling/demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# f = open("W3Schools/FileHandling/demofile2.txt", "r")
# print(f.read())


# f = open("W3Schools/FileHandling/demofile2.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# f = open("W3Schools/FileHandling/demofile2.txt", "r")
# print(f.read())


# # f = open("W3Schools/FileHandling/demofile3.txt", "x")
# f = open("W3Schools/FileHandling/demofile3.txt", "w")
# f.write("x - Create - will create a file, returns an error if the file exist\n")
# f.write("a - Append - will create a file if the specified file does not exist\n")
# f.write("w - Write - will create a file if the specified file does not exist")
# f.close()


import os
# # os.remove("W3Schools/FileHandling/demofile3.txt")
# if os.path.exists("W3Schools/FileHandling/demofile3.txt"):
#   os.remove("W3Schools/FileHandling/demofile3.txt")
# else:
#     print("The file does not exist")

# You can only remove empty folders
os.rmdir("W3Schools/FileHandling/myfolder")