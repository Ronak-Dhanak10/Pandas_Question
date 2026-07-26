# convert index into Numpy array

import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv")
print(df.to_numpy())