# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
print("Dataset values")
print(dataset)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state= 150)
print()
print("X_train Dataset Description and values:")
print(stats.describe(X_train))
print(X_train)
print()
print("X_test Dataset Description and values:")
print(stats.describe(X_test))
print("X_test Array Size: " + str(X_test.size))
print(X_test)
print()
print("y_train Dataset Description and values:")
print(stats.describe(y_train))
print(y_train)
print()
print("y_test Dataset Description and values:")
print(stats.describe(y_test))
print(y_test)
print()
print("X_Train and y_train shape definition:")
print(X_train.shape)
print(y_train.shape)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# y = m x + b
# b is intercept parameter
# m is coefficient (slope)
inter = regressor.intercept_
coe = regressor.coef_
print()
print("Intercept parameter and coefficient (slope):")
print('Intercept (b) is : ', inter)
print('Coefficient (m) is : ', coe)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
print()
print("y_pred Dataset Description and values:")
print(stats.describe(y_pred))
print()
print("Comparing Predicted Values vs Actual for Test set results:")
df1 = pd.DataFrame({'Actual': y_test, 'Predict': y_pred})
print(df1)
print()
print("Comparing Predicted Values vs Actual + Variance for Test set results:")
df2 = pd.DataFrame({'Actual': y_test, 'Predict': y_pred, 'Variance': y_test - y_pred})
print(df2)

from sklearn.metrics import r2_score

Score = r2_score(y_test, y_pred) * 100
print()
print('Score is : ', Score)

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

print()
print('Mean Absolute Error : ', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error : ', mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error : ', np.sqrt(mean_squared_error(y_test, y_pred)))

# Visualising the Training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='green')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
