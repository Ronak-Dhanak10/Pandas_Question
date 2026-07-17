import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
avg_fare = df.groupby("Pclass")["Fare"].mean()
print(avg_fare)