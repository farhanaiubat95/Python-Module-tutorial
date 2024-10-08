import numpy as np

# ----Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function.

array = np.array([1, 2, 3, 4, 5, 6, 5])

print("1. Mean (average one)        : ", np.mean(array))
print("2. Standard deviation        : ", np.std(array))

# 3 and 4 - you can use any one
print("3. Square Standard deviation : ", np.std(array)**2)
print("4. Variance                  : ", np.var(array))
print("5. Median (Middle One)       : ", np.median(array))
print("6. Unique Values             : ", np.unique(array, return_counts=True))

print()
print("7. List to ndarray : ", array)
print(type(array))  # ndarray object


# ----To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
array = np.array((1, 2, 3, 4))
print()
print("8. Tuple to ndarray : ", array)
print(type(array))


# ----Dimensions in Arrays
# A dimension in arrays is one level of array depth (nested arrays).

# ----0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
array = np.array(50)
print()
print("9. 0-D Arrays : ", array)
print("10. Number of Dimension : ", array.ndim)

# ----1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
print()
array = np.array([1, 2, 3, 4])
print("11. 1-D Arrays : ", array)
print("12. Number of Dimension : ", array.ndim)

# ----2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.
# These are often used to represent matrix or 2nd order tensors.
print()
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13]])
print("13. 2-D Arrays : \n", array)
print("14. Number of Dimension : ", array.ndim)


# ----3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
print()
# 2x(2x3)
array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [
                 [22, 23, 24, 25], [33, 34, 35, 36]]])
print("15. 3-D Arrays : \n", array)
print("16. 3D array shape : ", array.shape)
print("17. Number of Dimension : ", array.ndim)


# ----Higher Dimensional Arrays
# An array can have any number of dimensions.
print()
array = np.array([1, 2, 3, 4], ndmin=4)
print("18. 4-D Arrays : ", array)
print("19. Number of Dimension : ", array.ndim)
