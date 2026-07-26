# Read csv file and fetch all columns name
import pandas as pd
df = pd.read_csv("IRIS.csv")
print(df)
print(df.columns)