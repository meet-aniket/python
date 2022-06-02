import pandas as pd

df = pd.read_json('/home/aniket/Desktop/Python/Pandas/data.json')

# NOTE: The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())

# NOTE: The info() method also tells us how many Non-Null values there are present in each column.
# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values.

# NOTE: if the number of rows is not specified, the head() method will return the top 5 rows of DataFrame.
print(df.head())

# NOTE: The tail() method returns the headers and a specified number of rows, starting from the bottom.
print(df.tail())