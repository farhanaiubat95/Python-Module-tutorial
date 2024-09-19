import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D', 'E'])
y = np.array([4, 10, 6, 9, 15])

# Bar Color - (color)
# Bar Width - The default width value is 0.8
plt.bar(x, y, color='r', width=0.5)
plt.show()

# Horizontal Bars - The default height value is 0.8
plt.barh(x, y, height=0.5)
plt.show()
