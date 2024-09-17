# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].

import numpy as np

array = np.array([20, 30, 5, 35, 25, 70, 6, 7])
print("1. 1-D Array : \n", array)
print("* After slicing 1 to 5 : ", array[1:5])
print("* After slicing 0 to 3 : ", array[:3])
print("* After slicing 4 to len : ", array[4:])

# Negative Slicing (the minus operator to refer to an index from the end)
print("* After slicing -4 to -1 : ", array[-4:-1])

# STEP
# Use the step value to determine the step of the slicing
print("* After slicing 1 to 6 , taking gap 3 : ", array[1:6:3])
print("* After slicing 0 to len , taking gap 3 : ", array[::3])

# Slicing 2-D Arrays
print()
array = np.array([[1, 2, 3, 4, 15, 25, 35, 45], [5, 6, 7, 8, 10, 20, 30, 40]])
print("2-D Arrays : \n", array)
print("* After slicing 1, 2 to 7 : ", array[1, 2:7])

# From both elements, return index 2
print("* After slicing 0 & 1, index 3: ", array[0:2, 3])
print("* After slicing 0 & 1, 2 to 7 :\n", array[0:2, 2:7])
