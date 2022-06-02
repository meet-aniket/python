# Discovering duplicates
import pandas as pd

df = pd.read_csv('/home/aniket/Desktop/Python/Pandas/dirtyData.csv')
df.drop_duplicates(inplace=True)
print(df.duplicated())