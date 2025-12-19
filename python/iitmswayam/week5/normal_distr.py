from http.client import ACCEPTED
from importlib.metadata import distribution
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.stats as sp

import pandas as pd
import os as os 

print(os.getcwd())


path= os.getcwd() + "\\python\\iitmswayam\\week5\\cars.csv"
cars_data = pd.read_csv(path)
print(cars_data.info())

cars =cars_data.copy()

# cars1 = cars[(cars.yearOfRegistration<=2018) &(cars.yearOfRegistration>=1950) 
#             & (cars.price>=100)
#             & (cars.price<=15000)
#             & (cars.powerPS>=500)
#              & (cars.powerPS<=10) ] 
print("222222222")
print(cars)


print("hypothesios testing")

""" one sample of mean 
car used over 6000 poound or not"""
sample_size= 1000
sample1= cars.sample(sample_size, random_state=0)
print(sample1)
print(sample1["price"].mean())
pos_mean=6000
statistics, pvalue = sp.ttest_1samp(sample1["price"], pos_mean)

print(statistics, pvalue)


n=len(cars["price"])

#Degree of freedom
df = n-1

print(n,df)

# signiificance level - alphave _Value 

alpha = 0.5
# critical vlaue from standard distribution
# cv = sp.ppf([alpha/2, 1- alpha/2])

# print(cv)


'''
T test = ttest_1samp
z Test = proportions_ztest
two sample test for mean  two group = ttest_ind
two sample test for proportion two group = proportions_ztest
p<alpha is ACCEPTED
also Test sttistics is between the crtical values ex: z=-1.23 is between critical values -1.96 to + 1.96

Cross group validation 
chi Square test on independence
vehicle type depend on fueltype

'''
