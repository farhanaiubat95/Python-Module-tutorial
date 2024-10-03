# random.normal() method to get a Normal Data Distribution.
# It has three parameters:
# loc   - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size  - The shape of the returned array.

# normal distribution is (continous) whereas binomial is (discrete)
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

array = random.normal(1.75, 2.5, 1000)
# The "bins" are usually specified as consecutive, non-overlapping intervals of a variable.
plt.hist(array, bins=50)
plt.title("Normal Distribution")
plt.show()

array = random.normal(loc=1, scale=2, size=(3, 4))
print('1 - a random normal distribution of size 3x4 :\n', array)

# showing seaborn plot
sns.distplot(array, hist=False)
plt.show()

sns.distplot(random.normal(size=500), hist=False)
plt.show()
# The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.
