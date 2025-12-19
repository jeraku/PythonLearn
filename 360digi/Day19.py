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

