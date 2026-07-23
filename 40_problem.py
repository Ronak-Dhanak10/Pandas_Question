# Read csv file  and change header with using rows data

import pandas as pd 
df = pd.read_csv("IRIS.csv",header=1)
print(df)