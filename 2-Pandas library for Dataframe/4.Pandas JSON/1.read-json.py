# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
import pandas as pd

dataframe = pd.read_json(
    r"G:\Python-Module-tutorial\2-Pandas library for Dataframe\4.Pandas JSON\data.json")
print(dataframe)
