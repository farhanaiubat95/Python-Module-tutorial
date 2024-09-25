# Binomial Distribution is a Discrete Distribution.
# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
# It has three parameters:
# n    - number of trials.
# p    - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.

# normal distribution is (continous) whereas binomial is (discrete)
# but if there are enough data points it will be quite similar to normal distribution with certain "loc and scale."

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

array = random.binomial(n=100, p=0.5, size=500)
print(array)

# Visualization of Binomial Distribution
sns.distplot(array, hist=True, kde=False)
plt.show()

# Difference Between Normal and Binomial Distribution
print()
array1 = random.normal(loc=50, scale=5, size=500)
sns.distplot(array1, hist=False, label='normal')
sns.distplot(array, hist=False, label='binomial')

plt.show()