# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:55:06 2015

@author: dyu
"""
'''
DATA CLEANING
'''
import pandas as pd

'''
CLEANING DC GOVERNMENT DATA
'''
crimes = pd.read_csv('Crime Incidents - 2014.csv')

#lowercase formating preference
crimes.columns = [col.lower() for col in crimes]

#convert all date/time objects to datetime format
crimes['start_date'] = pd.to_datetime(crimes.start_date)
crimes['reportdatetime'] = pd.to_datetime(crimes.reportdatetime)
crimes['lastmodifieddate'] = pd.to_datetime(crimes.lastmodifieddate)
crimes['end_date'] = pd.to_datetime(crimes.end_date)

#rename column that is a pandas function
crimes.rename(columns={'shift':'policeshift'}, inplace=True)

'''
CLEANING WEB-SCRAPED NEIGHBORHOOD DATA
(See file NeighborhoodClusterScraper.py)
'''
neighborhooddata=pd.read_csv('neighborhooddata.csv')

#converting dtypes: columns that are objects should be floats or ints
neighborhooddata.avgfamilyincome=neighborhooddata.avgfamilyincome.str.replace(',','').apply(int)
neighborhooddata.foodstamps=neighborhooddata.foodstamps.str.replace(',','').apply(int)
neighborhooddata.receivingtanf=neighborhooddata.receivingtanf.str.replace(',','').apply(float)

#fixing missing values for median home price
#clusters 5, 8, 29, 36 dont have data for 2013, so i'm using the below:
#cluster 5 - used 2012 data
#cluster 8 - used avg for the dist
#cluster 29 - used cluster 30 price
#cluster 36 - used cluster 35 price 
neighborhooddata.medianhomeprice2013.loc[4] =str(821000)
neighborhooddata.medianhomeprice2013.loc[7]=str(602000)
neighborhooddata.medianhomeprice2013.loc[28]=str(208800)
neighborhooddata.medianhomeprice2013.loc[35]=str(330000)
neighborhooddata.medianhomeprice2013=neighborhooddata.medianhomeprice2013.str.replace(',','').apply(int)

#renaming column
neighborhooddata.rename(columns={'<built-in function id>':'cluster_id'}, inplace=True)
neighborhooddata.rename(columns={'cluster_id':'neighborhoodcluster'}, inplace=True)

#dropping random column
neighborhooddata.drop('Unnamed: 0',axis=1,inplace=True)

'''
CLEANING REQUESTED WEATHER DATA FROM NOAA
CSV file was requested from: http://www.ncdc.noaa.gov/cdo-web/

'''
dcweather=pd.read_csv('DC2014Weather.csv')

#isolating data for one weather station (Washington Reagan Airport Station)
reaganweather=dcweather[dcweather.STATION=='GHCND:USW00013743']

#formatting columns 
reaganweather.columns = [col.lower() for col in reaganweather]

'''
MERGING DATAFRAMES 
'''

alldata=pd.merge(crimes, neighborhooddata, how='left', on='neighborhoodcluster')

alldata.to_csv('dcprojectdata.csv')


