# Replace using fillna()

# NOTE: Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The "fillna()" method allows us to replace empty cells with a value:

import pandas as pd

df = pd.read_csv('/home/aniket/Desktop/Python/Pandas/dirtyData.csv')
# df.fillna(130, inplace=True)

# NOTE: To only replace empty values for one column, specify the column name for the DataFrame
# df['Calories'].fillna(130, inplace=True)

# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean(), median() and mode() methods to calculate the respective values for a specified column.

# NOTE: Mean = the average value (the sum of all values divided by number of values)
mean = df['Calories'].mean()
df['Calories'].fillna(mean, inplace=True)

# NOTE: Median = the value in the middle, after you have sorted all values ascending
median = df['Calories'].median()
df['Calories'].fillna(median, inplace=True)

# NOTE: Mode = the value that appears most frequently
mode = df['Calories'].mode()
df['Calories'].fillna(mode, inplace=True)