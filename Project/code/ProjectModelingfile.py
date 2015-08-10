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
#will drop all values that have neighborhood cluster missing, only 518 of over 38k rows
dcdata = dcdata[dcdata.neighborhoodcluster.notnull()]

#convert data types to datetime 
dcdata['start_date'] = pd.to_datetime(dcdata.start_date)
dcdata['reportdatetime'] = pd.to_datetime(dcdata.reportdatetime)
dcdata['lastmodifieddate'] = pd.to_datetime(dcdata.lastmodifieddate)
dcdata['end_date'] = pd.to_datetime(dcdata.end_date)
dcdata['date_only'] = pd.to_datetime(dcdata.date_only)


#adding weekday, weekend feature cols
dcdata['weekday']=dcdata.dayofweek.map({0:1,1:1,2:1,3:1,4:1,5:0,6:0})
dcdata['weekend']=dcdata.dayofweek.map({0:0,1:0,2:0,3:0,4:0,5:1,6:1})

#add hour grouping
#5-16 day
#17-4 night
dcdata['hour_2']=dcdata.hour.map({1:'night',2:'night',3:'night',4:'night',5:'day',6:'day',7:'day',8:'day',9:'day',10:'day',11:'day',12:'day',13:'day',14:'day',15:'day',16:'day',17:'night',18:'night',19:'night',20:'night',21:'night',22:'night',23:'night',0:'night'})
hour_dummies = pd.get_dummies(dcdata.hour_2, prefix='time2')
dcdata = pd.concat([dcdata, hour_dummies], axis=1)

import seaborn as sns
import numpy as np

#seaborn heatmap
sns.set(style="white")
corr = dcdata.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
           square=True,
           linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

'''
DOWNSAMPLING CODE
'''
#downsampling non-violent cases to resolve class imbalance 
#total violent counts: 6063
#total nonviolent counts: 31807
#will need to downsample 6063/31807, ~19%
mask = np.random.rand(len(dcdata[dcdata.violent==0])) < 0.19
nonviolentdownsample=dcdata[dcdata.violent==0][mask]
violent=dcdata[dcdata.violent==1]
dcdownsample=pd.concat([violent, nonviolentdownsample])
dcdownsample = dcdownsample[dcdownsample.census_tract.notnull()]
len(dcdownsample) #length of this new dataframe is 12026

'''
NULL HYPOTHESIS
'''
dcdownsample.violent.mean()
#0.50124729752203556

'''
DECISION TREES
'''
from sklearn import metrics
from sklearn.cross_validation import cross_val_score

from sklearn.tree import DecisionTreeClassifier
treeclass = DecisionTreeClassifier(random_state=1)
treeclass

feature_cols = ['time2_night','medianhomeprice2013', 'month', 'census_tract','poverty_rate','prcp','16plusemployed','weekend','avgfamilyincome','unemploymentrate','nohsdiploma']
X=dcdownsample[feature_cols]
y=dcdownsample.violent


# loop to find best max_depth
accuracy_scores = []
max_depth_range = range(1, 10)
# use LOOCV with each value of max_depth
for depth in max_depth_range:
    treeclass = DecisionTreeClassifier(max_depth=depth, random_state=1)
    scores = cross_val_score(treeclass, X, y, cv=10, scoring='accuracy')
    accuracy_scores.append(scores.mean())

plt.plot(max_depth_range, accuracy_scores)
plt.xlabel('max_depth')
plt.ylabel('Accuracy')


#max depth 5 tree
treereg = DecisionTreeClassifier(max_depth=5, random_state=1)
treereg.fit(X,y)

#computing feature performance
feature_imp=pd.DataFrame({'feature':feature_cols, 'importance':treereg.feature_importances_}).sort(columns='importance', ascending=False)

from sklearn.tree import export_graphviz
export_graphviz(treereg, out_file='tree_crime12.dot', feature_names=feature_cols)



'''
RANDOM FORESTS
'''

feature_cols = ['time2_night','medianhomeprice2013', 'month', 'census_tract','poverty_rate','prcp','16plusemployed','weekend','avgfamilyincome','unemploymentrate','nohsdiploma']
X = dcdownsample[feature_cols]
y = dcdownsample.violent

from sklearn.ensemble import RandomForestClassifier
rfclass = RandomForestClassifier(n_estimators=150, max_features=5, oob_score=True, random_state=1)
rfclass.fit(X, y)
rfclass.oob_score_

pd.DataFrame({'feature':feature_cols, 'importance':rfclass.feature_importances_}).sort(columns='importance', ascending=False)

'''
LOGISTIC REGRESSION
'''

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.cross_validation import train_test_split

#first model using features determined by decision trees
feature_cols = ['time2_night','weekend', 'census_tract','avgfamilyincome','unemploymentrate']
X = dcdownsample[feature_cols]
y = dcdownsample.violent

logreg = LogisticRegression()
logreg.fit(X, y)
y_pred_class = logreg.predict(X)
print metrics.accuracy_score(y, y_pred_class)

#Now, using x_train, y_train
X_train, X_test, y_train, y_test = train_test_split(X, y)
logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)
y_pred_class = logreg.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)

#Confusion matrix
metrics.confusion_matrix(y_test, y_pred_class)

#ROC curve
y_pred_prob = logreg.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

print metrics.roc_auc_score(y_test, y_pred_prob)

# histogram of predicted probabilities grouped by actual response value
df = pd.DataFrame(data = {'probability':y_pred_prob, 'actual':y_test})
df.probability.hist(by=df.actual, sharex=True, sharey=True)

print logreg.coef_
zip(feature_cols, logreg.coef_[0])

#logistic regression using cross-validation
from sklearn.cross_validation import cross_val_score
print cross_val_score(logreg, X, y, cv=10, scoring='accuracy').mean()

#second model using features determined by random forests
feature_cols = ['time2_night','month', 'census_tract','avgfamilyincome','prcp'] 
X = dcdownsample[feature_cols]
y = dcdownsample.violent

logreg = LogisticRegression()
logreg.fit(X, y)
y_pred_class = logreg.predict(X)
print metrics.accuracy_score(y, y_pred_class)

#Now, using x_train, y_train
X_train, X_test, y_train, y_test = train_test_split(X, y)
logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)
y_pred_class = logreg.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)

#Confusion matrix
metrics.confusion_matrix(y_test, y_pred_class)

#ROC curve
y_pred_prob = logreg.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

print metrics.roc_auc_score(y_test, y_pred_prob)

# histogram of predicted probabilities grouped by actual response value
df = pd.DataFrame(data = {'probability':y_pred_prob, 'actual':y_test})
df.probability.hist(by=df.actual, sharex=True, sharey=True)

print logreg.coef_
zip(feature_cols, logreg.coef_[0])

#logistic regression using cross-validation
from sklearn.cross_validation import cross_val_score
print cross_val_score(logreg, X, y, cv=10, scoring='accuracy').mean()
