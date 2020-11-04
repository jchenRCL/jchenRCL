# This script shows how to use the trained polynomial model to predict single value which we need

# libraries:

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
import pickle
from sklearn.preprocessing import PolynomialFeatures 

tr_features = global_data['norm_cp']
tr_labels = global_data['scores citations-score']

# sklearn train_test_split

X_train, X_test, y_train, y_test = train_test_split(tr_features, tr_labels, test_size=0.4, random_state=0)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=0)


# fit the linear regression model with Polynomial features

from sklearn.linear_model import LinearRegression

# fit multiple polynomial features
degrees = [1, 2, 3, 4, 5, 6, 7]

# initialise y_train_pred and y_test_pred matrices to store the train and test predictions
# each row is a data point, each column a prediction using a polynomial of some degree
y_train_pred = np.zeros((len(X_train), len(degrees)))
y_val_pred = np.zeros((len(X_val), len(degrees)))
y_test_pred = np.zeros((len(X_test), len(degrees)))

for i, degree in enumerate(degrees):
    
    # make pipeline: create features, then feed them to linear_reg model
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train.values.reshape(-1, 1), y_train.values)
    
    # predict on val and train data
    # store the predictions of each degree in the corresponding column
    y_train_pred[:, i] = model.predict(X_train.values.reshape(-1, 1))
    y_val_pred[:, i] = model.predict(X_val.values.reshape(-1, 1))
    y_test_pred[:, i] = model.predict(X_test.values.reshape(-1, 1))
    
# visualise train and test predictions
# note that the y axis is on a log scale

plt.figure(figsize=(16, 8))

# train data
plt.subplot(121)
plt.scatter(X_train.values.reshape(-1, 1), y_train.values)
plt.yscale('log')
plt.title("Train data")
for i, degree in enumerate(degrees):    
    plt.scatter(X_train.values, y_train_pred[:, i], s=15, label=str(degree))
    plt.legend(loc='upper left')
    
# validation data
plt.subplot(122)
plt.scatter(X_val.values, y_val.values)
plt.yscale('log')
plt.title("Validation data")
for i, degree in enumerate(degrees):    
    plt.scatter(X_val.values, y_val_pred[:, i], label=str(degree))
    plt.legend(loc='upper left')
    
#plt.savefig("Polynomial_regression_norm_cp_gloal_no_log_scale.jpeg", dmp = 400)
plt.show()

import sklearn
# compare r2 for train, validation, and test sets (for all polynomial fits)
print("R-squared values: \n")

for i, degree in enumerate(degrees):
    train_r2 = round(sklearn.metrics.r2_score(y_train.values, y_train_pred[:, i]), 2)
    val_r2 = round(sklearn.metrics.r2_score(y_val.values, y_val_pred[:, i]), 2)
    test_r2 = round(sklearn.metrics.r2_score(y_test.values, y_test_pred[:, i]), 2)
    print("Polynomial degree {0}: train score={1}, val score={2}, test score={3}".format(degree, 
                                                                         train_r2,
                                                                         val_r2,                
                                                                         test_r2))    
    

from sklearn.preprocessing import PolynomialFeatures

def create_polynomial_regression_model(degree, X_test, y_test):
    "Creates a polynomial regression model for the given degree"
  
    poly_features = PolynomialFeatures(degree=degree)
  
  # transforms the existing features to higher degree features.
    X_train_poly = poly_features.fit_transform(X_train.values.reshape(-1,1))
  
  # fit the transformed features to Linear Regression
    poly_model = LinearRegression()
    poly_model.fit(X_train_poly, y_train.values)
  
  # predicting on training data-set
    y_train_predicted = poly_model.predict(X_train_poly)
  
  # predicting on validation data-set
    y_val_predict = poly_model.predict(poly_features.fit_transform(X_val.values.reshape(-1,1)))
    
  # predicting on testing data-set
    y_test_predict = poly_model.predict(poly_features.fit_transform(X_test.values.reshape(-1,1)))
  
  # evaluating the model on training dataset
    rmse_train = np.sqrt(mean_squared_error(y_train.values, y_train_predicted))
    r2_train = r2_score(y_train.values, y_train_predicted)
  
  # evaluating the model on validation dataset
    rmse_val = np.sqrt(mean_squared_error(y_val.values, y_val_predict))
    r2_val = r2_score(y_val.values, y_val_predict)
    
  # evaluating the model on test dataset
    rmse_test = np.sqrt(mean_squared_error(y_test.values, y_test_predict))
    r2_test = r2_score(y_test.values, y_test_predict)
  
    print("The model performance for the training set")
    print("-------------------------------------------")
    print("RMSE of training set is {}".format(rmse_train))
    print("R2 score of training set is {}".format(r2_train))
  
    print("\n")
  
    print("The model performance for the validation set")
    print("-------------------------------------------")
    print("RMSE of test set is {}".format(rmse_val))
    print("R2 score of test set is {}".format(r2_val))
    
    print("\n")
  
    print("The model performance for the testing set")
    print("-------------------------------------------")
    print("RMSE of test set is {}".format(rmse_test))
    print("R2 score of test set is {}".format(r2_test))
    
    print("Citation Score is {}".format(y_test.values))
    print("Predicted Citation Score is {}".format(y_test_predict))
    
    print("\n")

    print("X_test is {}".format(X_test.values))
    print("y_test is {}".format(y_test.values))
    
    
    pkl_filename = f"Polynomial_regression_norm_cp_degree{degree}_new.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(poly_model, file)
        
        
# To call the model and input X_test, y_test to get y_test_predict, simply use the create_polynomial_regression_model(degree, X_test, y_test) function

# use UR's 2015 - 2019 Scopus API citation per publication count, normalized

X_test = (15.6555 - 11.4493)/3.2734
y_test = 91.2

create_polynomial_regression_model(2, X_test = pd.Series(X_test), y_test=pd.Series(y_test)) # if X-test and y_test is 2-D, use pd.Series(np.array([element1, element2]))

    
