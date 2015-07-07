# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:04:45 2015

@author: dyu
"""

'''
DC Neighborhood Cluster Web-Scraping
from https://neighborhoodinfodc.org
'''
from bs4 import BeautifulSoup
import requests
r = requests.get('http://neighborhoodinfodc.org/nclusters/Nbr_prof_clus2.html')
b = BeautifulSoup(r.text)

clusters=range(1,40)
Pop2010=[]
Bl2010=[]
Wh2010=[]
Hs2010=[]
As2010=[]

def get_cluster_data(cluster):
    r = requests.get('http://neighborhoodinfodc.org/nclusters/Nbr_prof_clus' + str(cluster) + '.html')
    b = BeautifulSoup(r.text)
    Pop2010.append(b('table')[2].find_all('tr')[6].find_all('td')[1].text)
    Bl2010.append(b('table')[2].find_all('tr')[29].find_all('td')[1].text)
    Wh2010.append(b('table')[2].find_all('tr')[32].find_all('td')[1].text)
    Hs2010.append(b('table')[2].find_all('tr')[35].find_all('td')[1].text)
    As2010.append(b('table')[2].find_all('tr')[38].find_all('td')[1].text)
    
[get_cluster_data(num) for num in clusters]  
    
    
pop_dict=dict(zip(clusters,Pop2010))
Bl_dict=dict(zip(clusters,Bl2010))
Data=[pop_dict, Bl_dict]
import pandas as pd

data2=pd.DataFrame(Data).T
data2.columns = ['Pop_2010','Bl_2010']
pd.DataFrame(Data,index='clusters', columns=['Pop_2010','Bl_2010'])

#look up defaultdict!

Pop2010 = b('table')[2].find_all('tr')[6].find_all('td')[1].text
#the above prints the table for population in 2010
Bl2010 = b('table')[2].find_all('tr')[29].find_all('td')[1].text
#the above prints the table for % black non-Hispanic, 2010
Wh2010 = b('table')[2].find_all('tr')[32].find_all('td')[1].text
#the above prints the table for % white,non-Hispanic 2010
Hs2010 = b('table')[2].find_all('tr')[35].find_all('td')[1].text
#the above prints the data for % Hispanic 2010
As2010 = b('table')[2].find_all('tr')[38].find_all('td')[1].text
#the above prints the data for % Asian/PI non-Hispanic 2010

#need to append b,c,d