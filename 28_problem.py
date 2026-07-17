import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

result = df.groupby("Pclass")["Survived"].mean()
print(result)