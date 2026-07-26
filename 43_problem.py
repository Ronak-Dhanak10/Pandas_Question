# Read csv file and remove heading or add indexing

import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv", header=None)
print(df)