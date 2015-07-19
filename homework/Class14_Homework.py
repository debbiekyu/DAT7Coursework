# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:42:23 2015

@author: dyu
"""

'''
CLASS 14 HOMEWORK: YELP REVIEW TEXT
'''

# read yelp.csv into a dataframe

import pandas as pd
yelp=pd.read_csv('yelp.csv')

#create new dataframe that only has 5 star and 1 star reviews
yelp51=yelp[(yelp.stars==5) | (yelp.stars==1)]

#Split the new DataFrame into training and testing sets, 
#using the review text as the feature and the star rating as the response.

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(yelp51.text, yelp51.stars, random_state=1)

#Use CountVectorizer to create document-term matrices from X_train and X_test.

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(decode_error='ignore')
yelp_train_dtm = vect.fit_transform(X_train)
yelp_test_dtm = vect.transform(X_test)

train_features = vect.get_feature_names()
train_features[:45]
train_features[-45:]

train_arr = yelp_train_dtm.toarray()

import numpy as np
np.sum(train_arr, axis=0)

train_token_counts = pd.DataFrame({'token':train_features, 'count':np.sum(train_arr, axis=0)})
train_token_counts.sort('count', ascending=False)

#Use Naive Bayes to predict the star rating for reviews in the testing set, 
#and calculate the accuracy.

from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(yelp_train_dtm, y_train)

y_pred_class = nb.predict(yelp_test_dtm)

from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class)
print metrics.confusion_matrix(y_test, y_pred_class)

#calculate the AUC, create object with zeros and ones
y_pred_prob = nb.predict_proba(yelp_test_dtm)[:, 1]

y_test_1=[]
for num in y_test:
    if num==5:
        y_test_1.append(1)
    else:
        y_test_1.append(0)
        
print metrics.roc_auc_score(y_test_1, y_pred_prob)

#Plot the ROC curve.
import matplotlib.pyplot as plt
fpr, tpr, thresholds = metrics.roc_curve(y_test_1, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

#Print the confusion matrix, and calculate the sensitivity and specificity.
print metrics.confusion_matrix(y_test_1, y_pred_class)

#sensitivity calculation
813/float(25+813) #results in 0.97

#specificity calculation
126/float(126+58) #results in 0.68

#browse false positives and false negatives; hypothesize why these are incorrectly classified
#false positives
X_test[y_test < y_pred_class]

#false negatives
X_test[y_test > y_pred_class]
'''
For the false negatives, some of the reviews mention some negative 
experiences that were tangentially related to their experience at this restaurant 
they liked (e.g. the previous visit was bad, or right before they went they talk 
about their car breaking down).  

For the false positives, this is a bit harder.The reverse is also true - for example,
people make mention of positive experiences at other places or recommend other
restaurants other than the one they're currently reviewing, so that could be one 
reason why. 
'''
#what threshold would balance sensitivity and specificity?
y_pred_class = np.where(y_pred_prob >0.85, 1, 0)
metrics.confusion_matrix(y_test_1, y_pred_class)
#A threshold of 0.85 would balance both sensitivity and specificity 
#this is a higher threshold so that the model is MORE specific as opposed to
#more sensitive
