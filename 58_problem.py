# Drop Nan row--> All row data is Nan using how="all" to drop row
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print(df)
print(df.dropna(how="any")) # remove full row if one value is null
print(df.dropna(how="all")) # remove row if all value is nill