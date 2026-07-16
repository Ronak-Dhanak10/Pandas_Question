import pandas as pd

df = pd.read_csv("IRIS.csv")

df['petal_ratio'] = df['petal_length'] / df['petal_width']

print(df)