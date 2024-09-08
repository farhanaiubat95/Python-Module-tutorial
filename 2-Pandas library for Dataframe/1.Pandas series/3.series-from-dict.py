import pandas as pd

exerxise = {
    "day1": 100,
    "day2": 200,
    "day3": 500
}

series = pd.Series(exerxise)
print("1- Exercise 1 :")
print(series)

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
series = pd.Series(exerxise, index=['day1', 'day2'])
print("\n2- Exercise 2 :")
print(series)
