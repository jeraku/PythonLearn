"""
Built in module
refer the Day16 folder for more ref
# differnt way of importing module 
# import math
# from math import cos
# import math.cos 
# import math as m
# import *
# import math
# from math import *

all() method in dictionaries  return true or False, if all valus are true then True else False

Regular expression

Refer Day16 folder as well
"""
# import sys
# print(sys.path)


def cal_area_trianage(l,h):
    return 1/2 * l * h
def cal_area_sqr(l):
    return l * l
def cal_area_rec(l,b):
    return l * b
def cal_area_cir(r):
    return 3.14 * r * r

# differnt way of importing module 
# import math
# from math import cos
# import math.cos 
# import math as m

s = {0:"True", 1: "False"}
print(s)
print(all(s))

s = {0:"True", 1: "True"}
print(s)
print("eventhough values is True but 0 key is False so output is ",all(s))

s = {1:"True", 2: "True"}
print(s)
print(all(s))

print("===================Regular expression =============")
"""
\d - digit 

"""
import re
txt = "Hi This is jegan Raj Kumar and aga ie 25"
x =re.search("^Hi.*egan", txt) #respond match with result
print(x)

x1=re.findall("egan",txt)
print(x1)

x2 = re.findall(r'\d{1,3}', txt)
print(x2)

x3 = re.split("\s", txt) #split by space and return in list
print(x3)

# *-> zero or more occurences spaces will also be selected
# + -> 1 or more occurences 
x4 = re.split("\d+", txt) #
print(x4)
# x5 = re.split("\d*", txt) #
# print(x5)

allname = "my name is jegan , what is your name"
for i in re.finditer("name", allname):
    loc = i.span()  # index locaiton will be printed
    print(loc)

print(allname[32])