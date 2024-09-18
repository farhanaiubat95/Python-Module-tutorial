import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 60])
ypoints = np.array([0, 20])

plt.plot(xpoints, ypoints)
plt.show()

# use shortcut string notation parameter 'o', which means 'rings'
plt.plot(xpoints, ypoints, 'o')
plt.show()

# Multiple Points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


# Default X-Points
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
