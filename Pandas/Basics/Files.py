# If your data sets are stored in a file, Pandas can load them into a DataFrame.
import pandas as pd

# This will return system's maximum rows defined in Pandas option settings.
print(pd.options.display.max_rows)

# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows)

''' Load the CSV into a DataFrame '''
df = pd.read_csv('/home/aniket/Desktop/Python/Pandas/data.csv')

# NOTE: to_string() will return entire DataFrame

''' Load the JSON file into a DataFrame '''
df = pd.read_json('/home/aniket/Desktop/Python/Pandas/data.json')

# NOTE: JSONs == Python Dictionaries
# NOTE: If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly