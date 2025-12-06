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

""" categorizing of variable type in dataset
Categorical variable - group variable, data spitted based on the categories.
Numerical variable - Measurable quantity 

"""

# print(scatter plot ->>> shows individual data points on x and Y axis)  used to corelation between two vairables.


print("--- SCATTER PLOT")
print(plt.figure(figsize=(8,5)))
print(plt.scatter(df["Age"], df["Price"], color="red"))
plt.title("satter plot, Age vs price")
plt.xlabel("Age")
plt.ylabel("Price")
# plt.show()

print("--- Line chart")
age_price = df.groupby("Age")["Price"].mean().sort_index()
age_price.plot(kind="line", marker = "o")
plt.title("age by price")
plt.xlabel("age")
plt.ylabel("price")
# plt.show()

print("--------- BAR plot")
print("compare values across categories")

fuel_count = df["FuelType"].value_counts()
index=np.arange(len(fuel_count))
plt.bar(index, fuel_count.values, color=["red", "blue", "cyan"], edgecolor= "darkblue")

plt.xticks(index, fuel_count.index, rotation=90)
plt.show()

print("---- PIE chart")
fuel_count.plot(kind ="pie", autopct= "%1.1f%%",  startangle=90, figsize=(6,6) )
plt.show()

print("--------- Histogram > distribution of single numeric variable")

plt.figure(figsize=(8,5))
plt.hist(df["KM"], bins=5, color="red", edgecolor="white")
plt.show()

print("------------------------------------------")
print("seaboarn Visualisation -> trend estimation")
print("Regrssion scatter plot -> plot with regression line")
# sns.regplot(x="Price", y= "Age", data = df)