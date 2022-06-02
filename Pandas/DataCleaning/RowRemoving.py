'''
Data cleaning means fixing bad data in your data set and bad data could be:

:- Empty cells
:- Data in wrong format
:- Wrong data
:- Duplicates

'''

# NOTE: Empty cells can potentially give you a wrong result when you analyze data.
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

import pandas as pd

df = pd.read_csv('/home/aniket/Desktop/Python/Pandas/dirtyData.csv')

# NOTE: If you want to change the original DataFrame, use the "inplace = True" argument.
df.dropna(inplace = True)

# NOTE: By default, the dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
