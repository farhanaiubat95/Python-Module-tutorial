# Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g.
# the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
# It has two parameters:
# a    - distribution parameter.
# size - The shape of the returned array.

from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

array = rd.zipf(a=2, size=(2, 3))
print("1. Zipf's Distribution : \n", array)

# 'Visualization of Zipf Distribution'
# -> Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.
array = rd.zipf(a=2, size=2000)
sns.distplot(array[array < 10], kde=False)
plt.title("Zipf's Distribution 1")
plt.show()

sns.distplot(array[array < 10], kde=True)
plt.title("Zipf's Distribution 2")
plt.show()
