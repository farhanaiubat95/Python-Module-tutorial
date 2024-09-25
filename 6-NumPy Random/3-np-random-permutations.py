# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
#  two methods for this: shuffle() and permutation().

import numpy as np
from numpy import random

# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('1 -  Original Array : ', array)

random.shuffle(array)
print('  -> By shuffle, changing arrrangement randomly : ', array)


# Generating Permutation of Arrays
print()
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('2 -  Original Array : ', array)

print('  -> By Permutation, returns a re-arranged array : ', random.permutation(array))