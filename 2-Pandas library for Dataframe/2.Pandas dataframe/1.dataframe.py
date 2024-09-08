# It is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
import pandas as pd

data = {
    "car_speed": [100, 250, 480],
    "Time": [20, 30, 45]
}

# load data into a DataFrame object:
dataframe = pd.DataFrame(data)

print("\n* All Data rows are:")
print(dataframe)

# Pandas use the loc attribute to return one or more specified row(s)
print("\n** Row of 1 is :")
print(dataframe.loc[1])

# use a list of indexes:
print("\n*** Row of 1 & 2 are :")
print(dataframe.loc[[1, 2]])

# With the index argument, you can name your own indexes.
dataframe = pd.DataFrame(data, index=['No-1 :', 'No-2 :', 'No-3 :'])
print("\n# All Data rows are:")
print(dataframe)

print("\n## Row of 1 & 2 are :")
print(dataframe.loc[['No-1 :', 'No-2 :',]])
