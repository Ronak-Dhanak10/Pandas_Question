# Finding Unique data in file
import pandas as pd
df = pd.read_csv("globalAirQuality.csv")
print(df.nunique())

