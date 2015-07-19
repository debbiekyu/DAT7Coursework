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

#rename column that is a pandas function
crimes.rename(columns={'shift':'policeshift'}, inplace=True)

#convert all date/time objects to datetime format
crimes['start_date'] = pd.to_datetime(crimes.start_date)
crimes['lastmodifieddate'] = pd.to_datetime(crimes.lastmodifieddate)
crimes['end_date'] = pd.to_datetime(crimes.end_date)

#editing reportdatetime
#currently a string, need to slice hrs/mins/seconds to map to weather date
crimes['date_only']=crimes.reportdatetime.str[:10]
#convert to datetime object
crimes['date_only']=pd.to_datetime(crimes.date_only)

#convert to datetime object
crimes['reportdatetime'] = pd.to_datetime(crimes.reportdatetime)

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
reaganweather=pd.DataFrame(dcweather[dcweather.STATION=='GHCND:USW00013743'])

#formatting columns 
reaganweather.columns = [col.lower() for col in reaganweather]
reaganweather['date']=pd.to_datetime(reaganweather.date)
reaganweather['day']=reaganweather.date_only.dt.day
reaganweather['month']=reaganweather.date_only.dt.month

#formatting temperature and converting to fahrenheit, temperatures from .csv
#files from NOAA are in tenths of degrees without the decimal point
reaganweather['tminf']=(reaganweather.tmin/10)*9/5+32
reaganweather['tmaxf']=(reaganweather.tmax/10)*9/5+32

#calculating average temperature
reaganweather['avgtempf']=(reaganweather.tminf+reaganweather.tmaxf)/2
reaganweather.to_csv('2014reaganweather.csv')

#reformatting date, since converting to datetime with no hr/min/sec results in
#extra characters and date format is incorrect
reaganweather['date_only']=reaganweather.date.astype(str)
#slice part of string that has date
reaganweather['date_only']=reaganweather.date_only.str[21:29]
#convert to datetime 
reaganweather['date_only']=pd.to_datetime(reaganweather.date_only)

#resetting index
reaganweather.reset_index(inplace=True)

weather_cols=['date_only','tminf','tmaxf','avgtempf','prcp','snow','day','month']
reagan_weather=reaganweather[weather_cols]

#save to CSV
reaganweather.to_csv('2014reaganweather.csv')
reagan_weather.to_csv('2014reaganweatheredited.csv')

'''
MERGING DATAFRAMES 
'''
test_merge=pd.merge(crimes,reagan_weather, how='left', on='date_only')


alldata=pd.merge(crimes, neighborhooddata, how='left', on='neighborhoodcluster')
alldata.to_csv('dcprojectdata.csv')


