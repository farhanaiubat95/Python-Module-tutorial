# Joining NumPy Arrays
# Joining means putting contents of two or more arrays in a single array.
# [concatenate()] - function, along with the axis.
# If axis is not explicitly passed, it is taken as 0.
# stack()
# hstack()- Stacking Along rows
# vstack()- Stacking Along Columns
# dstack()- Stacking Along Height (depth)

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("1. Array1 : ", array1)
print("2. Array2 : ", array2)

array = np.concatenate((array1, array2))
print("3. Adding 2 arrays : ", array)


# Join two 2-D arrays along - [rows (axis=1)]
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
print("\n4. Array1 : \n", array1)
print("5. Array2 : \n", array2)

array = np.concatenate((array1, array2), axis=1)
print("\n6. Adding 2 arrays : \n", array)


# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print("\n7. Array1 : ", array1)
print("8. Array2 : ", array2)

array = np.stack((array1, array2), axis=1)
print("\n9. Adding 2 arrays : \n", array)


# Stacking Along Rows
# NumPy provides a helper function: [hstack()] to stack along rows.
array = np.hstack((array1, array2))
print("\n10. Adding 2 arrays : ", array)


# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.
array = np.vstack((array1, array2))
print("\n11. Adding 2 arrays : \n", array)


# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
array = np.dstack((array1, array2))
print("\n12. Adding 2 arrays : \n", array)