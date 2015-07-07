# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:40:59 2015

@author: dyu
"""

'''
Class 11 In-class Exercise
'''

#Read titanic.csv into a DataFrame.
import pandas as pd
titanic = pd.read_csv('titanic.csv')

#Define Pclass and Parch as the features, and Survived as the response.
feature_cols = ['Pclass', 'Parch']
X=titanic[feature_cols]
y=titanic.Survived

#Split the data into training and testing sets.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#Fit a logistic regression model and examine the coefficients to confirm that they make intuitive sense.
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
zip(feature_cols, logreg.coef_[0])

#Make predictions on the testing set and calculate the accuracy.
y_pred = logreg.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred)