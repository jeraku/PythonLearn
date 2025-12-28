import pandas as pd
import numpy as np
import os as os

path =os.getcwd() + "/360digi/Day19/cars.csv"
print(path)
val = pd.read_csv(path)

# print(val)
print("-----------")
print(val.shape) #size of row and columns
print(type(val))

print((val.head(2)))
print("-----------")
print((val.tail(2)))
print("-----------")
print((val.info()))
print("-----------")
print((val.iloc(1)))
print("-----------")
# print((val.value_counts()))
print("-----------")
print(val.seller.value_counts())
print("-----------")
print(val.describe()) #works only for numerical values
print("-----------")
print((val.head(2)))

# print(val.)