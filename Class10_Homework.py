# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 14:05:42 2015

@author: dyu
"""
'''
Class 10 Yelp Linear Regression Homework
'''
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

import matplotlib.pyplot as plt
import seaborn as sns

#read yelp.csv into a Dataframe
yelp = pd.read_csv('yelp.csv')

#explore the relationship between each of the vote types and the number of stars
sns.pairplot(yelp, x_vars=['cool','useful','funny'], y_vars='stars', size=4)
sns.pairplot(yelp)

'''
It seems that people will write highly useful, cool, and useful and cool reviews for more highly
rated restaurants, generally speaking. There aren't that many cool reviews for 1-2 star
places as opposed to useful reviews for 1-2 star places. There is a greater distribution of funny
reviews across different star ratings; in conjunction from what I have observed, people
like to be comical with their reviews for both great and horrible places.
'''

#define cool/useful/funny as the features and stars as the response
yelpdata=['cool','useful', 'funny']
X = yelp[yelpdata]
y = yelp.stars

#Fit a linear regression model and interpret the coefficients. 
#Do the coefficients make intuitive sense to you? 
#Explore the Yelp website to see if you detect similar trends.
linreg = LinearRegression()
linreg.fit(X, y)
print linreg.intercept_
zip(yelpdata, linreg.coef_)

'''
A unit increase of a 'cool' vote for a review is associated with a 0.27 increase
in the star rating the person gave the restaurant. A unit increase of a 'useful'
vote for a review is associated with a star rating decrease of 0.147 that the person
gave the restaurant. A unit increase in a 'funny' vote for a review is associated with
a 0.135 decrease in the star rating that the person gave the restaurant.

Because two of these coefficients are negative, ('useful' and 'funny'), this implies
that these two coefficients are not independent and have relationships with each other 
and 'cool' reviews as well. 

'''

#Evaluate the model by splitting it into training and testing sets and computing the RMSE. 
#Does the RMSE make intuitive sense to you?

def train_test_rmse(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))

train_test_rmse(X,y)

'''
The rmse is 1.17, which means that the difference between the model and the test data
is about 1.17 stars, which seems like a fairly large error since our units of stars
is only 1-5.  
'''

#Try removing some of the features and see if the RMSE improves.
yelpdata2= ['cool','useful']
X = yelp[yelpdata2]

train_test_rmse(X,y)
'''
Now the rmse is 1.18
'''
cool_only=['cool']
X=yelp[cool_only]
train_test_rmse(X,y)

'''
Now the rmse is 1.20, so this has not been improving. However, the data does not show
a very strong trend between cool/useful/funny so I am not really surprised that our model
does not seem to be very accurate.
'''
'''
BONUS EXERCISES
'''


#Instead of treating this as a regression problem, treat it as a classification problem 
#and see what testing accuracy you can achieve with KNN.

yelpdata=['cool','useful', 'funny']
X = yelp[yelpdata]
y = yelp.stars

from sklearn.neighbors import KNeighborsClassifier

def yelpknnfit(num):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    knn = KNeighborsClassifier(n_neighbors=num)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)
    
#in building a function i wanted to automate the number of neighbors,
#then plotted the distribution of accuracy scores 
knntries = range(5,500)
scores = [yelpknnfit(num) for num in knntries]
knnscores = {}
knnscores['knntries']=knntries
knnscores['scores']=scores
yelpknn = pd.DataFrame(knnscores)
yelpknn.plot(x='knntries',y='scores',kind='scatter')




#Constructing the data myself from yelp.json
with open('yelp.json', 'rU') as f:
    data = f.readlines()
    
import json

#splitting json lines into a list of dictionaries
yelp_list = [json.loads(data[num]) for num in range(10000)]
#fixing 'votes' dictionary of dictionaries

funny = {}
useful ={}
cool = {}

yelp_list[0]['votes'].keys() 



yelpdataframe = pd.DataFrame((yelp_list[0])














