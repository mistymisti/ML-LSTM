
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


#Importing the dataset
dataset = pd.read_csv('hou_all.csv',sep=',',names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV','CONST'])
dataset = dataset[['CONST','CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']]

#Splitting the dependent and independent variable
#The variable to be predicted is MEDV(PRICE)
X_source = dataset.iloc[:, dataset.columns != 'MEDV' ]   #Independent Variable
y_target = dataset.iloc[:, dataset.columns == 'MEDV' ]   #Dependent Variable

#Splitting the dataset into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X_source, y_target, test_size = 0.3, random_state = 0)

#Training using Linear Regression
linearRegression = LinearRegression()
linearRegression.fit(X_train, y_train)

#Predicting the outcome using the trained model
Y_pred = linearRegression.predict(X_test)



#Comparing the original test values and predicted values
print('Root Mean Squared Error : %0.20f' % np.sqrt(mean_squared_error(y_test,Y_pred)))


