""" 
local variable
global variable 
recursive function
List comprehension
newlist = [i for i in range(0,12) if i%2==1]

Dictionary comprehension
ditcs_k = {k*2:v*2 for k,v in dicts.items()}

Zip and unzip using Set 
mappes = zip(name,age, mark)
# unzipping example
nms, ags, mrk = zip(*mappes)

tuple  packing and unpacking 

"""

age =20 
def local():
    age =30 
    name="jegan"
    print(f"local variable is {age}")
    print("name is %s and age is %i" % (name, age))

local()
print(f"global variable is {age}")

#defining global variable inside the function
x=5
def func():
    global x
    x=10
    print("x value inside function is ", x)

func()
print("x value of global is ", x)

# without Recursion function 
def fact(n):
    if n<0:
        print("input the positive number")
    elif n==0:
        print(f"factorial of {n}! is 1") 
    else:
        fact=1
        for i in range(1, n+1):
            fact = fact*i
        print(f"factorial of {n}! is {fact}") 

fact(10)


#Recursion function

def fact(n):
    if n<0:
        print("enter positive number")
    elif n==0:
        return 1
    elif n==1:
        return 1    
    else:
        return (n*fact(n-1))

ret = fact(5)

print(f"fact val is {ret}")

print("-------------------List comprehension -----------------------------------")
# List comprehension 
# unicode = internation standard 
symbols = "£$^%%$&$"
code = []
for symbol in symbols:
    print(symbol , end = "")
    code.append(ord(symbol))
print("\r")
print(code)

# Alternate way - List comprehension
symbols = "£$^%%$&$"
code = [ord(symbol) for symbol in symbols]
print(code)

newlist = [i for i in range(0,12) if i%2==1]
print(newlist)

print("--------------------------")

print("-------------------Dictionary comprehension -----------------------------------")
#dictionary comprehension

n= range(10)
print(n)
dicts={}
for i in n:
    if i%2==0:
        dicts[i] = i**2
print(dicts)

print("dictionary comprehension 1: ")
n= range(10)
print(n)
dicts = {k:k**2 for k in n if k%2==0 }
print(dicts)


print("dictionary comprehension 2: ")

dicts = {"a":1, "b":2,"c":4}

ditcs_k = {k*2:v*2 for k,v in dicts.items()}
print(ditcs_k)

print("-------------------Zip and unzip with Set -----------------------------------")
# Zip and unzip

name = ["jegan", "raj", "kumar"]
age = [20,40,50]
mark = [300,500,402]
mappes = zip(name,age, mark)
print(mappes)
mappes = set(mappes)
print(mappes)

# unzipping example
nms, ags, mrk = zip(*mappes)

print(nms)
print(ags)

