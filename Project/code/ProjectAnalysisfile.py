# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:43:07 2015

@author: dyu
"""
import pandas as pd
dcdata=pd.read_csv('dcprojectdata.csv')


#checking for null values
dcdata.isnull().sum()
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

#looking at the distribution of crimes by policeshift
dcdata.policeshift.value_counts()
dcdata.groupby(['policeshift','offense']).count()

#look at crimes by cluster
dcdata.groupby(['neighborhoodcluster','offense']).agg(['count', 'mean', 'min', 'max'])
neighborhood_offense_count=dcdata.groupby(['neighborhoodcluster','offense']).agg(['count'])

#look at crimes by month
dcdata.groupby(['month','offense']).agg('count')

#looking at the count of crimes by neighborhood cluster
neighborhood_crimes_count=dcdata.groupby('neighborhoodcluster').offense.count()
monthly_crimes_count=dcdata.groupby('month').offense.count()

jan_crimes=dcdata(dcdata.month==1).groupby('offense').ward.count()

jan_crimes.groupby('offense').ward.count()

dailycrimes=dcdata[dcdata.groupby('reportdatetime').ward.count()]

dcdata[dcdata.reportdatetime.day]

'''
EXPLORATORY VISUALIZATIONS
'''

'''
LINE PLOTS
'''
#line plot of offenses for the year
dcdata.date_only.value_counts().plot()


'''
CRIME BARPLOTS 
'''
#crimes groupby plot data
crimes_totals = dcdata.groupby('offense').ward.count().order()

#ward crime data
ward1=dcdata[dcdata.ward == 1].groupby('offense').ward.count()
ward2=dcdata[dcdata.ward == 2].groupby('offense').ward.count()
ward3=dcdata[dcdata.ward == 3].groupby('offense').ward.count()
ward8=dcdata[dcdata.ward == 8].groupby('offense').ward.count()

#total crime barplot
crimes_totals.plot(kind='bar',grid=False,colormap='Wistia_r')
#crime barplots by ward
ward1.plot(kind='bar')
ward2.plot(kind='bar')
ward3.plot(kind='bar')
ward8.plot(kind='bar')

'''
SPECIFIC OFFENSE PLOTS
'''
sexabuse=dcdata[dcdata.offense=='SEX ABUSE'].groupby('neighborhoodcluster').offense.count()
assault=dcdata[dcdata.offense=='ASSAULT W/DANGEROUS WEAPON'].groupby('neighborhoodcluster').offense.count()
homicide=dcdata[dcdata.offense=='HOMICIDE'].groupby('neighborhoodcluster').offense.count()
arson=dcdata[dcdata.offense=='ARSON'].groupby('neighborhoodcluster').offense.count()
burglary=dcdata[dcdata.offense=='BURGLARY'].groupby('neighborhoodcluster').offense.count()
theft_other=dcdata[dcdata.offense=='THEFT/OTHER'].groupby('neighborhoodcluster').offense.count()
theft_auto=dcdata[dcdata.offense=='THEFT F/AUTO'].groupby('neighborhoodcluster').offense.count()
robbery=dcdata[dcdata.offense=='ROBBERY'].groupby('neighborhoodcluster').offense.count()
vehicletheft=dcdata[dcdata.offense=='MOTOR VEHICLE THEFT'].groupby('neighborhoodcluster').offense.count()

vehicletheft.append('assault')


vehicletheft.plot(kind='bar')
assault.plot(kind='bar')




offensetotal=dcdata.groupby('neighborhoodcluster').offense.count()

ind=np.arange(39)
plt.bar(ind,offensetotal, color='green')
plt.xticks(ind)



ind=np.arange(39)
plt.bar(ind,robbery)
plt.bar(ind,theft_other,color='green',bottom=robbery)
plt.xticks(ind)

#plots using pandas default plots
sexabuse.plot(kind='bar',color='blue')
assault.plot(kind='bar',color='green')


#filtering for relevant columns

'''
BROKEN SEABORN CODE
'''

#plots using seaborn
#BROKEN!!!
#sns.set(style="whitegrid")
#plt.figure(figsize=(12,6))
#sns.barplot(x='offense', data=dcdata)

#didn't work plot1=set_xticklabels(rotation=30)
#plt.setp(labels, rotation=45)

'''
HORIZONTAL BARPLOT
'''

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Plot the total crashes
sns.set_color_codes("pastel")
sns.barplot(x="offense", y="neighborhoodcluster", data=dcdata,
            label="Total", color="b")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="alcohol", y="abbrev", data=crashes,
            label="Alcohol-involved", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Automobile collisions per billion miles")
sns.despine(left=True, bottom=True)


sns.factorplot(x='offense', row='neighborhoodcluster', data=dcdata, kind='bar')
sns.factorplot(x='offense',data=ward8,kind='bar')
sns.factorplot(x='ward',hue='ward',data=assault,kind='bar',palette='Blues')


