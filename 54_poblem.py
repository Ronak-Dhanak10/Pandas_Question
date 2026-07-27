# fetch perticular value use-> iloc[]
import pandas as pd 
df = pd.read_csv("IRIS.csv")
print(df.iloc[0,2])