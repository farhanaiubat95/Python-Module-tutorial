# One of the most used method for getting a quick overview of the DataFrame, is the head() method.
# The head() method returns the headers and a specified number of rows, starting from the top.
import pandas as pd

dataFrame = pd.read_csv(
    r"G:\Python-Module-tutorial\2-Pandas library for Dataframe\titanic.csv")

# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
print("* Not specified rows number, so it's printed only 5 rows : ")
print(dataFrame.head())

# printing the first 7 rows of the DataFrame
print("\n** First 7 rows are printed below : ")
print(dataFrame.head(1000))


# There is also a tail() method for viewing the last rows of the DataFrame.
# The tail() method returns the headers and a specified number of rows, starting from the bottom.
print("\n# Not specified rows number, so it's printed from last 5 rows : ")
print(dataFrame.tail())

# printing the last 4 rows of the DataFrame
print("\n## Last 4 rows are printed below : ")
print(dataFrame.tail(4))


# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.
print()
print(dataFrame.info())
