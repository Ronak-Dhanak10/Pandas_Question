# Get perticular data 
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print(df.loc[[1,2,3],["Name","Age"]])