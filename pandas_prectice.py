import pandas as pd

# myDataSet = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myVar = pd.DataFrame(myDataSet);

# print(myVar);

''' This will return the version of pandas installed in your system '''
# print(pd.__version__)

''' Series: are like columns in a table in Pandas, it is a one dimensional array holding data of any type. '''
numArr = { "day1": 420, "day2": 380, "day3": 390 }
myVar = pd.Series(numArr, index=["day1", "day2"])
print(myVar);