# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:04:45 2015

@author: dyu
"""

'''
DC Neighborhood Cluster Web-Scraping
from https://neighborhoodinfodc.org
'''
import pandas as pd
from bs4 import BeautifulSoup
import requests 

cluster_id=range(1,40)
#population tab 
Pop2010=[]
Bl2010=[]
Wh2010=[]
Hs2010=[]
As2010=[]
#well-being tab
poverty08_12=[]
unemployment08_12=[]
employed08_12=[]
nohsdiploma08_12=[]
avgfamincome08_12=[]
foodstamps2014=[]
tanf2014=[]
#chousing tab
medianhomeprice2013=[]

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
    
neighborhood_data = pd.DataFrame({id:cluster_id, 'population':Pop2010, '%_africanamerican':Bl2010, '%_white':Wh2010, '%_hispanic':Hs2010, '%_asian':As2010, 'poverty_rate':poverty08_12,'unemploymentrate':unemployment08_12,'16plusemployed':employed08_12,'nohsdiploma':nohsdiploma08_12,'avgfamilyincome':avgfamincome08_12,'foodstamps':foodstamps2014,'receivingtanf':tanf2014, 'medianhomeprice2013':medianhomeprice2013})

neighborhood_data.to_csv('neighborhooddata.csv')


