# Sorting means putting elements in an ordered sequence.
import numpy as np

array = np.array([4, 5, 2, 1])
print('1 - Original Array : ', array)
print('  -> Sorted Array  : ', np.sort(array))


# Sort the array alphabetically
print()
array = np.array(['BMW', 'Audi', 'Honda', 'Tesla'])
print('2 - Original Array : ', array)
print('  -> Sorted Array  : ', np.sort(array))


# Sort a boolean array
print()
array = np.array([True, False, True, False, False])
print('3 - Original Array : ', array)
print('  -> Sorted Array  : ', np.sort(array))


# Sorting a 2-D Array
print()
array = np.array([[30, 25, 23, 45, 15], [2, 5, 1, 6, 3]])
print('4 - Original Array : ', array)
print('  -> Sorted Array  : \n', np.sort(array))
