'''
Lesson on file reading using Airline Safety Data
https://github.com/fivethirtyeight/data/tree/master/airline-safety
'''

# read the whole file at once, return a single string (including newlines)
# 'rU' mode (read universal) converts different line endings into '\n'
f = open('airlines.csv', 'rU')
data = f.read()
f.close()
# use a context manager to automatically close your file
with open('airlines.csv', 'rU') as f:
    data = f.read()

# read the file into a list (each list element is one row)
with open('airlines.csv', 'rU') as f:
    data = []
    for row in f:
        data.append(row)
# do the same thing using a list comprehension
with open('airlines.csv', 'rU') as f:
    data = [row for row in f]
# side note: splitting strings
'hello dat7 students'.split()
'abc,def,ghi'.split(',')

# split each string (at the commas) into a list
with open('airlines.csv', 'rU') as f:
    data = [row.split(',') for row in f]

# do the same thing using the csv module
import csv
with open('airlines.csv', 'rU') as f:
    data = [row for row in csv.reader(f)]
# separate the header and data

[x*x for x in range(0,10)]

'''
EXERCISES:

1. Create a list containing the average number of incidents per year for each airline.
Example for Aer Lingus: (2 + 0)/30 = 0.07
Expected output: [0.07, 2.73, 0.23, ...]
Loop through each code, find 85-99 incidents, add to 2000-2014 incidents, store the sum, divide the sum by 30, append to a list
'''

Base = data[1:]
avg_incidents = [round((int(row[2])+int(row[5]))/float(30),2) for row in Base]
 

'''
2. Create a list of airline names (without the star).
Expected output: ['Aer Lingus', 'Aeroflot', 'Aerolineas Argentinas', ...]
'''

airlines = [row[0] for row in Base]
airlines_nos = []
for row in Base:
    if row[0][-1] == '*':
        airlines_nos.append(row[0][:-1])
    else:
        airlines_nos.append(row[0])
        
#Loop through each row in Base, take the 0th value, remove the star if there is one
'''

3. Create a list (of the same length) that contains 1 if there's a star and 0 if not.
Expected output: [0, 1, 0, ...]

'''
stars = []
for row in Base:
    if row[0][-1] == '*':
        stars.append(0)
    else:
        stars.append(1)
        
'''
4. BONUS: Create a dictionary in which the key is the airline name (without the star)
   and the value is the average number of incidents.
Expected output: {'Aer Lingus': 0.07, 'Aeroflot': 2.73, ...}
'''


#Take the two lists, avg incidents and airline names, and value-key them together
#loop through the two lists
#OR combine the two lists into key-value pairs




'''
A few extra things that will help you with the homework
'''

# 'set' data structure is useful for gathering unique elements
my_list = [1, 2, 1]
set(my_list)            # returns a set of 1, 2
len(set(my_list))       # count of unique elements

# 'in' statement is useful for lists
1 in my_list            # True
3 in my_list            # False

# 'in' is useful for strings (checks for substrings)
my_string = 'hello there'
'the' in my_string      # True
'then' in my_string     # False

# 'in' is useful for dictionaries (checks keys but not values)
my_dict = {'name':'Kevin', 'title':'instructor'}
'name' in my_dict       # True
 'Kevin' in my_dict      # False

# 'count' method for strings counts how many times a character appears
my_string.count('e')    # 3
