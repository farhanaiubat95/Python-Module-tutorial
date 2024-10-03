# Exponential distribution is used for describing time till next event e.g. failure/success etc.
# It has two parameters:
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size  - The shape of the returned array.

from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

array = rd.exponential(scale=2, size=(2, 3))
print("1. Exponential Distribution : \n", array)

sns.distplot(rd.exponential(size=3000), hist=False)
plt.show()

# Relation Between Poisson and Exponential Distribution

# Poisson distribution deals with number of occurences of an event in a time period whereas
# exponential distribution deals with the time between these events.
