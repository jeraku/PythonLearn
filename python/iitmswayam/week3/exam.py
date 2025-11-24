import pandas as pd
import numpy as np
import os  as os

path = os.getcwd() + "\\python\\iitmswayam\\week3\\tips.csv"
print(path)
print(os.curdir)
cars_data= pd.read_csv(path)
print(cars_data.info())
print(max(cars_data["TotalBill"]))
print(min(cars_data["TotalBill"]))
print(max(cars_data["TotalBill"]) - min(cars_data["TotalBill"]))
print("=== NAN value count is ")
print(cars_data["Smoker"].isna().sum())
print("3rd quanrantile value(Q3) is ==> ")
print(cars_data["TotalBill"].quantile(0.75))


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
#  What is the command to convert the above dictionary into a dataframe named ‘df’ in pandas?
cd= pd.DataFrame(data)
print(pd.DataFrame(data))
print(cd.info())