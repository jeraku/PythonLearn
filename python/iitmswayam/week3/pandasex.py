"""
dataframe 
    > two dimensional size mutable
    > labelled axes - 
 
import os  as os >> os to change the working directory
import pandas as pd >> pandas library to work with data frames
import numpy as np >> numpy library to perform numeric operations

os.chdir("c:/jegan") > to set working directory
    
    
"""
import os  as os
import pandas as pd
import numpy as np
print(os.curdir)
print(os.getcwd())
path = os.getcwd() + "\\python\\iitmswayam\\week3\\cars.csv"
print(path)
print(os.curdir)
cars_data= pd.read_csv(path)
# cars_data= pd.read_csv(path, "index_col=0") first column is the index column
print(cars_data.keys())
"""
two ways of Copy of original data  

shallow copy :> create only new variable refers the orignal object. if the value changes in main one then it will replace in the copied ones as well
    >  samp = cars_data.copy(deep=False)
    >  samp = cars_data
Deep copy :> copied into another new object. Modification will be reflected only in new object.
    > samp = cars_data.copy(deep=True)    
"""
print("------------1111111111")
# To get the index from row labels of the data frame 
print(cars_data.index)
print(cars_data.index)
print(cars_data.columns)
print(cars_data.size)
print(cars_data.shape) # 428 rows and 15 columns
print(cars_data.memory_usage()) # memory usage in bytes
print(cars_data.ndim) #number of axis /array dimensions rows - 1 and column- 2 so output will be 2

print("indexing and selecting data ")
print(cars_data.head(4)) # return first 4 rows, default value is 5 rows
print(cars_data.at[3, "Model"]) #at provides label-based scalar lookup
print(cars_data.iat[3,6])
print(cars_data.tail(4)) # return last 4 rows, default value is 5 rows
print(cars_data.loc[:,"Type"]) # fetch all the values from the row Type
print(cars_data.loc[1:4,"Type"]) # fetch the values from the row Type


print("==================================")
"""
DataType 
    Numeric - int, float
            python int pandas int64 Numeric character
            python float pandas float64 numeric with decimal
            64 in pandas is store the memory allocation is 64 bits, it allows computers to orgainise and efficiency

    character - string
        > category (variables taken on a limited, fixed number of possible value) and Object (for strings the length is not fixed)
        
    dataframe.dtypes
    """
print(cars_data.dtypes) # returns the data type of each column
print(cars_data.dtypes.value_counts()) 
print("-------categorical datatpye")
print(cars_data.select_dtypes(include=[object])) #Object values alone printed check info() results

print(cars_data.info()) 
print(np.unique(cars_data["Make"]))

print(">>>> cleaning data using PANDAS====================================")
print("Before")
print(cars_data.info())
cars_data= pd.read_csv(path, index_col=0,na_values=["??","????"])
print("After")
print(cars_data.info())

# convert a datatype into an object
cars_data["Horsepower"] = cars_data["Horsepower"].astype("object")
print(cars_data["Horsepower"].nbytes) #to check the size of the column values
print(cars_data["Horsepower"].astype("category").nbytes) #size will get reduced.

print(np.unique(cars_data["Horsepower"]))
pd.set_option('future.no_silent_downcasting', True)
cars_data["Horsepower"] = cars_data["Horsepower"].replace(500, 501)
print(np.unique(cars_data["Horsepower"]))

#To check the missing values in columns
print(cars_data.isnull().sum())

