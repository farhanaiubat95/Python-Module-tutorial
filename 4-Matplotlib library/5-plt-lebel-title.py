import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 4, 6, 7, 10])
ypoints = np.array([4, 21, 18, 12, 4])

# use shortcut string notation parameter 'o', which means 'rings'
plt.plot(xpoints, ypoints, 'o-')
plt.title("Student's Performance Data")
plt.xlabel('Students')
plt.ylabel('Average marks')
plt.show()

# Font Properties
# fontdict
# Position the Title- (loc)
font1 = {'family': 'serif', 'color': 'm', 'size': 16}
font2 = {'family': 'serif', 'color': 'g', 'size': 10}

plt.plot(xpoints, ypoints, 'o-')

plt.title("Student's Performance Data", fontdict=font1, loc='left')
plt.xlabel('Students', fontdict=font2, loc='right')
plt.ylabel('Average marks', fontdict=font2)
plt.show()
