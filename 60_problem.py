# Drop all Nan value Rows Using->> inplace=True
# Replace all Nan value with perticular value ->> inplace=True
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print(df)
df.dropna(inplace=True)
df.fillna(15, inplace=True)