# ValueError: Columns must be same length as key

import pandas as pd

df1 = pd.DataFrame({
    'column1': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'column2': [29, 30, 31, 32]
})

df2 = pd.DataFrame({
    'column1': [100, 200, 300]
})

df1[['column3', 'column4', 'column5']] = df2['column1']

print(df1)