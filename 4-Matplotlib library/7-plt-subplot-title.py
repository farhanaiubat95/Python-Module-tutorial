import matplotlib.pyplot as plt
import numpy as np


# ---Column ways
# suptitle()

# plot 1
x = np.array([2, 4, 6, 7, 10])
y = np.array([4, 21, 18, 12, 4])

# the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(1, 2, 1)
plt.title('Car speed data')
plt.plot(x, y)

# plot 2
x = np.array([3, 6, 9, 15, 20])
y = np.array([9, 4, 10, 15, 1])

# the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(1, 2, 2)
plt.title('Petrol used data')
plt.plot(x, y)

plt.suptitle('My car shop',c='g')
plt.show()


# ---Row ways
# plot 1
x = np.array([2, 4, 6, 7, 10])
y = np.array([4, 21, 18, 12, 4])

# the figure has 1 row, 2 columns, and this plot is the first plot.
plt.subplot(2, 1, 1)
plt.title('Car speed data')
plt.plot(x, y)

# plot 2
x = np.array([3, 6, 9, 15, 20])
y = np.array([9, 4, 10, 15, 1])

# the figure has 1 row, 2 columns, and this plot is the second plot.
plt.subplot(2, 1, 2)
plt.title('Petrol used data')
plt.plot(x, y)

plt.show()

# Draw 6 plots