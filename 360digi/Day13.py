"""
ITERATORS
TRAVERse through all the values within python, its an object or variable
It implements the iterator protocol
iterator methods.
__iter__()
__next__()

size is reduced a lot in MB size when it comes to iterator

GENERATOR
yield (instead of using return, we need to use yield)
generator object will be pulled as a iterator object
MAIN AIM  is for LESS  MEMORY
"""

names = ["jegan", "raj", "kumar"]
print(names) #Iterables 

new_list = names.__iter__() #converting to iterator
print(new_list) # this isa iterator object

print("====general way============")
for obj in new_list:
    print(obj)

print("========== Another way of converting into iterator ===============")

new_list = iter(names)
print(new_list)
print(type(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
# print(next(new_list)) stop iteration error will be thrown



print("-------------")

names = [i for i in range(1,2000000)]

# print(names)
new_list = iter(names)
print(new_list)
print(next(new_list))

import sys
print(f"size of variable {sys.getsizeof(names)} bytes")
print(f"size of variable {sys.getsizeof(new_list)} bytes")

print("------------------")

iterable_value ="Machine learning"
iterator = iter(iterable_value)

while True:
    try: 
        print(next(iterator))
    except StopIteration as e:
        print(f"stop iteration errror {e}") 
        break 

print("=========================GENERATOR================= ")
# special type of function, it will give you iteration of values 
print("general way")
def sequence(n):
    x=[]
    for i in range(n):
        x.append(i)
    return x

alist = sequence(300000)
print(type(alist))

print(">>> generator way")
def sequence(n):
    for i in range(n):
        yield i
# print(sequence(30))
blist = sequence(3000000000)
print(type(blist))
# generator object will be pulled as a iterator object
print(next(blist))
print(next(blist))
print(next(blist))
print(f"blist {sys.getsizeof(blist)} in bytes")
print(f"alist {sys.getsizeof(alist)} in bytes")


def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b = b , a+b

# creating a generator object using yield function
x= fib(100)
print(x)

# Iterating over the generator using next option
while True:
    try:
        print(next(x), end =" ")
    except StopIteration:
        print("stop iteration error ")
        break