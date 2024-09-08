import pandas as pd

list = [10, 30, 50]
series = pd.Series(list, index=["A", "B", 'C'])
print(series)

# check lebels
print("\n* Lebel of B is : ", series['B'])
