import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
avg_age = df.groupby("Pclass")["Age"].mean()
print(avg_age)