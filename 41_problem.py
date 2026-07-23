# Read csv file and change heading with input names using Names=

import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv", names=["col","col2","col3"])
print(df)