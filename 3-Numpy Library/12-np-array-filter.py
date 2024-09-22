# In NumPy, you filter an array using a boolean index list
# If the value at an index is (True) that element is contained in the "filtered" array,
# if the value at that index is (False) that element is "excluded" from the filtered array.

import numpy as np

array = np.array([10, 20, 50, 45, 100])
x = [True, False, True, True, False]

new_array = array[x]
print("1 - Original Array        : ", array)
print("  -> Filtering True Array : ", new_array)

# Creating the Filter Array
filter_array = []

# go through each element in arr
for element in array:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 45:
        filter_array.append(True)
    else:
        filter_array.append(False)

new_array = array[filter_array]

print()
print("2 - Original Array         : ", array)
print("  -> Filtered Array        : ", filter_array)
print("  -> Filtering True Array  : ", new_array)


# Creating Filter Directly From Array
filter_array = array > 30
new_array = array[filter_array]

print()
print("3 - Original Array         : ", array)
print("  -> Filtered Array        : ", filter_array)
print("  -> Filtering True Array  : ", new_array)


# Create a filter array that will return only even elements from the original array
filter_array = array % 2 == 0
new_array = array[filter_array]

print()
print("4 - Original Array         : ", array)
print("  -> Filtered Array        : ", filter_array)
print("  -> Filtering True Array  : ", new_array)
