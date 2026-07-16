import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

female = df[df['Sex'] == 'female']

print(female)