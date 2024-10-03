# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
# It has two parameter:
# a    - shape parameter.
# size - The shape of the returned array.

from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

array = rd.pareto(a=2, size=(2, 3))
print("1. Pareto Distribution : \n", array)

sns.distplot(rd.pareto(a=2, size=1000), kde=False)
plt.title('Pareto Distribution 1 ')
plt.show()

sns.distplot(rd.pareto(a=3, size=3000), kde=True)
plt.title('Pareto Distribution 2 ')
plt.show()
