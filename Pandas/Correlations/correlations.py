# The corr() method calculates the relationship between each column in your data set.
# NOTE: The corr() method ignores "not numeric" columns.

import pandas as pd

df = pd.read_csv('/home/aniket/Desktop/Python/Pandas/pulse_data.csv')
print(df.corr())

# What is a good correlation? It depends on the use, 
# but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.