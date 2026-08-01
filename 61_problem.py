# Drop perticular column Nan value USing ->> thresh = 3
# thresh stands for minimum number of non-NaN values required to keep a row (or column).

import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
print(df)
df1 = df.dropna(thresh=3)
print(df1)