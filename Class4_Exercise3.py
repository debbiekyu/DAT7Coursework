'''
EXERCISE THREE
'''

# read ufo.csv into a DataFrame called 'ufo'
import pandas as pd
ufo = pd.read_csv('ufo.csv')

# check the shape of the DataFrame
ufo.shape

# what are the three most common colors reported?
ufo.rename(columns={'Colors Reported':'colors', 'Shape Reported':'shape'}, inplace=True)
ufo.colors.value_counts()
#Most common colors reported are Orange, Red, and Green

# rename any columns with spaces so that tthey don't contain spaces
#see above code

# for reports in VA, what's the most common city?
ufo[ufo.State =='VA'].City.value_counts()
#most common city is Virginia Beach

# print a DataFrame containing only reports from Arlington, VA
ufo[(ufo.State =='VA') & (ufo.City=='Arlington')]

# count the number of missing values in each column
ufo.isnull().sum()

# how many rows remain if you drop all rows with any missing values?
ufo.dropna()
#15510 rows remain 