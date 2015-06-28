# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:55:06 2015

@author: dyu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
crimes = pd.read_csv('Crime Incidents - 2014.csv')

'''
DATA CLEANING AND EXPLORATION
'''

#investigate data and properties
crimes.head()
crimes.dtypes

#lowercase formating preference
crimes.columns = [col.lower() for col in crimes]


#convert all date/time objects to datetime format
crimes['start_date'] = pd.to_datetime(crimes.start_date)
crimes['reportdatetime'] = pd.to_datetime(crimes.reportdatetime)
crimes['lastmodifieddate'] = pd.to_datetime(crimes.lastmodifieddate)
crimes['end_date'] = pd.to_datetime(crimes.end_date)

#rename column that is a pandas function
crimes.rename(columns={'shift':'policeshift'}, inplace=True)

#looking at the distribution of crimes by policeshift
crimes.policeshift.value_counts()
crimes.groupby(['policeshift','offense']).count()

#looking at the distribution of crimes

'''
Questions:
What are the hours of the police shifts?

'''
'''
EXPLORATORY VISUALIZATIONS
'''

#crimes groupby plot data
crimes_totals = crimes.groupby('offense').ward.count().order()
#overall barplot of crimes
crimes_totals.plot(kind='bar',grid=False,colormap='Wistia_r')



#data crime barplots by ward
ward1=crimes[crimes.ward == 1].groupby('offense').ward.count()
ward2=crimes[crimes.ward == 2].groupby('offense').ward.count()
ward3=crimes[crimes.ward == 3].groupby('offense').ward.count()
ward4=crimes[crimes.ward == 4].groupby('offense').ward.count()
ward5=crimes[crimes.ward == 5].groupby('offense').ward.count()
ward6=crimes[crimes.ward == 6].groupby('offense').ward.count()
ward7=crimes[crimes.ward == 7].groupby('offense').ward.count()
ward8=crimes[crimes.ward == 8].groupby('offense').ward.count()
sexabuse=crimes[crimes.offense=='SEX ABUSE'].groupby('ward').offense.count()
sexabuse.plot(kind='bar')

#crime barplots by ward
crimes_totals.plot(kind='bar',grid=False,colormap='Wistia_r')
ward1.plot(kind='bar')
ward2.plot(kind='bar')
ward3.plot(kind='bar')
ward8.plot(kind='bar')
#filtering for relevant columns

