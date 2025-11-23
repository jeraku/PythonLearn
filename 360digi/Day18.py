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
from array import *
arr = array("i", [12,12,34,5,66,6])

for x in arr:
    print(x)