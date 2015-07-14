# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:28:55 2015

@author: dyu
"""

# TASK 1: read the data from titanic.csv into a DataFrame
import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT7/master/data/titanic.csv'
titanic = pd.read_csv(url, index_col='PassengerId')

# TASK 2: define Pclass/Parch as the features and Survived as the response
feature_cols = ['Pclass', 'Parch']
X = titanic[feature_cols]
y = titanic.Survived

# TASK 3: split the data into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# TASK 4: fit a logistic regression model
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
logreg.fit(X_train, y_train)

# TASK 5: make predictions on testing set and calculate accuracy
y_pred_class = logreg.predict(X_test)
from sklearn import metrics
print metrics.accuracy_score(y_test, y_pred_class)

'''
HANDLING MISSING VALUES
Sci-kit models expect there are no missing values.
You either need to get rid of the data or fill it in.
'Missing value inputation' - filling in missing values
One approach - dropping rows with missing values; obviously this doesn't always work if 
there are a ton of missing values - you'd have to get rid of most of your data.
Second approach - drop rows for one column - this is the below line of code using
notnull() for Age. This still forces us to lose 20% of our data.

With missing value inputation you often fill missing values with the mean for that column.
There are no hard and fast rules with how you fill the values; this is where
domain knowledge often comes in in terms of the best value to fill.
"What is most likely to not cause problems?"

You can build models to inpute values (tends to be a lot of work).
Can use knn to inpute missing values, since it uses similarity to
fill that likely value. KNN is common inputation method.

'''
titanic.isnull().sum()
titanic.dropna().shape
titanic[titanic.Age.notnull()]

#inputing missing values
titanic.Age.fillna(titanic.Age.mean(), inplace=True)

'''
NULL ACCURACY
What accuracy could I achieve by always predicting the most frequent response?
(Usually in the training set) and predicting that in the test set.
Takes the strategy and ignores the X data and you only look at your y data.

For a binary classification problem, you can take the mean of the test set
(that would reflect your most frequent response)

We have to INFER what the majority class is.  For y_test.mean() < .5, we can
infer it is zero.  So we subtract it as 1 to get the null accuracy.  
We want to compare our accuracy score with the null accuracy, so if our 
metrics.accuracy_score is higher than null accracy this is good. 

'''
print y_test.mean()
print 1-y_test.mean()

'''
CONFUSION MATRICES
Sci-kit learn has a confusion matrix function.
[TN, FP - ACTUAL NEGATIVES ROW
FN, TP] - ACTUAL POSITIVES ROW
In sci-kit learn, actuals are always going across.

Calculations for confusion matrix below:
Sensitivity: 43/(52+43) = 43%
Specificity: 107/(107+21) = 83%

THREHOLDS IN LOGISTIC REGRESSION
Logistic regression sets default class cutoff % at .5. 
How do we make a model more sensitivie in terms of adjusting the threshold?
Reduce the threshold.
SENSITIVE classifiers set the threshold very LOW (so that MORE predictions
are classified as POSITIVE)
SPECIFIC classifiers set the threshold very HIGH.

In the code, we re-classified some of the predictions by lowering the threshold.
SENSITIVITY WENT UP
SPECIFICITY WENT DOWN
When one goes up, the other goes down. They are inverse. Sometimes adjusting
threshold will have one stay the same, and the other goes up, but you'll
never have both of the values go up. 
'''
metrics.confusion_matrix(y_test, y_pred_class)

y_pred_prob=logreg.predict_proba(X_test)[:,1]
import matplotlib.pyplot as plt
plt.hist(y_pred_prob)

#lowering the threshold
import numpy as np
y_pred_class = np.where(y_pred_prob >0.25, 1, 0)
metrics.confusion_matrix(y_test, y_pred_class)

'''
HANDLING CATEGORICAL FEATURES
Need to assign values to features that are categories (e.g. male or female)
Can assign numbers if they are ordered, or if unordered, use dummy encoding.
Need to choose scales that make sense relative to the math.

Negative logodds is a decrease in probability; positive coefs increase probability
Sex_Female positive coef is compared to the 0 baseline for male

logreg coef is in logodds by default
you can convert to logodds to change it to odds which makes it easier to interpret
just put coefs in exp() function to convert to odds

the way you encode your category forces you to keep track of how you will
interpret the coefficient.

sci-kit learn will treat responses as classes in calssificaiton models
and does not care how you encode them, the numbers don't matter.



'''
# encode Sex_Female feature
titanic['Sex_Female'] = titanic.Sex.map({'male':0, 'female':1})
#added it to our code
feature_cols = ['Pclass', 'Parch', 'Age','Sex_Female']
X = titanic[feature_cols]
y = titanic.Survived
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
logreg.fit(X_train, y_train)

zip(feature_cols,logreg.coef_[0])

#encoding features with more than 2 levels
titanic.Embarked.value_counts()
#there is no ordered relationship here because they are just ports where ppl
#got onto the ship

pd.get_dummies(titanic.Embarked).head()
pd.get_dummies(titanic.Embarked, prefix='Embarked').head()
pd.get_dummies(titanic.Embarked, prefix='Embarked').iloc[:,1:].head()
#iloc can allow you to select columns in dataframe based on location
#leaving 2 of the 3 out, makes the left out category as the baseline
Embarked_dummies=pd.get_dummies(titanic.Embarked, prefix='Embarked').iloc[:,1:]

titanic=pd.concat([titanic,Embarked_dummies],axis=1)
#axis=0 will concatenate as more rows at the bottom
feature_cols = ['Pclass', 'Parch', 'Age','Sex_Female','Embarked_S','Embarked_Q']
X = titanic[feature_cols]
y = titanic.Survived
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
logreg.fit(X_train, y_train)
zip(feature_cols,logreg.coef_[0])



'''
Definitions:

Training accuracy: training and testing on same data
Testing accuracy: training on one set and testing it on another set
'''