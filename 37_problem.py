#  Read csv file and access perticular column using column name
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv",usecols=["Name"])
print(df)