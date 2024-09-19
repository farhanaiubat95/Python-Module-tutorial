import matplotlib.pyplot as plt
import numpy as np

# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval.
# we use NumPy to randomly generate an array with 250 values,
# where the values will concentrate around 170, and the standard deviation is 10.
x = np.random.normal(100, 10, 20)

plt.hist(x, color='green')
plt.show()
