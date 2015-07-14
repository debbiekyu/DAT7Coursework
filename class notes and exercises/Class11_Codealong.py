# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:38:32 2015

@author: dyu
"""

# glass identification dataset
import pandas as pd
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data'
col_names = ['id','ri','na','mg','al','si','k','ca','ba','fe','glass_type']
glass = pd.read_csv(url, names=col_names, index_col='id')
glass['assorted'] = glass.glass_type.map({1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1})

glass.plot(x='al', y='ri', kind='scatter')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()

feature_cols=['al']
X=glass[feature_cols]
y=glass.ri

linreg.fit(X, y)
print linreg.intercept_
print linreg.coef_

ri_pred=linreg.predict(X)
plt.plot(glass.al, ri_pred, color='red')
plt.scatter(glass.al,glass.ri)

sns.lmplot(x='al',y='ri',data=glass, ci=None)

zip(feature_cols, linreg.coef_)

plt.scatter(glass.al, glass.assorted)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
feature_cols=['al']
X=glass[feature_cols]
y=glass.assorted
linreg.fit(X, y)
assorted_pred=linreg.predict(X)
plt.scatter(glass.al, glass.assorted)
plt.plot(glass.al, assorted_pred, color='red')

nums=np.array([5,15,8])
np.where(nums > 10, 'big', 'small')

assorted_pred_class = np.where(assorted_pred >= 0.5, 1, 0)
plt.scatter(glass.al, glass.assorted)
plt.plot(glass.al, assorted_pred_class, color='red')

glass['assorted_pred_class']=assorted_pred_class
glass.sort('al',inplace=True)

#note the below where the second plot references the dataframe
plt.scatter(glass.al, glass.assorted)
plt.plot(glass.al, glass.assorted_pred_class, color='red')

'''
MOVING ONTO LOGISTIC REGRESSION
'''
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
#C=1e9 turns off regularization parameter??
feature_cols=['al']
X=glass[feature_cols]
y=glass.assorted
logreg.fit(X, y)

assorted_pred_class=logreg.predict(X)

plt.scatter(glass.al, glass.assorted)
plt.plot(glass.al, assorted_pred_class, color='red')

assorted_pred_prob=logreg.predict_proba(X)[:,1]
plt.scatter(glass.al, glass.assorted)
plt.plot(glass.al, assorted_pred_prob, color='red')

print logreg.predict_proba(1)
print logreg.predict_proba(2)
print logreg.predict_proba(3)
#tells you predicted probabilities for all classes
#results are 2 values, proba of 0, and proba of 1 
logreg.predict_proba(X)[:,1] #notation at the end cuts off proba for all except for 1 in your array
#rows, comma columns : means all and 1 means column 1, not column 0

'''
REVIEW OF READING ON PROBABILITY AND ODDS
''''''
odds is the thing you selected over the things that dont fit the criteria
probability of 50% is also odds of 1
probablity is bounded from 0 to 1
odds are bounded to infinity

'''
np.exp(1) # e in numpy
np.log(2.718) #1, or the inverse of e
np.exp(np.log(25))








