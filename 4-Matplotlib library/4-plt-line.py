import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1, 25, 20, 40, 0])
plt.plot(ypoints, linestyle='dotted', marker='*')
plt.show()

# color- c
#  Hexadecimal color values:
# 140 supported color names
plt.plot(ypoints, c='y', marker='^')
plt.show()


# Line Width- lw
plt.plot(ypoints, lw='5.2', c='c', marker='x')
plt.show()


# Multiple Lines
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
x2 = np.array([0, 1, 2, 3])

plt.plot(y1, c='y')
plt.plot(y2, c='g')
plt.show()

# two lines by specifiyng the x- and y-point
plt.plot(x1, y1, x2, y2)
plt.show()
