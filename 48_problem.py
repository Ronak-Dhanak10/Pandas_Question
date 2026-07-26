# fetch perticular rows using slicing
import pandas as pd 
df = pd.read_csv("IRIS.csv")
print(df[3:6])