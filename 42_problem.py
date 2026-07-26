# Read csv file and change heading with input names using Names=

import pandas as pd 
df = pd.read_csv("Titanic-Dataset.csv",names=
                 ["col1","col2","col3","col4","col5"])
print(df)
# Extra column heading name 
# Extra column give data as a NaN

