import matplotlib.pyplot as plt
import numpy as np

x = np.array([15, 25, 25, 35])

# The size of each wedge is determined by comparing the value with all the other values,
# by using this formula : The value divided by the sum of all values: x/sum(x)
plt.pie(x)
plt.show()

# lebels
# Shadow
# colors
# Legend - legend() & title
# The startangle - parameter is defined with an angle in degrees, default angle is 0
labels = ["BMW", "Audi", "Honda", "Tesla"]
colors = ["y", "c", "b", "m"]
plt.pie(x, labels=labels, startangle=180, shadow=True, colors=colors)
plt.legend(title='Four car : ')
plt.show()

# Explode -The explode parameter, if specified, and not None, must be an array with one value for each wedge
# Shadow
# Legend - legend()
myexplode = [0, 0, 0, 0.2]
colors = ["hotpink", "m", "c", "r"]
plt.pie(x, labels=labels, startangle=180,
        explode=myexplode, shadow=True, colors=colors)
plt.legend(title='Four car : ')
plt.show()



