import pandas as pd
df = pd.read_csv("IRIS.csv")
print(df.head(10))# first 10 rows
print(df.shape) #no. of rows and columns
print(df.info()) # Give info of Data like entries column rows and Datatype