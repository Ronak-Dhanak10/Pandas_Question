import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")

print(df.iloc[:,[1,3,4,5,9]])