import pandas as pd
S = pd.Series([22,23,25,26], index = ["Adam","Sabrina","Ana","Charlie"])# Labeled is a named Index
print(S)

print(S["Adam"])
print(S.index)