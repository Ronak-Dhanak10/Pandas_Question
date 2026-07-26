# Read csv file and change perticular column data type 

import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv",dtype={"Age":float})
print(df)