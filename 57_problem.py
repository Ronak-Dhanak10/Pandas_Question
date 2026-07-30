# Drop Nan data with axis using dropna()
import pandas as pd
df = pd.read_csv("IRIS.csv")
print(df)
print(df.dropna())