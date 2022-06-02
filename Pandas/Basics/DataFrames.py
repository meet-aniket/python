# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

# Pandas uses the loc attribute to return one or more specified row(s)

# This will return single single row with index '0'
print(df.loc[0]);

# This will return a Pandas Series
print(df.loc[[0, 1]])

# NOTE: When using [] result will be Pandas DataFrame


''' Named Indexes in DataFrames '''
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)