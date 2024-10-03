# Logistic Distribution is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.
# It has three parameters:
# loc   - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size  - The shape of the returned array.

from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

array = rd.logistic(loc=1, scale=2, size=(2, 3))
print("1. Logistic distribution : \n", array)
sns.distplot(array, hist=False)
plt.show()

sns.distplot(rd.logistic(size=2000), hist=False)
plt.show()


# Difference Between Logistic and Normal Distribution
# Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
# For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.

sns.distplot(rd.normal(loc=1, scale=2, size=2000), hist=False, label='normal')
sns.distplot(rd.logistic(size=2000), hist=False, label='logistic')

plt.show()
