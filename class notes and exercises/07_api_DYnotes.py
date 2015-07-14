'''
CLASS: Getting Data from APIs

What is an API?
- Application Programming Interface
- Structured way to expose specific functionality and data access to users
API calls could be about actions as well, not just pulling the data
- Web APIs usually follow the "REST" standard

How to interact with a REST API:
- Make a "request" to a specific URL (an "endpoint"), and get the data back in a "response"
- There are different request methods
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Request is usually in a URL format
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)
'''

# read IMDb data into a DataFrame: we want a year column!
import pandas as pd
movies = pd.read_csv('imdb_1000.csv')
movies.head()

# use requests library to interact with a URL
import requests
r = requests.get('http://www.omdbapi.com/?t=the shawshank redemption&type=movie&r=json')

# check the status: 200 means success, 4xx means error
r.status_code
# view the raw response text
r.text
# decode the JSON response body into a dictionary
r.json()
# extracting the year from the dictionary
r.json()['Year']
d = r.json()
d['Year']
# what happens if the movie name is not recognized?
r = requests.get('http://www.omdbapi.com/?t=blahblahblah&type=movie&r=json')

# define a function to return the year
#You will need to build a function so you don't need to rewrite URLs when
#working with APIs. Each request will be a URL.
def get_movie_year(title):
    r = requests.get('http://www.omdbapi.com/?t=' + title + '&type=movie&r=json')
    info = r.json()
    if info['Response']=='True':
        return int(info['Year'])
    else:
        return 0 

# test the function
get_movie_year('Finding Nemo')

# create a smaller DataFrame for testing
top_movies = movies.head().copy()

# write a for loop to build a list of years
from time import sleep
years = []
for title in top_movies.title:
    years.append(get_movie_year(title))
    sleep(1)

#list comprehension without sleep function
years = [get_movie_year(title) for title in top_movies.title]
    
#sleep function is there to address rate limiting, so you're hitting the API in
#a methodical way so as not to perceive you as a threat. 1 call per second is considered
#very slow! 
    
# check that the DataFrame and the list of years are the same length
assert(len(top_movies)==len(movie_years))
#if something has failed, assert can alert you that something has failed
#assuming years is the same length as dataframe

# save that list as a new column
top_movies['years'] = years

'''
Bonus content: Updating the DataFrame as part of a loop
'''

# enumerate allows you to access the item location while iterating
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print index, letter

# iterrows method for DataFrames is similar
for index, row in top_movies.iterrows():
    print index, row['title']

# create a new column and set a default value
movies['year'] = -1

# loc method allows you to access a DataFrame element by 'label'
movies.loc[0, 'year'] = 1994

# write a for loop to update the year for the first three movies
for index, row in movies.iterrows():
    if index < 3:
        movies.loc[index, 'year'] = get_movie_year(row['title'])
        sleep(1)
    else:
        break

'''
Other considerations when accessing APIs:
- Most APIs require you to have an access key
- Most APIs limit the number of API calls you can make (per day, hour, minute, etc.)
- Not all APIs are free
- Not all APIs are well-documented
- Pay attention to the API version

Python wrapper is another option for accessing an API:
- Set of functions that "wrap" the API code for ease of use
- Potentially simplifies your code
- But, wrapper could have bugs or be out-of-date or poorly documented
'''
