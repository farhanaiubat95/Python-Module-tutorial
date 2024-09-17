import numpy as np

# must be (rows x column)
# Convert the following (1-D) array with 12 elements into a (2-D) array.
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_reshape = array.reshape(3, 4)
print("1. 1D to 2D array - 3 x 4 matrix : \n", new_reshape)
print("-> Dimension : ", new_reshape.ndim)

# Convert the following (1-D) array with 12 elements into a (3-D) array.
print()
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_reshape = array.reshape(2, 2, 3)
print("2. 1D to 3D array - 2 x 2 x 3 matrix : \n", new_reshape)
print("-> Dimension : ", new_reshape.ndim)

# Returns Copy or View?
# Check if the returned array is a copy or a view:
print()
print("3. Copy or View ? ans view : \n", array.reshape(3, 4).base)
print("-> Dimension : ", array.ndim)

# Unknown Dimension
# (Pass -1 )as the value, and NumPy will calculate this number for you.
print()
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_array = array.reshape(2, 2, -1)
print("4. Unknown Dimension : \n", new_array)
print("-> Dimension : ", new_array.ndim)


# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
print()
print("5. Multidimensional array : \n", new_array)
print("-> Dimension : ", new_array.ndim)
reshape_array = new_array.reshape(-1)
print("6. Reshape Multidimensional array into a 1D array",reshape_array)
print("-> Dimension : ", reshape_array.ndim)
