# Rayleigh distribution is used in "signal processing".
# It has two parameters:
# scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size  - The shape of the returned array.

from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

array = rd.rayleigh(scale=2, size=(2, 3))
print("1. Rayleigh distribution : \n", array)

sns.distplot(rd.rayleigh(size=3000), hist=False)
plt.title('Rayleigh distribution ')
plt.show()
