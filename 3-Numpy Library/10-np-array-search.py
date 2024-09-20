import numpy as np

# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.

array = np.array([1, 7, 3, 7, 5, 7, 7])
x = np.where(array == 7)  # return indx [1],[3],[5],[6]
print('1- index position of 7 : ', x)

# condition
array = np.array([1, 2, 3, 7, 5, 6, 10])
x = np.where(array % 2 == 0)  # return indx [1],[5]
print('2- index position of even numbers : ', x)


# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array,
# and returns the index where the specified value would be inserted to maintain the search order.

x = np.searchsorted(array, 7)  # return indx 3
print('3- index position of 7 : ', x)

array = np.array([1, 2, 3, 7, 5, 6, 10])
# side='right' to return the right most index instead
x = np.searchsorted(array, 7, side='right')  # return indx 3
print('4- index position of 7 : ', x)


# Multiple Values
# To search for more than one value, use an array with the specified values.
x = np.searchsorted(array, [4, 8])  # 3,6
print('5- Multiple Values : ', x)
