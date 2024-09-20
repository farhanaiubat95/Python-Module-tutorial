# Iterating means going through elements one by one.
# we can do this using basic for loop of python
# Iterating Arrays Using - [ nditer()]
# Different Data Types
# Different Step Size
# Enumerated Iteration Using ndenumerate()

import numpy as np

# iterate on (a 1-D array)
array1 = np.array([1, 2, 34])
print("1. 1D array iterating:")
for x in array1:
    print(x)


# Iterating (2-D Arrays)
# In a 2-D array it will go through (all the rows).
array2 = np.array([[1, 2, 34], [10, 20, 25]])
print("\n2. 2D array iterating -rows:")
for x in array2:
    print(x)


# If we iterate on a n-D array it will go through n-1th dimension one by one.
print("\n2. 2D array iterating one by one:")
for x in array2:
    for y in x:
        print(y)


# Iterating 3-D Arrays
# In a 3-D array it will go through all the 2-D arrays.
array3 = np.array([[[1, 2], [4, 5]], [[7, 8], [10, 11]]])
print("\n3. 3D array iterating -rows:")
for x in array3:
    print(x)


# If we iterate on a n-D array it will go through n-1th dimension one by one.
# Iterate down to the scalars
print("\n3. 3D array iterating one by one:")
for x in array3:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using - [ nditer()]
print("\n4. 3D array iterating one by one directly:")
for x in np.nditer(array3):
    print(x)


# Iterating Array With Different Data Types
# op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
# extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered']
print("\n5. 1D array iterating 'int to string' :")
for x in np.nditer(array1, flags=['buffered'], op_dtypes=['S']):
    print(x)


# Iterating With Different Step Size
print('\n6. Print Original Array : \n', array2)
print("\n6. 2D array iterating Different Step Size :")
for x in np.nditer(array2[:, ::2]):  # [r1:r2, indx-start:indx-end:step]
    print(x)


# Enumerated Iteration Using - [ndenumerate()]
# Enumeration means mentioning sequence number of somethings one by one.
print("\n7. 2D array iterating Enumerated :")
for idx, x in np.ndenumerate(array2):  
    print(idx, x)

print("\n8. 3D array iterating Enumerated :")
for idx, x in np.ndenumerate(array3):  
    print(idx, x)

print("\n9. 1D array iterating Enumerated :")
for idx, x in np.ndenumerate(array1):  
    print(idx, x)