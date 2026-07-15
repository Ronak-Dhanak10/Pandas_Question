import pandas as pd

df = pd.read_csv("IRIS.csv")

result = df.groupby("species")["sepal_length"].mean()
result = df.groupby("species")["petal_width"].max()
result = df.groupby("species")["sepal_width"].std()
# •Averagesepal_length
# •Maximumpetal_width
# •Standard deviation of sepal_width


print(result)