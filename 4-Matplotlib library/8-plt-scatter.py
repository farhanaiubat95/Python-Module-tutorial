# The scatter() function plots one dot for each observation.
# It needs two arrays of the same length

import matplotlib.pyplot as plt
import numpy as np

# Color Each Dot
x = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
y = np.array([4, 21, 18, 12, 4, 5, 7, 6, 10, 5])
colors = np.array(['red', 'green', 'orange', 'blue', 'black', 'hotpink',
                  'gray', 'magenta', 'purple', 'yellow'])
plt.scatter(x, y, c=colors)
plt.show()


# Compare Plots
x = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
y = np.array([4, 21, 18, 12, 4, 5, 7, 6, 10, 5])
plt.scatter(x, y, c='r')

x = np.array([3, 6, 9, 12, 15, 18, 21, 24, 28, 30])
y = np.array([12, 21, 18, 12, 4, 5, 7, 6, 10, 5])
plt.scatter(x, y, c='c')

plt.show()


# ColorMap - (cmap)  each color has a value that ranges from (0 to 100.)
# Color Each Dot
# Size- (s)
# the transparency of the dots with the (alpha argument).

x = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])
y = np.array([4, 21, 18, 12, 4, 5, 7, 6, 10, 5, 3])

colors = 0
list = []
for i in range(0, 101, 10):
    list.append(i,)

print(list)
colors = np.array(list)
sizes = np.array(list)
plt.scatter(x, y, c=colors, cmap='viridis', s=sizes, alpha=0.5)
plt.colorbar()
plt.show()


# Combine Color Size and Alpha
x = np.random.randint(10, size=(20))
y = np.random.randint(10, size=(20))
colors = np.random.randint(10, size=(20))
sizes = 10 * np.random.randint(10, size=(20))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='Accent_r')

plt.colorbar()

plt.show()
