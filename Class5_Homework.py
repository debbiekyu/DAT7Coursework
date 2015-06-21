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
#alternatively, when i had issues with my ipython console so using terminal, i also used:
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
movies.content_rating.replace(['NOT RATED','APPROVED','PASSED','GP'],'UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(['X','TV-MA'], 'NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum()
#there are 3 missing values in the content_rating column. No missing values in other columns.

# if there are missing values: examine them, then fill them in with "reasonable" values
movies.content_rating.fillna(value='NA', inplace=True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration < 120].star_rating.mean()
#7.84
movies[movies.duration >= 120].star_rating.mean()
#7.95
#Movies that are 2 hrs or longer have a slightly better star rating avg of 7.95 as opposed
#to movies that are shorter than 2 hrs, which have an avg star rating of #7.84

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
#The above didn't show much variation in terms of mean so did the following:
movies.boxplot(by='content_rating')

# determine the top rated movie (by star rating) for each genre

movies.groupby('genre').describe()

#NEED TO REVISIT THIS TO GET THE TITLE OF THE MOVIE!! 

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies[movies.title.duplicated()]
#the above code is telling me what movies supposedly have the same title, need to check they are actually dupes

# calculate the average star rating for each genre, but only include genres with at least 10 movies

avg_star_rating = movies.groupby('genre').star_rating.agg(['mean'])
genre_count = movies.genre.value_counts()[:9]




#
#for title, genre in movies.groupby('genre'):
#    print movies.star_rating.max()

movies.filter([movies.genre.value_counts() >=10])

movies[movies.genre=='Drama'].star_rating.mean()

top_movies =[]
for title, star_rating in movies.groupby('genre'):
    top_movies['title'] = star_rating.max()

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
