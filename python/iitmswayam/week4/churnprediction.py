"""
joining 3 different data
merge operation
"""

import pandas as pd
import numpy as np
import os as os

path = os.getcwd() + "\\python\\iitmswayam\\week4\\week4data\\demoDetails.csv"
path1 = os.getcwd() + "\\python\\iitmswayam\\week4\\week4data\\acDetails.txt"
path2 = os.getcwd() + "\\python\\iitmswayam\\week4\\week4data\\serviceDetails.csv"
demoDetails = pd.read_csv(path, index_col=0)
acDetails = pd.read_csv(path1, sep="\t")
serviceDetails = pd.read_csv(path2, index_col=0)

print(len(demoDetails))
print(len(np.unique(demoDetails["customerID"])))

print(len(acDetails))
print(len(np.unique(acDetails["customerID"])))
print(len(serviceDetails))
print(len(np.unique(serviceDetails["customerID"])))

print(demoDetails.duplicated(subset=['customerID'], keep=False))
print(demoDetails[demoDetails.duplicated(subset=['customerID'], keep=False)])
print(acDetails[acDetails.duplicated(subset=['customerID'], keep=False)])
print(serviceDetails[serviceDetails.duplicated(subset=['customerID'], keep=False)])

demoDetails = demoDetails.drop_duplicates()
print(demoDetails)

acDetails.customerID.equals(demoDetails.customerID)
serviceDetails.customerID.equals(demoDetails.customerID)
acDetails.customerID.equals(serviceDetails.customerID)

churn = pd.merge(demoDetails, acDetails , on = "customerID")
churn.columns

print(churn)
churn = pd.merge(churn, serviceDetails , on = "customerID")
churn.columns
churn1 = churn.copy()

print("Data Exploration")
print(churn.info())

print("================Data 2 =================")
# get unique values and counts using pandas
print(churn1["tenure"].value_counts()) #unique values + counts
print(churn1["SeniorCitizen"].unique()) # unique values only


categorical_data = churn.select_dtypes(include = ["object"]).copy() #columns that are stored as object tpye in pandas
# above line filters the object type data and create a copy in another variable
print(categorical_data.columns)
categorical_data = categorical_data.drop(["tenure", "customerID"], axis =1) #axis=1 refers to columns for deletion
print(categorical_data)

frequencies = categorical_data.apply(lambda x: x.value_counts()).T.stack()
print(frequencies)

print(churn1.describe()) #returns summary value

churn1["tenure"] = churn1.tenure.replace("Four", 4)
churn1["tenure"] = churn1.tenure.replace("One", 4)
churn1["tenure"] = churn1.tenure.astype("int")

print(churn1["tenure"].info())

print("============================")
print(pd.crosstab(index=churn1["Dependents"], columns="labelname"))

churn1["Dependents"] = churn1["Dependents"].replace("1@#", 'No')
print(pd.crosstab(index=churn1["Dependents"], columns="labelname"))

print("--------logical validation formatting issue-----------")
print(churn1["customerID"])
# get customer id whose length is more than 10
# first length check
ref_data= [i for i, value in enumerate(churn1["customerID"]) if len(value)!=10]
print(ref_data)

#reg ex validation for pattern
import re
pattern_val= '^[0-9]{4,4}-[A-Z]{5,5}'
p=re.compile(pattern_val)
type(p)
ref_data = [i for i,v in enumerate(churn1["customerID"]) if p.match(v)==None]
print(ref_data)

fp2= re.compile('^[0-9]{4,4}/[A-Z]{5,5}')
fp1= re.compile('^[A-Z]{5,5}-[0-9]{4,4}')

for i in ref_data:
    false_str = str(churn1.customerID[i])
    if fp1.match(false_str):
        str_split = false_str.split("-")
        churn1["customerID"][i] = str_split[1] + "-" + str_split[0]
    elif fp2.match(false_str):
        churn1["customerID"][i] = false_str.replace("/", "-")


y=churn1[(churn1.InternetService=="No")]
print(y)

z=y.iloc[:,13:20]

print(z)

# changing the value of internet services to Yes
for i, row in z.iterrows():
    yes_cnt= row.str.count("yes").sum()
    if(yes_cnt>=2):
        z.loc[i].InternetService="yes"
    else:
        z.loc[i,:] = "no internet service"
print(z)

print("-----OUTLIER detection")

import matplotlib.pyplot as plt
import seaborn as sns

print(churn1.tenure.describe())
sns.boxplot(y=churn1["tenure"])
# plt.show()

churn1["tenure"]= np.where(churn1["tenure"]>=500, churn1["tenure"].median(), churn1["tenure"])

sns.boxplot(y=churn1["tenure"])
# plt.show()

print(churn1["tenure"].describe())

print(churn1.isnull().sum())

""" If input data contains numerical value -> then we can insert mean/Median as input.

for categorical data -> we need to use the mode value. which the no of occurence is more.

 """

print(churn1["TotalCharges"].mean())

sns.boxplot(x=churn1["TotalCharges"], y=churn1["Churn"])
# plt.show()

print(churn1["Churn"])


churn1["TotalCharges"] = churn1.groupby("Churn")["TotalCharges"].transform(lambda x: x.fillna(x.mean()))
print(churn1["TotalCharges"].isnull().sum())

print(churn1["MonthlyCharges"].mean())
sns.boxplot(x=churn1["MonthlyCharges"], y=churn1["Churn"])
# plt.show()
churn1["MonthlyCharges"] = churn1.groupby("Churn")["MonthlyCharges"].transform(lambda x:x.fillna(x.mean()))
print(churn1["MonthlyCharges"].isnull().sum())

print("---SAMPLING---------")

import random
p1= list(range(1,20))
print(p1)
val = random.sample(population=p1, k = 10)
print(val)
p2= list(range(1,30))
print(p2)
val = random.choices(population=p2, k = 10)
print(val)