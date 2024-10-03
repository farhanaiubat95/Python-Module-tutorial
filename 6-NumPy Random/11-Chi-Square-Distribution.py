# Chi Square distribution is used as a basis to verify ("the hypothesis").
# It has two parameters:
# df   - (degree of freedom).
# size - The shape of the returned array.

from numpy import random as rd
import matplotlib.pyplot as plt
import seaborn as sns

array = rd.chisquare(df=2, size=(2, 3))
print("1. Chi Square Distribution : \n", array)

sns.distplot(rd.chisquare(df=2, size=3000), hist=False)
plt.title('Chi Square Distribution ')
plt.show()
