'''funciton is a block of reusable code 
    designed to perform a reusable task

'''
from pandas import value_counts


def add(num1: int, num2: int) -> int: 
    return num1+ num2
print(add(10,20))

print("positional arguments")
def add(*args) -> int:
    a,b,c,d = args
    print(a+b)
    return args
print(add(10,20,30,40))

print("Keyword arguments")
def add(**kwargs) -> int:
    return kwargs
print(add(a=10,b=20,c=30,d=40))

print("Keyword & positional arguments")
def add(*args,**kwargs) -> int:
    print(args)
    print(kwargs)
    return args, kwargs
print(add(100,2000, a=10,b=20,c=30,d=40))

print("loops" )

def add(*args):
    sum=0
    x=100
    for val in args:
        sum+=val
    return sum,x

total= add(10,30,405)
print(total)

x=10
# lamda x : x * x