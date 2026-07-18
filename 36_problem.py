# Read csv file and access Specific column using indexing
import pandas as pd 
df = pd.read_csv("IRIS.csv", usecols=[4])
print(df)