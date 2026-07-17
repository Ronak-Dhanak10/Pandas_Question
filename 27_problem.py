import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
fare = df.query('Fare > 30')
print(fare)