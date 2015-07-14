# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 20:49:14 2015

@author: dyu
"""

'''
Class Exercise
'''

glass.describe()


'''
EXERCISE: Glass Identification (aka "Glassification")
'''

# TASK 1: read the data into a DataFrame

import pandas as pd
glass_cols = ['id','ri','na','mg','al','si','k','ca','ba','fe','type']
glass=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data', names = glass_cols)

# TASK 2: briefly explore the data
glass.info
glass.shape

# TASK 3: convert into binary classification problem
glass['type_num'] = glass.type.map({1:0,2:0, 3:0,4:0, 5:1,6:1,7:1})

# TASK 4: create a feature matrix (X) using all features
feature_cols=['ri','na','mg','al','si','k','ca','ba','fe']
X=glass[feature_cols]

# TASK 5: create a response vector (y)
y = glass.type_num

# TASK 6: split X and y into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4)

# TASK 7: fit a KNN model on the training set using K=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

# TASK 8: make predictions on the testing set and calculate testing accuracy
knn.fit(X,y)
knn.predict(X)

from sklearn import metrics
y_pred = knn.predict(X_test)

# TASK 9: write a for loop that computes testing accuracy for a range of K values
k_range = range(1, 51)
training_error = []
testing_error = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)
    y_pred = knn.predict(X)
    training_error.append(metrics.accuracy_score(y, y_pred))
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    testing_error.append(metrics.accuracy_score(y_test, y_pred))

# TASK 10: plot K value versus testing accuracy to choose on optimal value for K
import matplotlib.pyplot as plt
plt.style.use('ggplot')

plt.plot(k_range, testing_error)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Error')
# TASK 11: calculate the null accuracy

# TASK 12: search for useful features


# redo exercise using only those features