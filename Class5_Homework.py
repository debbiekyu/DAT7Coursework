'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
import pandas as pd
movies = pd.read_csv('imdb_1000.csv')

# check the number of rows and columns
movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
round(movies.duration.mean())
#result is 121 mins

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration').head()
movies.sort('duration').tail()

# create a histogram of duration, choosing an "appropriate" number of bins
import matplotlib.pyplot as plt
movies.duration.plot(kind='hist', bins=25)
#alternatively, i had issues with my ipython console so using terminal, i used:
import pylab
pylab.ion() 
#which then opened my plots in a separate window. 

# use a box plot to display that same data
movies.duration.plot(kind='box')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
#group by content rating and count
movies.groupby('content_rating').title.count()

# use a visualization to display that same data, including a title and x and y labels
movies.groupby('content_rating').title.count().plot(kind='bar', title='Distribution of Movie Ratings')
#NEED TO REVISIT FOR AXIS LABELS!!!

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace('NOT RATED','UNRATED', inplace=True)
movies.content_rating.replace('APPROVED','UNRATED', inplace=True)
movies.content_rating.replace('PASSED','UNRATED', inplace=True)
movies.content_rating.replace('GP','UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace('X','NC-17', inplace=True)
movies.content_rating.replace('TV-MA','NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum()
#there are 3 missing values in the content_rating column. No missing values in other columns.

# if there are missing values: examine them, then fill them in with "reasonable" values
movies.content_rating.replace('NaN','MISSING', inplace=True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration < 120].star_rating.mean()
#7.84
movies[movies.duration > 120].star_rating.mean()
#7.95
#Movies that are longer than 1 hrs have a slightly better star rating avg of 7.95 as opposed
#to movies that hare shorter than 1 hr, which have an avg star rating of #7.84

# use a visualization to detect whether there is a relationship between star rating and duration
movies.plot(kind='scatter',x='star_rating',y='duration')
#There does not seem to be a relationship between star rating and duration, based
#on my scatterplot.

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.groupby('content_rating').duration.mean().plot(kind='bar')
#bar graph does not seem to display any relationship between content rating and duration.

# determine the top rated movie (by star rating) for each genre

movies.groupby('genre').star_rating.max()

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies[movies.title.duplicated()]

# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
