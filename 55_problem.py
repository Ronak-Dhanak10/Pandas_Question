# Drop perticular data line using Drop() fnxn
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print("Drop Name column:\n",df.drop("Name",axis=1))
print(df)