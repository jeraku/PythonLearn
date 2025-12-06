"""Data visualisation 
Types of data 
Quantitative data (number or value is present)
    Numerical and mesurable 
Qualitative data (description and % values )
    Descriptive and categorical 

Map:
Heatmap

Correlation matrix chart

matplotlib
seaborn
"""

from matplotlib import markers
import pandas as pd # data manipulation -> Load clean and organise datasets
import numpy as np # numerical calculation -> Arrays and metrices
import matplotlib.pyplot as plt # for creating plots and charts.
import seaborn as sns # on top of matplotlib data visualisation
import os as os
# sns.set(style="darkgrid")   legacy command going forward use set_theme

print("--------")
print(os.getcwd())
path = os.path.abspath(__file__)
print(path)
path1= os.getcwd() + "\\python\\iitmswayam\\week4\\Toyota.csv"
print(path1)
df = pd.read_csv(path1, index_col=0, na_values= ["??", "????"])
df.dropna(inplace=True) #rmeove nan rows 
print(df.head(5))

print(df.info()) #summary of data frame

print(df["Doors"].unique()) #object prints unique values
# df["Doors"] = df["Doors"].replace({"three":3, "four": 4, "five": 5})
# print(df["Doors"].unique())
df["Doors"] = df["Doors"].replace({"three":3, "four": 4, "five": 5}, regex=True).astype(int)
print(df["Doors"].unique())
print(df.info())
print(df["MetColor"].unique())
print(df["Automatic"].unique())
df["MetColor"] = df["MetColor"].astype("str")
df["Automatic"] = df["Automatic"].astype("str")
print(df.info())
print(df.describe())


print("888888888888888888888888888888")




print("------------------------------------------")
print("seaboarn Visualisation -> trend estimation")
print("Regrssion scatter plot -> plot with regression line")
sns.regplot(x="Price", y= "Age", data = df)
plt.title("scatter plot with regression line")
plt.show()
sns.regplot(x="Price", y= "Age", data = df, fit_reg=False)
plt.title("scatter plot without regression line")
# plt.show()


print("---------- LMPLOT with HUE")
sns.lmplot(x="Age", y= "Price", data = df, hue="FuelType", fit_reg=True, palette="Set1")
plt.title("scatter plot without regression line")
# plt.show()

print("---------- count plot")
sns.countplot(x="FuelType", data = df)
plt.title("Fueltype count")
# plt.show()
sns.countplot(x="FuelType", data = df, hue = "Automatic")
plt.title("Fueltype count")
# plt.show()

print("=========histogram plot")
sns.histplot(df["Age"], kde=True) #kernel density extreme
# plt.show()
# 
sns.boxplot(y="Price", data =df)
# plt.show()


sns.boxplot(x="FuelType", y="Price", data =df)
# plt.show()

sns.boxplot(x="FuelType", y="Price", hue="Automatic", data =df, palette="Set2")
# plt.show()

print("--------------------------------------------")
print("combine box plot and histogram")

f,(ax_box, ax_hist) = plt.subplots(2,sharex=True, gridspec_kw={"height_ratios": (.15,.85)}, figsize=(8,6))
# (row, sharexaxis, 15%ofheight and 85% of histogram, figuresize)
sns.boxplot(x=df["Price"], ax=ax_box)
sns.histplot(x=df["Price"],kde=False, ax=ax_hist)
ax_box.set(xlabel="")
# plt.show()

print("-----------------HEATMAP")

print("Corelation visualition matrix")

plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap="coolwarm")
plt.show()


sns.pairplot(df, hue="FuelType")
plt.suptitle("testing pairplot", y=1.02)
plt.show()