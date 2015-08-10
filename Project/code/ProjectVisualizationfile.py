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
VISUALIZING & EXPLORING DEMOGRAPHIC INFO
'''
dcdata.groupby('neighborhoodcluster').population.plot(kind='bar')

dcdata[dcdata.groupby('neighborhoodcluster').population]

dcdata.plot(kind='scatter',x='neighborhoodcluster',y='population')

dcdata.plot(kind='scatter',x='poverty_rate',y='medianhomeprice2013',s=dcdata['population']/50,c='neighborhoodcluster',colormap='rainbow',figsize=(10,10))

dcdata.sort('neighborhoodcluster').population.unique()

'''
PLOTS FOCUSING ON THE DISTRIBUTION OF CRIMES
'''
#total crime counts by crime type
dcdata.groupby('offense').ward.count().plot(kind='bar')

#count of violent vs. non-violent
dcdata.groupby('violent').ward.count()

dcdata.sort('census_tract')
dcdata[dcdata.violent==1].groupby('census_tract').ward.agg('count').plot(kind='bar',figsize=(20,4))


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
#nonviolent crimes by time of day
dcdata[dcdata.violent==0].groupby('hour').ward.agg('count').plot(kind='bar',figsize=(10,4))

#stacked barplot of crime types by hour
dcdata['nonviolent']=dcdata.offense.map({'SEX ABUSE':0,'HOMICIDE':0,'ASSAULT W/DANGEROUS WEAPON':0, 'ROBBERY':0, 'ARSON':1,'BURGLARY':1,'THEFT/OTHER':1,'THEFT F/AUTO':1, 'MOTOR VEHICLE THEFT':1})
offense_hrs=['violent','nonviolent','hour']
offensedf=dcdata[offense_hrs]
offensedf.groupby('hour').sum().plot(kind='bar', figsize=(10,4), stacked=True)


#violent and non-violent crimes by neighborhood cluster
dcdata.violent.hist(by=dcdata.neighborhoodcluster, figsize=(15,15))
dcdata[dcdata.violent==1].groupby('neighborhoodcluster').ward.agg('count').plot(kind='bar', figsize=(20,5))
dcdata[dcdata.violent==1].groupby('neighborhoodcluster').ward.agg('count')


'''
PLOTS FOCUSING ON WEATHER ELEMENTS
'''
reagan_weather_2=pd.read_csv('2014reaganweatheredited.csv')
reagan_weather_2['date_only'] = pd.to_datetime(reagan_weather_2.date_only)
offensecountday=['violent','nonviolent','date_only']
offensedf2=dcdata[offensecountday]
offensedf3=offensedf2.groupby('date_only').sum()
offensedf3.reset_index(inplace=True)
weather_merge=pd.merge(reagan_weather_2,offensedf3, how='left', on='date_only')
weather_merge['rain_inches']=(weather_merge.prcp/10)*0.0393701
weather_merge.groupby('date_only').rain_inches.sum().plot(kind='bar', figsize=(20,5))

#avg temp barplot
dcdata[dcdata.violent==1].groupby('avgtempf').ward.agg('count').plot(kind='bar',figsize=(20,5))

#avg temp boxplots by offense
dcdata.boxplot(column='avgtempf', by='offense', figsize=(15,5))

#rain
dcdata.prcp.plot(kind='box')

#snow
dcdata[dcdata.groupby('date_only')].snow.agg('count')

#rain
dcdata['rain_inches']=(dcdata.prcp/10)*0.0393701

rain=['month','date_only','rain_inches','violent']
raindf=dcdata[rain]
raindf.groupby('month').sum()

raindf.hist(by=raindf.date_only, sharex=True)
raindf.groupby('date_only').rain_inches.sum().plot(kind='bar', figsize=(20,5))
raindf.groupby('date_only').violent.sum().plot(kind='bar', figsize=(20,5))
