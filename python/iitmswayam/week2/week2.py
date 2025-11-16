""" 
list
tuple
set
dict
range
str(a Sequence)
array



Mutable  - > list, set, dict
immutable -> tuple, str, range 

numpy array type is ndarray

"""


import numpy as np

print(np.__version__)

my_list= [2,3,45,5,345,6,345,734,7,3452,8,8]
print(f"My list values are  {my_list}")
nparrays = np.array(my_list)
print("numpy array list is ", nparrays)
print(type(nparrays))

print(nparrays[0])
nparrays[0]=20
print(nparrays)
print("22222222slicing ----")
b= nparrays[:3]
print(b)
# numpy creates view slicing hcnaged the original array list

print("------------Multi dimentional array --------------")
nested_list = [[1,2,3],[4,5,6]]
multi_array = np.array(nested_list)
print(multi_array)

print(multi_array[1,2])

print(type(multi_array))
print("number of dimension ", (multi_array.ndim))
print("share",multi_array.shape) # rows & column
print("size", multi_array.size)
print("data type", multi_array.dtype)

np1= np.zeros(3)
print(np1)
print("==========")
np2= np.zeros((3,3))
print(np2)
print("11111111111")
np1= np.ones(3)
print(np1)
np2= np.ones((3,4))
print(np2)
print("-----------")
print("speed value is displayed")
print(np.empty(2))

np1 = np.empty(2)
print(np1)

print("111111111111")
print("this command prints the range values in array order")
range_arr= np.arange(4)
print(range_arr)

range_arr= np.arange(2,20,2)
print(range_arr)
print("============")
print(np.linspace(0,10,num=5))

print("---------")
ones_1= np.ones(2)
print(ones_1)
ones_1= np.ones(4, dtype=np.int32)
print(ones_1)

print("sorting arrays")
ones_1=np.array([3,4,7,8,5,3,4,1])
print(np.sort(ones_1))

print("join arrays using concatenate")
x=np.array([[1,3],[4,6]])
y=np.array([[7,8]])
z= np.concatenate((x,y), axis = 0)
print(z)

print("reshape an array")
print("turn 1D array with matrix(3*4) of 12 elements")
arr= np.arange(12)
reshape_arr = arr.reshape((3,4))
print(reshape_arr)
row= reshape_arr[1]
col= reshape_arr[:,-1]
print(row)
print(col)


print("elemet wise math operation > element wise computation")
data_1= np.array([1,2])
data_2= np.array([3,4])
data_3= data_1 + data_2
print(data_3)
data_4= data_1 - data_2
print(data_4)
print("data Multiplication ", data_1 * data_2)
print("data division ", data_2 / data_1)
print("data sum of elements ", data_2.sum())
data_val = np.concatenate((data_1, data_2), axis=0)
print("data concatenate", data_val )
data_2= np.array([[1,2],[5,2]])
print("if axis=0 then column wise additopn will be printed")
print("data sum by axis for 2D array y column wise", data_2.sum(axis=0 )) 


print("if axis=1 then row wise additopn will be printed")
print("data sum by axis for 2D array by row wise", data_2.sum(axis=1 )) 
print("2222222222222222222-----------Broadcasting")
print(data_1)
print("reshaping the value in data1", data_1*5)

print("array operations in numpy")
data_1= np.array([2,3,5,6,6,7,8,81,68,1,23,723])
print(data_1.max())
print(data_1.min())
print(data_1.sum())

data_2= np.array([[2.4,3.5,5.6,6.7],[6.7,7.2,8.4,81.6]])
print(data_2.max())
print(data_2.min())
print(data_2.sum())
print(data_2.min(axis=0)) # column wise value
print(data_2.max(axis=1)) # row value 

data_1= np.array([2,3,5,6,6,7,8,81,68,1,23,723])
unique_value = np.unique(data_1)
print(unique_value)

print("flattening 2D array to 1D array")
data_1 = np.array([[1,3],[4,7]])
print(data_1.flatten())
print("Transpose of an array")
arr = np.array([[1,3],[4,7]])
print(arr)
print(arr.T)
print(arr.transpose())


print("statiscal summary")
dp = np.array([1,2,4,5,6,8,9,9,4,4,6,82])

print("mean values is ", np.mean(dp)) # Average value
print("median values is ", np.median(dp)) # middle numbre in an array
print("standard deviation ",np.std(dp) ) # square root of the variance


print("========================================")
print("Handing missing data")
data = np.array([2,4,6,np.nan,8,np.nan,10])
print("missing data in np", np.nanmean(data))

data = np.array([10,20,30,np.nan,50,np.nan,50])
mean_val = np.nanmean(data)
std_val= np.nanstd(data)
standardized= (data - mean_val ) / std_val
print("standardized value is ", standardized)
