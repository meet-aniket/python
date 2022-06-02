# Series: are like columns in a table in Pandas, it is a one dimensional array holding data of any type.

import pandas as pd

data = { "day1": 420, "day2": 380, "day3": 390 }

# Series without indexes
series = pd.Series(data)
print(series)

# Series with indexes
series = pd.Series(data, index=["day1", "day2"])
print(series);