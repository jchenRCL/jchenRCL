# Code source: 
# https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py

import joblib # joblib can save models for later comparison
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings('ignore', category = FutureWarning)
warnings.filterwarnings('ignore', category = DeprecationWarning)
from sklearn.model_selection import train_test_split
import seaborn as sns
import re
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import scale
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import make_pipeline

# Load the diabetes dataset
data_X, data_y = train['weighted citation count'], train['scores citations-score']

X_train, X_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.4, random_state=0)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=0)

# RidgeCV implements ridge regression with built-in cross-validation of the alpha parameter. 
# The object works in the same way as GridSearchCV except that it defaults to Generalized Cross-Validation (GCV), an efficient form of leave-one-out cross-validation:

reg = linear_model.RidgeCV()

# Create linear regression object
#regr = linear_model.LinearRegression()

# Train the model using the training sets
reg.fit(X_train.values.reshape(-1, 1), y_train)

# Make predictions using the testing set
data_y_pred = reg.predict(X_test.values.reshape(-1, 1))

# The coefficients
print('Coefficients: \n', reg.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, data_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, data_y_pred))

# Plot outputs
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, data_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.savefig("Ridge_CV_regression.jpeg", dpi = 400)
plt.show()
