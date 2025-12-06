"""
numpy 


"""

import numpy as np

x=[10,23,44,52,13] 
print(x*2)

y=np.array(x)
print(y)
print(y*2)

print(y>10, y[y>10])
print(y[2])

from numpy import  random 
x =random.randint(3,9)
print(x)

print("numpy array share memory ---- memory save")

a=np.arange(10)
print(a)
print(a[::2])

b= a[::2]
print(b)
print(np.shares_memory(a,b))
print(a,b)
print(type(a))

arr = np.array([[1213,2342,2344,2345,23476],[234,234,23242,454,324]])
print(arr)
print(arr[0,1])
print(arr[1,4])
print(arr[::2])
arr = np.array([1213,2342,2344,2345,23476])
print(arr[1:2:2])

print("masking array")
a= np.arange(10)
print("a value is ", a)
mask  = (a%2==0)
print(mask)
print(a[mask])
            
a=np.matrix('1,3; 3,5')
print(a)
a=np.matrix([[1,3], [3,5]])
print(a)
        

print("numpy broadcasting ")
a= np.arange(2,10,2)
print(a)
b= np.arange(1,10,2)
print(b)
print(a.shape, a, b.shape,b)

a= a[:,np.newaxis]
print(a)
print(a.shape)
print("------------------")
print(a)
print(b)
print(a+b)

print("===================================================")
print("DATA STRUCTURE")
print("Array/Vector")
from array import *
arr = array("i", [12,12,34,5,66,6])

for x in arr:
    print(x)

# print(help(array))

print("insert operation")
arr.insert(1, 60)
print(arr)

print("deletion")
arr.remove(66)
print(arr)

print("update")
arr[2] = 80
print(arr)

print("---------2D array")

T= [[12,4,56], [23,345,74], [24,34456,46]]

print(T[0])
print(T[1][2])

print("insert in 2d array")
print(T)
T.insert(1, [3123,576,234])
print(T)

print("matrix example")

from numpy import *
TransposeEx= array([["Mon",12,4,56], ["Tue", 23,345,74], ["wed", 24,34456,46]])
print(TransposeEx)
a= reshape(TransposeEx,(3,4))
print(a)
print("---accessing value in matrix")
print(a[2])
print(a[2][2])

print("Adding a data in matrix")
Tr = append(a, [["Thrus", 12,34,121]], 0) # (0 end = Row ) add by using the append at the end of 0 row
print(Tr)
Tr1 = insert(Tr,[4],[[1],[123],[1234],[1134]],1) # (1 end = column) column will be added to the matrix

print(Tr1)
print("=========")
Tr2= delete(Tr1, [2],0) #2nd row will be deleted
print(Tr2)

print("=========")
Tr2= delete(Tr1, [2,3],1) # entire 2nd colum will be deleted
print(Tr2)


print("============Other operations ==================")

z= np.diag(1+np.arange(4)) # diagonal arrange matxi 1-4 in sideways
print(np.arange(4))
print(z)
print(type(z))
z1= np.zeros(10)
print(z1)
z1[4] =112
print(z1)

z2 = np.random.random(30) # random vector of 30 values will be generated
print(z2)
print(z2.mean())

# reverse a vector
z4 = np.arange(30)
print(z4)
z4= z4[::-1]
print(z4)


import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

# Select the first row
print(df.iloc[0])

# Select the first two rows and first column
print(df.iloc[0:2, 0])


