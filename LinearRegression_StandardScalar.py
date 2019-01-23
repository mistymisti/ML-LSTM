
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm


#Importing the dataset
dataset = pd.read_csv('hou_all.csv',sep=',',names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV','CONST'])
dataset = dataset[['CONST','CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']]


#Splitting the dependent and independent variable
X_source = dataset.iloc[:, dataset.columns != 'MEDV' ] 
y_target = dataset.iloc[:, dataset.columns == 'MEDV' ]


#Splitting the dataset into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X_source, y_target, test_size = 0.3, random_state = 0)


model = sm.OLS(y_train,X_train)
result = model.fit()
print(result.summary())



#Training using Linear Regression
linearRegression = LinearRegression()
linearRegression.fit(X_train, y_train)


#Predicting the outcome using the trained model
Y_pred = linearRegression.predict(X_test)



#Comparing the original test values and predicted values
print('Root Mean Squared Error : %0.20f' % np.sqrt(mean_squared_error(y_test,Y_pred)))




