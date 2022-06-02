# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
import pandas as pd

df = pd.read_csv('/home/aniket/Desktop/Python/Pandas/dirtyData.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Remove rows with a NULL value in the "Date" column
df.dropna(subset=['Date'], inplace=True)

# Set "Duration" = 45 in row 7
df.loc[7, 'Duration'] = 45

# Loop through all values in the "Duration" column and If the value is higher than 120, set it to 120.
for idx in df.index:
  if df.loc[idx, 'Duration'] > 120:
    df.loc[idx, 'Duration'] = 120


# Delete rows where "Duration" is higher than 120.
for idx in df.index:
  if df.loc[idx, "Duration"] > 120:
    df.drop(idx, inplace=True)
