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


'''
LOGISTIC REGRESSION
'''
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
feature_cols = ['avgtempf', 'neighborhoodcluster','prcp','month']
X = dcdata[feature_cols]
y = dcdata.crime_type
logreg.fit(X, y)
pred_crime = logreg.predict(X)

crime_pred_prob = logreg.predict_proba(X)[:, 1]
plt.scatter(dcdata.neighborhoodcluster, dcdata.crime_type)
plt.plot(dcdata.neighborhoodcluster, crime_pred_prob, color='red')
