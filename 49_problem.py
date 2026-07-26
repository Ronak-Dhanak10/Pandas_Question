# convert index into array
import pandas as pd
df = pd.read_csv("IRIS.csv")
print(df.index.array)