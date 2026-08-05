# Fill the forward value on Nan place 
# Fill the Nan value with the forward value
import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print(df.fillna(method='ffill'))