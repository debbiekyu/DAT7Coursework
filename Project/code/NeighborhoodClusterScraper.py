# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:04:45 2015

@author: dyu
"""

'''
DC Neighborhood Cluster Web-Scraper

This is script for a web-scraper that I created to scrape data from the https://neighborhoodinfodc.org.
I am scraping data by each 'Neighborhood Cluster' - in which each cluster has separate html webpages
devoted to certain types of socioeconomic/population type data.  I have created lists below to scrape
the data points that I want, and then built a script to scrape those elements into the list for each
neighborhood cluster.
'''
import pandas as pd
from bs4 import BeautifulSoup
import requests 

#creating a list of id's for each neighborhood cluster, 39 total
cluster_id=range(1,40)
#lists of data points i want to scrape from the 'population' html page for each cluster
Pop2010=[]
Bl2010=[]
Wh2010=[]
Hs2010=[]
As2010=[]
#lists of data points i want to scrape from the 'well-being' html page for each cluster
poverty08_12=[]
unemployment08_12=[]
employed08_12=[]
nohsdiploma08_12=[]
avgfamincome08_12=[]
foodstamps2014=[]
tanf2014=[]
#lists of data points i want to scrape from the 'housing' html page for each cluster
medianhomeprice2013=[]

#loops through list of cluster id's to scrape the data point for each cluster
#all data points are arranged in tables on each html page; i have identified
#the table column/row from which each data point is located

for num in cluster_id:
    r = requests.get('http://neighborhoodinfodc.org/nclusters/Nbr_prof_clus' + str(num) + '.html')
    b = BeautifulSoup(r.text)    
    Pop2010.append(b('table')[2].find_all('tr')[6].find_all('td')[1].text)
    Bl2010.append(b('table')[2].find_all('tr')[29].find_all('td')[1].text)
    Wh2010.append(b('table')[2].find_all('tr')[32].find_all('td')[1].text)
    Hs2010.append(b('table')[2].find_all('tr')[35].find_all('td')[1].text)
    As2010.append(b('table')[2].find_all('tr')[38].find_all('td')[1].text)
    
    r = requests.get('http://neighborhoodinfodc.org/nclusters/Nbr_prof_clusb' + str(num) + '.html')
    b = BeautifulSoup(r.text)
    poverty08_12.append(b('table')[2].find_all('tr')[6].find_all('td')[1].text)
    unemployment08_12.append(b('table')[2].find_all('tr')[17].find_all('td')[1].text)
    employed08_12.append(b('table')[2].find_all('tr')[21].find_all('td')[1].text)
    nohsdiploma08_12.append(b('table')[2].find_all('tr')[26].find_all('td')[1].text)
    avgfamincome08_12.append(b('table')[2].find_all('tr')[36].find_all('td')[1].text)
    foodstamps2014.append(b('table')[2].find_all('tr')[55].find_all('td')[1].text)
    tanf2014.append(b('table')[2].find_all('tr')[71].find_all('td')[1].text)
    
    r = requests.get('http://neighborhoodinfodc.org/nclusters/Nbr_prof_clusc' + str(num) + '.html')
    b = BeautifulSoup(r.text)
    medianhomeprice2013.append(b('table')[2].find_all('tr')[59].find_all('td')[1].text)
    
#this creates a pandas dataframe that with the index being the cluster id and each column is one of my lists
neighborhood_data = pd.DataFrame({id:cluster_id, 'population':Pop2010, '%_africanamerican':Bl2010, '%_white':Wh2010, '%_hispanic':Hs2010, '%_asian':As2010, 'poverty_rate':poverty08_12,'unemploymentrate':unemployment08_12,'16plusemployed':employed08_12,'nohsdiploma':nohsdiploma08_12,'avgfamilyincome':avgfamincome08_12,'foodstamps':foodstamps2014,'receivingtanf':tanf2014, 'medianhomeprice2013':medianhomeprice2013})

#saving this pandas dataframe as a csv file
neighborhood_data.to_csv('neighborhooddata.csv')


