# Read csv file and skip some rows using rows number
import pandas as pd 
df = pd.read_csv("IRIS.csv",skiprows=[1,3])
print(df)