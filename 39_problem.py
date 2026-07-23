# Read csv file and change index with column data 
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv", index_col="Name")
print(df)