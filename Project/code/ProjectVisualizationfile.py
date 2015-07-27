# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:08:07 2015

@author: dyu
"""

import pandas as pd
dcdata=pd.read_csv('dcprojectdata.csv')


#checking for null values
dcdata.isnull().sum()
#will remove null values for neighborhood clusters
dcdata = dcdata[dcdata.neighborhoodcluster.notnull()]

#convert data types to datetime 
dcdata['start_date'] = pd.to_datetime(dcdata.start_date)
dcdata['reportdatetime'] = pd.to_datetime(dcdata.reportdatetime)
dcdata['lastmodifieddate'] = pd.to_datetime(dcdata.lastmodifieddate)
dcdata['end_date'] = pd.to_datetime(dcdata.end_date)
dcdata['date_only'] = pd.to_datetime(dcdata.date_only)

#sort by date
dcdata.sort('date_only')

'''
DATA EXPLORATION
'''
import numpy as np
import matplotlib as mpl
import scipy as sp 
import matplotlib.pyplot as plt
import seaborn as sns

'''
PLOTS FOCUSING ON THE DISTRIBUTION OF CRIMES
'''
#total crime counts by crime type
dcdata.groupby('offense').ward.count().plot(kind='bar')

#count of violent vs. non-violent
dcdata.groupby('violent').ward.count()


'''
PLOTS FOCUSING ON DATE/TIME ELEMENTS
'''
#line plot of offenses for the year
dcdata.date_only.value_counts().plot(figsize=(15,5))

#looking at the data behind the plot
dcdata.date_only.value_counts()


violentcrimedays=dcdata[dcdata.violent==1].groupby('date_only').ward.agg('count')
violentcrimedays.plot(figsize=(15,5))


#look at crimes by month, violent and non-violent
dcdata.groupby(['month','violent']).ward.agg('count').plot(kind='bar')

#violent crimes only
dcdata[dcdata.violent==1].groupby('month').ward.agg('count').plot(kind='bar',figsize=(15,5))

#violent crimes by day of week
dayofweeklabels=['Mon','Tues','Weds','Thurs','Fri','Sat','Sun']
dcdata[dcdata.violent==1].groupby('dayofweek').ward.agg('count').plot(kind='bar',figsize=(10,4))
plt.xlabel('Number of Violent Crimes')
plt.ylabel('Count')

#violent crimes by time of day
dcdata[dcdata.violent==1].groupby('hour').ward.agg('count').plot(kind='bar',figsize=(10,4))

#violent and non-violent crimes by neighborhood cluster
dcdata.violent.hist(by=dcdata.neighborhoodcluster, figsize=(15,15))
dcdata[dcdata.violent==1].groupby('neighborhoodcluster').ward.agg('count').plot(kind='bar', figsize=(20,5))
dcdata[dcdata.violent==1].groupby('neighborhoodcluster').ward.agg('count')

'''
PLOTS FOCUSING ON WEATHER ELEMENTS
'''
#avg temp barplot
dcdata[dcdata.violent==1].groupby('avgtempf').ward.agg('count').plot(kind='bar',figsize=(20,5))

#avg temp boxplots by offense
dcdata.boxplot(column='avgtempf', by='offense', figsize=(15,5))

#rain
dcdata.prcp.plot(kind='box')

#snow
dcdata[dcdata.groupby('date_only')].snow.agg('count')
