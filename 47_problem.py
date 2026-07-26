# if you want to fetch some data in csv file Use--> describe() fnxn this fnxn give the data like : (count, mean, std, min, 25%, 50%, 75%, max)
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print(df.describe())