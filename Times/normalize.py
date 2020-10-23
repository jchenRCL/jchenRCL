from sklearn import preprocessing
import numpy as np

# normalize the data attributes
train.loc[:, 'weighted citation count normal'] = preprocessing.normalize(np.array(train['weighted citation count']).reshape(1,-1)).flatten().tolist()
train.head()

