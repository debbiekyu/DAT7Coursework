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

cluster_data = {}
cluster_data['clusters'] = range(1,40)
cluster_data['pop2010'] 

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

def get_cluster_data(num_cluster):
    r = requests.get('http://neighborhoodinfodc.org/nclusters/Nbr_prof_clus' + cluster + '.html')
    b = BeautifulSoup(r.text)
    Clustercluster = {}
    Cluster['Pop2010'] = 