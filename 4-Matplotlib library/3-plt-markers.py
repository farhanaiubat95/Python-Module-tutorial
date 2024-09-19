import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 4, 6, 7, 20])
ypoints = np.array([1, 25, 70, 55, 60])

# use shortcut string notation parameter 'o', which means 'rings'
plt.plot(xpoints, ypoints, '*')
plt.show()

plt.plot(xpoints, ypoints, marker='*')
plt.show()


# Format Strings fmt
# marker|line|color
# Line Reference '-', ':', '--', '-.'
# Color Reference 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'
plt.plot(ypoints, '*-.r')
plt.show()


# Marker Size
# Marker Color
# markeredgecolor- mec (border)
# markerfacecolor- mfc (fill)
# Hexadecimal color values- #fff
plt.plot(xpoints, ypoints, 'o-.k', ms=20, mec='y', mfc='g')
plt.show()
