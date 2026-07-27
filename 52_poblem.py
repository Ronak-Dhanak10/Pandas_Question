# Change data in your csv file
import pandas as pd 
df = pd.read_csv("IRIS.csv")
df.loc[0,"Name"] = 'Python'
print(df)