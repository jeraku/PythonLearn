from email.utils import decode_rfc2231
import pandas as pd
import numpy as np
import os as os

path =os.getcwd() + "/360digi/Day19/"
print(path)
# pd.read_csv()
x1= [1,2,3,4,6,7]
x2=[10,11,12,13,53,56]
x3= list(range(6))
print(x3)
X = pd.DataFrame(columns= ["x1","x2","x3"])
print("-----------")
print(X)
X["x1"] = x1
X["x2"] = x2
X["x3"] = x3
print("-----------")
print(X)

# shallow copy vs deep copy.
# deep copy = original data will not changed  deep =True
# shallow copy = changes within the original data
print("-----------")
dff =X.copy(deep=False)
print(dff)
print("-----------")
dff1 =X.copy(deep=True)
print(dff)


# convert list to pandas series format
print(x1)
print(type(x1))
X["x1"] = pd.Series(x1)
X["x2"] = pd.Series(x2)
X["x3"] = pd.Series(x3)
print(X)
print(type(X))
print(X.x1)
print(X[["x1","x2"]])

print(X.columns)
print(X.iloc[0:3,1])
print("-----------")
# index location
print(X.iloc[1:2,1:2])
print("-----------")
# location

print(X.loc[0:2, ["x2", "x2"]]) #column name to be definded in location
print("-----------")
df1 = pd.DataFrame({"a1": [2,4,5,7], "a2": [7,5,4,3]})
df2 = pd.DataFrame({"a1": [2,4,5,7], "a3": [71,51,14,13]})
print(df1)
print(df2)
print("-----------")
dfm = pd.merge(df1,df2) # same filed like a1 is required to do merge
print(dfm)
dfm = pd.merge(df1,df2,on="a1")

print("-----------JOIN ==========")

df1 = pd.DataFrame({"a1": [2,4,5,7], "a2": [7,5,4,3],}, index=[2000,2002,2004,2005])
df2 = pd.DataFrame({"a4": [2,4,5,87], "a3": [71,51,14,13]},index=[2200,22302,2004,2005])

print(df1)

joined = df2.join(df1)
print(joined)


print("------Replace index name------")
df1 = pd.DataFrame({"a1": [2,4,5,7], "a2": [7,5,4,3],})
df2 = pd.DataFrame({"a4": [2,4,5,87], "a3": [71,51,14,13]})
print(df1)
df1.set_index("a1", inplace=True) # Assing index names as column name > we are assinging the index name as our own vlaue
print(df1)

print("-----------")
print(df2)
df2 = df2.rename(columns = {"a4": "a5"})
print(df2)

print("------concatenation-----")
concate= pd.concat([df2,df1])
print(concate)

print("=======")
print(df2)
print(df2["a5"] >3)
print("=======")
df2["a6"]=["one", "two", "three", "foure"]
print(df2)
print("=======")
df2.iat[1,2]="Six"
print(df2)
print("=======")
print(df2.info())

df2.a5[2], df2.a3[1]=None,None
print(df2)

print("=======")
print(df2.isnull())
print("=======")
print(df2.isna())
print("=======")
print(df2.isna().sum())
df3=df2
print("=======")
print(df3.dropna(inplace=False))
print("=======")
print(df3)
print("=======")
print(df3.dropna(inplace=True))
print("=======")
print(df3)


print("-----------")

# imputation = missing value to be replaced by some logical value