import find_area as f
area = f.cal_area_cir(10)
print(area)

""" importing the module from different location of files """

import sys
import os 
# system expects the directory path to fetch the other modules.

val = os.path.abspath(".\\360digi")
sys.path.append(val)
print(sys.path)

import Day16 as f1 
a1 = f1.cal_area_cir(10)
print(a1)

