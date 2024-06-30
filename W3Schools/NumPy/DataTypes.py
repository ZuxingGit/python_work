# https://www.w3schools.com/python/numpy/numpy_data_types.asp

# Get the data type of an array object:
import numpy as np
# arr = np.array([1, 2, 3, 4])
# print(arr.dtype)
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5], dtype='i4')
# print(arr)
# print(arr.dtype)

# # Change data type from float to integer by using 'i/int' as parameter value:
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)


# Change data type from integer to boolean:
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)