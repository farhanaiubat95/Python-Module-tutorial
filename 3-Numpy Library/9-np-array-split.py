# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
new_array = np.array_split(array, 3)

print('1. divide into 2 colums : ', new_array)
print('  -> * Index serial ways print indx[0], indx[1], indx[2] :\n',
      new_array[0], new_array[1], new_array[2])

new_array1 = np.array_split(array, 4)
print('\n2. divide into 4 colums : ', new_array1)
print('  -> * Index serial ways print indx[0], indx[1], indx[2], indx[3] :\n',
      new_array1[0], new_array1[1], new_array1[2], new_array1[3])


# Splitting 2-D Arrays
# Use the same syntax when splitting 2-D arrays.

# axis
# The example below also returns three 2-D arrays,
# but they are split along the row (axis=1).

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
                 10, 11, 12], [13, 14, 15], [16, 17, 18]])

new_array = np.array_split(array, 3)
print('\n3. divide into 3 colums : \n', new_array)

new_array = np.array_split(array, 3, axis=1)
print('\n4. divide into 3 colums axis=1: \n', new_array)


#  using hsplit() opposite of hstack()
# Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().