# It is a one-dimensional array holding data of any type.
import pandas as pd

list = [10, 30, 50]
series = pd.Series(list)
print(series)

# lebels check
print("\n* Lebel of 2 is : ", series[2])
