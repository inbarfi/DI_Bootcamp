# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 22:00:04 2021

@author: Inbar
"""

#w7_d1_class
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# lst = [2, 4, 6, 8, 13, 2020]
# numpy_arr = np.array(lst)
# 
# print(numpy_arr)
# print(numpy_arr[-2:])
# #print(numpy_arr.reshape((3,2)))
# lst_2d = [[3, 5, 7, -4, 1], [0, 5, 33, -750, 2]]
# numpy_arr_2d = np.array(lst_2d)
# print(numpy_arr_2d)
# print("mean is", np.mean(numpy_arr_2d, 0))
# #print(numpy_arr_2d.reshape(-1,2))
# print(numpy_arr_2d[:, 1]) #from all 
# =============================================================================

# =============================================================================
# #numpy 
# def my_array(arr):
#     #using np methods/attributions np.
#     return arr.min(), arr.std(), np.product(arr), np.dot(arr, arr), arr-4, np.mean(arr)
#     #return min(arr) #also works with regular Python functions
# 
# one_dim_array = np.array([1,2,3,4,5,6])
# print(my_array(one_dim_array))
# =============================================================================

# =============================================================================
# import pandas as pd
# #Iris database 
# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# 
# #print(df.head())
# #print(df.shape) #pandas shape starts with rows
# #print(df.head)
# #print(df.info())
# #print(df.describe())
# #print(df.species.unique())
# #print(df[df.species == 'setosa'])
# #print(df.sort_values('sepal_length', ascending=False))
# #print(df.groupby('species').apply(np.mean))
# # it returns a DataFrame of the grouped results. species has now become an
# # index in the DataFrame
# 
# #first 6 rows: 
# #print(df.iloc[:6])
# #print("--------")
# #print(df.loc[:6]) # loc - including 
# 
# #class exercise - print out the 50th row from the Iris dataframe
# #print(df.iloc[50])
# #Get the 50th to 60th row of the Iris DataFrame skipping every other row 
# #and return a new DataFrame of just the species, petal_length, and petal_width
# #skip_rows = [i for i in range (50,61,2)]
# #print(skip_rows)
# #new_df = pd.DataFrame(df, columns = ['species', 'petal_length', 'petal_width'], index = skip_rows)
# #print(new_df)
# 
# #Group the data by species and get the median and the sum of sepal_length for each group
# #n_df = df.groupby('species').apply(np.median)
# #print(n_df)
# #n_df = df.groupby('species').apply(np.sum)
# #print(n_df)
# =============================================================================

#Data Visualization
# Iris database 
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# ?
#colors = {'setosa':'red', 'versicolor':'green', 'virginica':'blue'}
#plt.plot(df.index, df["sepal_length"], "b--") 
#plt.show()
#​plt.scatter(df['sepal_length'], df['petal_length'], c = df.species.map(colors))
#plt.show()
#print(plt.scatter(df['sepal_length'], df['petal_length']))
#plt.xlabel('sepal_length (cm)')
#plt.ylabel('petal_length (cm)')
#plt.grid() 
#plt.show()
# =============================================================================
# setosa_df = df[df.species == 'setosa']
# versicolor_df = df[df.species == 'versicolor']
# virginica_df = df[df.species == 'virginica']
# 
# fig, ax = plt.subplots(1,3,figsize=(13, 5)) #creating 3 figures
# # starting from ax[] to refer to the figure number
# # ? what's the .petal_length...?
# ax[0].hist(setosa_df.petal_length, color='g', label = 'setosa')
# ax[1].hist(versicolor_df.petal_length, color='r', label = 'versicolor')
# ax[2].hist(virginica_df.petal_length, color='b', label = 'virginica')
# 
# ax[0].legend()
# ax[1].legend()
# ax[2].legend()
# ax[0].set_ylabel('Frequency')
# ax[1].set_ylabel('Frequency')
# ax[2].set_ylabel('Frequency')
# ax[0].set_xlabel('petal length (cm)')
# ax[1].set_xlabel('petal length (cm)')
# ax[2].set_xlabel('petal length (cm)')
# 
# plt.show()
# =============================================================================
# =============================================================================
# # Using NumPy, create an array of length 100 filled with random ints between 0 and 75
# # doesn't work - ?
# rand_arr = np.random.randint(low=0, high=75, size=(100,))
# print(​rand_arr)
# # Reshape that array to a 50 x 2 matrix
# ​rand_arr.reshape(50,2)
# # Make a scatter plot of the 1st column as the x axis and the second column as the y axis
# ​plt.scatter(rand_arr[:, 0], rand_arr[:, 1])
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show() 
# # make a histogram of each of the columns and make titles for each plot
# first_column = rand_arr[:, 0]
# second_column = rand_arr[:, 1]
# 
# fig, ax = plt.subplots(1,2,figsize=(13, 5))
# ​
# ax[0].hist(first_column, color='b', label = 'first_column')
# ax[1].hist(second_column, color='r', label = 'second_column')
# ​
# ax[0].legend()
# ax[1].legend()
# ​
# ax[0].set_ylabel('Frequency')
# ax[1].set_ylabel('Frequency')
# ​
# ax[0].set_xlabel('Random_number')
# ax[1].set_xlabel('Random_number')
# ​
# plt.show()
# ​
# =============================================================================
titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
titanic_df = df
#print(titanic_df.head())
print(titanic_df.Sex.unique())
#male_data = titanic_df[titanic_df.Sex == 'male']


# =============================================================================
# plt.figure(figsize= (10,5))
# titanic_df.Fare.plot(kind="hist", color = 'g')
# plt.xlabel('Fare')
# plt.title('Amount')
# plt.show()
# 
# titanic_df.Pclass.unique()
# 
# first_c = titanic_df[titanic_df.Pclass == 1].Survived.value_counts(normalize=True)
# second_c = titanic_df[titanic_df.Pclass == 2].Survived.value_counts(normalize=True)
# third_c = titanic_df[titanic_df.Pclass == 3].Survived.value_counts(normalize=True)
# 
# third_c
# 
# fig, ax = plt.subplots(1,3, figsize = (13,6))
# 
# ax[0].pie(first_c, labels = first_c.index.map({0: "Not Survived", 1: "Survived"}), autopct = '%1.1f%%',)
# ax[0].set_title('First_class')
# 
# ax[1].pie(second_c, labels = second_c.index.map({0: "Not Survived", 1: "Survived"}), autopct = '%1.1f%%',)
# ax[1].set_title('Second_class')
# 
# ax[2].pie(third_c, labels = third_c.index.map({0: "Not Survived", 1: "Survived"}), autopct = '%1.1f%%',)
# ax[2].set_title('Third_class')
# 
# plt.show()
# 
# =============================================================================

# =============================================================================
# Daily_digest
# x=np.arange(0,10) #Array of range 0 to 9
# y=x**3
# plt.plot(x,y)
# plt.title('Line Chart')
# plt.xlabel('X-Axis') 
# plt.ylabel('Y-Axis')
# plt.show()
# # Generation of 1 set of variables 
# x = np.arange(0,11)
# y = x**3
# 
# # Generation of 1 set of variables
# x2 = np.arange(0,11)
# y2 = (x**3)/2
# 
# # Printing all variables
# #print(x,y,x2,y2,sep="\n") # each value will be printed in another line.
# plt.plot(x,y,color='r',label='first data', linewidth=5) 
# plt.plot(x2,y2,color='y',linewidth=5,label='second data')
# plt.title('Multiline Chart')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
# 
# # Shows the legend in the best postion with respect to the graph
# plt.legend()
# =============================================================================

# =============================================================================
# x = ["India",'USA',"Japan",'Australia','Italy']
# y = [6,7,8,9,2]
# 
# # Printing the variables
# print(x)
# print(y)
# 
# plt.bar(x,y, label='Bars1', color ='r') # Function to plot
# plt.xlabel("Country")
# plt.ylabel("Inflation Rate%")
# plt.title("Bar Graph")
# plt.show()
# =============================================================================
# =============================================================================
# # Multiple bar charts
# # Generation of 1 set of variables 
# x = ["India",'USA',"Japan",'Australia','Italy']
# y = [6,7,8,9,5]
# 
# # Generation of 2 set of variables
# x2 = ["India",'USA',"Japan",'Australia','Italy']
# y2 = [5,1,3,4,2]
# #x and x2 are the same
# 
# # Printing all variables
# print(x,y,x2,y2,sep="\n")
# 
# # Functions to plot 
# plt.bar(x,y, label='Inflation', color ='y')
# plt.bar(x2,y2, label='Growth', color ='g')
# 
# # Functions to give x and y labels
# plt.xlabel("Country")
# plt.ylabel("Inflation & Growth Rate%")
# 
# plt.title("Multiple Bar Graph")
# plt.legend()
# plt.show()
# =============================================================================
# =============================================================================
# # Histogram
# # Generation of variable
# stock_prices = [32,67,43,56,45,43,42,46,48,53,73,55,54,56,43,55,54,20,33,65,62,51,79,31,27]
# 
# # Function to show the chart
# plt.figure(figsize = (5,5))
# plt.hist(stock_prices, bins = 4)
# =============================================================================
# =============================================================================
# #scatter plot
# # Generation of x and y variables
# x = [1,2,3,4,5,6,7,8]
# y = [5,2,4,2,1,4,5,2]
# 
# # Function to plot the graph
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Scatter Plot')
# =============================================================================














