""" 
sorted
collection libary to handle the missing key in dictionary

lambda
map
print(list(map(lambda x: x*2, val)))

filter
# filter(function return true or false, iterable)
print(list(filter(lambda x: x<20, list(range(0,30)))))

reduce
print(reduce(lambda x, y : x*y, val))

"""
animals = ["dog", "cat", "bear" , "sheep", "elephant"]

print(sorted(animals))
print(animals)

print(sorted(animals, reverse=True))
print(sorted(animals, key=len, reverse=True))

# Augmented assignment
# list is mutable
l= [1,2,4]
print(id(l),l)
# id(l) -> location from the ram memory=
l *= 2
print(id(l),l) # data replace with in the same location

t=(1,2,4)
print(id(t),t)
t *=2
print(id(t),t)


# handling error in dictionary if the key is not present then how to handle.
dd= {"a":1, "b":2}
# print(dd["c"]) -> It will throw error, so to handle this error, we will go with the below option
import collections as cl
from re import S
defd = cl.defaultdict(lambda:"key not available")
defd["a"]=1
defd["b"]=3
print("the value of a is ", defd["a"])
print("the value of a is ", defd["c"]) #this will not throw error, lambda function will be invoked.

# lambda function ex
# x=10
b= lambda x : x*x
print(b)
print(b(10))

# map function ex
val= [1,2,4,5,5,6,7,7]
print(list(map(lambda x: x*2, val)))

print(list(map(str,val)))

# filter function ex
# filter(function return true or false, iterable)

val1= [1,2,5,6,7,8,83,3]

print(list(filter(lambda x:x%2, val1)))

print(list(filter(lambda x: x<20, list(range(0,30)))))

# reduce function ex
from functools import reduce

val = [1,34,5,23,6,7,7,823,2384,8]
print(reduce(lambda x, y : x*y, val))
# help(reduce)


# loop vs comprehension vs map
val1= [1,2,5,6,7,8,83,3]
sq1=[]

# for loop 
for i in val1:
    sq1.append(i**2)
    
# comprehension
sq2=[i**2 for i in val1]

sq3= list(map(lambda x: x**2,val1))

print(sq1)
print(sq2)
print(sq3)

