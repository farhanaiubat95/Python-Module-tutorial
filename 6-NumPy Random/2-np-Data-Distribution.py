# 'Data Distribution' is a (list) of all possible values, and how often each value occurs.
# Such lists are important when working with ("statistics and data science").

# 'Random Distribution'
# A random distribution is a set of random numbers that follow a certain ("probability density function.")
# Probability Density Function :-  A function that describes a continuous probability. i.e. probability of all values in an array.

from numpy import random as rd

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
# The probability for the value to be 3 is set to be 0.1
# The probability for the value to be 5 is set to be 0.3
# The probability for the value to be 7 is set to be 0.6
# The probability for the value to be 9 is set to be 0

# 1D array
# The sum of all probability numbers should be 1. p=[0.1, 0.3, 0.4, 0.2]
num = rd.choice([4, 8, 16, 24], p=[0.1, 0.3, 0.4, 0.2], size=(10))
print('1 - 1D array data distributed into 10 values : ', num)

# 2D array
# The sum of all probability numbers should be 1. p=[0.1, 0.3, 0.4, 0.2]
print()
num = rd.choice([4, 8, 16, 24], p=[0.1, 0.2, 0.7, 0.0], size=(3, 4))
print('2 - 2D array data distributed into 3 rows & 4 columns values : \n', num)
