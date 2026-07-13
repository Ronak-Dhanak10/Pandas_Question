import pandas as pd 
dic = {"name":['python','c','c++','java'],"Rank":[1,4,3,2]}
var = pd.Series(dic)
print(var)
# if you used mixed typr data than the series type is object 
