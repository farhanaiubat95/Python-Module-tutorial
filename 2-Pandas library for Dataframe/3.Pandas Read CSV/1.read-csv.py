# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
import pandas as pd

dataframe = pd.read_csv(
    r'G:\Python-Module-tutorial\2-Pandas library for Dataframe\titanic.csv')
print(dataframe)
print()
print(dataframe.to_string())  # use to_string() to print the entire DataFrame.


# another way - if you don't want to use r(read)
# dataframe = pd.read_csv(
#    'G:\\Python-Module-tutorial\\2-Pandas library for Dataframe\\3.Pandas Read CSV\\data.csv')


# Maximum rows- can be changed
pd.options.display.max_rows = 10000
print("\n** Maximum rows of this data table is : ", pd.options.display.max_rows)
print(dataframe.head(500))
