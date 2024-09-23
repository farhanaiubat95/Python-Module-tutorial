# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
# Random numbers generated through a generation algorithm are called (pseudo random).
# randint()
# rand()
# choice()

from numpy import random

# Generate a random integer from 0 to 200:
num = random.randint(200)
print("1 - Print a random integer number from 0 to 200 :  ", num)

# Generate Random integer (Array)
# 1-D array
num = random.randint(300, size=(6))  # size = index[0, 1, 2, 3, 4, 5]
print("2 - Print 1D arrays containing 6 random integers number from 0 to 300 :  ", num)

# 2-D array
num = random.randint(100, size=(4, 6))  # 4 rows
print("3 - Print 2D arrays containing 4 rows & 6 columns random integers number from 0 to 100 :  \n", num)

# rand() method
# Generate a random float from 0 to 1:
print()
num = random.rand()
print("4 - Print a random float number from 0 to 1 :  ", num)

# 1-D array
num = random.rand(5)
print("5 - Print 1D arrays containing 5 random float number from 0 to 1 :  \n\t", num)

# 2-D array
num = random.rand(3, 4)  # 3 rows & 4 columns
print("6 - Print 2D arrays containing 3 rows & 4 columns random float number from 0 to 1 :  \n", num)

# choice() method
# Generate Random Number From Array
print()
# 1-D array that consists of the values
num = random.choice([10, 20, 9, 3, 15, 100, 30])
print("6 - Print a value from 1D array[10, 20, 9, 3, 15, 100, 30] :  ", num)

# 2-D array that consists of the values
num = random.choice([10, 20, 9, 3, 15, 100, 30], size=(3, 4))
print("7 - Print a value from 2D array[10, 20, 9, 3, 15, 100, 30] :  \n", num)
