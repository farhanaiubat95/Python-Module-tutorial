import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 4, 6, 7, 10])
ypoints = np.array([4, 21, 18, 12, 4])

# use shortcut string notation parameter 'o', which means 'rings'
plt.plot(xpoints, ypoints, 'o-')
plt.title("Student's Performance Data")
plt.xlabel('Students')
plt.ylabel('Average marks')

# Grid Lines to a Plot
# plt.grid()
# grid(color = 'color', linestyle = 'linestyle', linewidth = number)
plt.grid(axis='x',c='r',ls='--',lw='1')
plt.show()
