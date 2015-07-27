# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:29:20 2015

@author: dyu
"""

import pandas as pd
import matplotlib.pyplot as plt
dcdata=pd.read_csv('dcprojectdata.csv')


#checking for null values
dcdata.isnull().sum()
dcdata = dcdata[dcdata.neighborhoodcluster.notnull()]

#convert data types to datetime 
dcdata['start_date'] = pd.to_datetime(dcdata.start_date)
dcdata['reportdatetime'] = pd.to_datetime(dcdata.reportdatetime)
dcdata['lastmodifieddate'] = pd.to_datetime(dcdata.lastmodifieddate)
dcdata['end_date'] = pd.to_datetime(dcdata.end_date)
dcdata['date_only'] = pd.to_datetime(dcdata.date_only)

#sort by date
dcdata.sort('date_only')

#map crime types to numbers:
dcdata['crime_type'] = dcdata.offense.map({'ARSON':1,'HOMICIDE':2,'BURGLARY':3, 'SEX ABUSE':4, 'ASSAULT W/DANGEROUS WEAPON':5,'ROBBERY':6,'MOTOR VEHICLE THEFT':7,'THEFT F/AUTO':8, 'THEFT/OTHER':9})

import seaborn as sns
sns.heatmap(dcdata.corr())

'''
LOGISTIC REGRESSION
'''

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split

#First, using x_train, y_train
feature_cols = ['hour','medianhomeprice2013','avgtempf']
X = dcdata[feature_cols]
y = dcdata.violent
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)
y_pred_class = logreg.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)


#Confusion matrix...although something is wrong here
metrics.confusion_matrix(y_test, y_pred_class)

#ROC curve
y_pred_prob = logreg.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

print logreg.coef_
zip(feature_cols, logreg.coef_[0])


#logistic regression using cross-validation
from sklearn.cross_validation import cross_val_score
print cross_val_score(logreg, X, y, cv=10, scoring='accuracy').mean()

#logistic regression visualizations
plt.scatter(dcdata.neighborhoodcluster, dcdata.violent)
plt.scatter(dcdata.avgtempf, dcdata.violent==1)

dcdata.sort('neighborhoodcluster')
plt.plot(dcdata.neighborhoodcluster, crime_pred_prob, color='red')
