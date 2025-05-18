#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    val=[0,0]
    for i in range(0,len(a)):
        if(a[i]>b[i]):
            val[0]=val[0]+1
        elif(a[i]<b[i]):
            val[1]=val[1]+1
    return val
    
    
a=[1,2,3,2,4]
b=[3,2,1,5,3]
compareTriplets(a,b)