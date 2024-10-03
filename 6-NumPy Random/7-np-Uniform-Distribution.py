# Used to describe probability where every event has equal chances of occuring.
# E.g. Generation of random numbers.
# It has three parameters:
# a - lower bound - default 0 .0.
# b - upper bound - default 1.0.
# size - The shape of the returned array.

from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

array = rd.uniform(size=(2, 3))

print('1 - Original array : \n', array)

sns.distplot(array, hist=False)
plt.show()

sns.distplot(rd.uniform(size=1000), hist=False)
plt.show()