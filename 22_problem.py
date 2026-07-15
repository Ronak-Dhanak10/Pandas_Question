import pandas as pd
df = pd.read_csv("IRIS.csv") 
pl = df[(df["petal_length"]> 4.5) & (df["species"]=="Iris-virginica")]
print(pl)
# .B •petal_length>4.5
# •species="Iris-virginica"