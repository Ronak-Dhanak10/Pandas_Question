# Read csv and check how much index in csv file
import pandas as pd 
df = pd.read_csv("IRIS.csv")
print(df)
print(df.index)