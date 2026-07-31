# Drop perticular column Nan value USing sebset=["clm name"]
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print(df)
print(df.dropna(subset=["Name"]))
