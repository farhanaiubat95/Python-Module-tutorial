# the (copy) is a new array. &
# The copy owns the data and any changes made to the copy will not affect original array,

# the (view) is just a view of the original array. & The view does not own the data. &
# any changes made to the view will affect the original arra

import numpy as np

#copy
array = np.array([1, 3, 4, 5, 6, 7])
a_copy = array.copy()
print("1. Original Data : ", array)
array[0] = 70
print("* Print copy data : ", a_copy)
print("* Print original data after changing index[0]=70 : ", array)

#View
a_view = array.view()
print()
print("2. Original Data : ", array)
array[0] = 50
print("* Print view data : ", a_view)
print("* Print original data after changing index[0]=50 : ", array)


# Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns (None) if the array (owns) the data.
# Otherwise, the base  attribute refers to the (original object).
print()
print("-> Copy has its Own data, so : ",a_copy.base)
print("-> View does not has its Own data, so : ",a_view.base)