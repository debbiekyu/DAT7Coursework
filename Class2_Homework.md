#Class 2 Homework

**Question 1:**  
i. The first row represents the column headers, therefore each column represents the items 
listed in the order of the items listed in that row. e.g. first column is order_ID, second 
column is quantity, etc. Each row is each individual item in each order, so for example, 
the first order is the first four rows of data, where the customer ordered 4 items.    
ii. There are 1834 orders in the file - I used the tail command to look at the last order 
number.  
iii. There are 55,837 lines in the file.   
iv. It appears that chicken burritos are more popular (count of 553) as opposed to steak
burritos (count of 368).  
v. Chicken burritos have more black beans than pinto beans.m

**Question 2:**  

Code for list of all the CSV or TSV files in the DAT7 repo:
```
find . -name '*.tsv' -o -name '*.csv'  
./data/airlines.csv  
./data/chipotle.tsv  
./data/drinks.csv  
./data/imdb_1000.csv  
./data/sms.tsv  
./data/ufo.csv  

```  

**Question 3:**  
Number of occurrences of the word 'dictionary' across all files in the DAT7 repo: 23
Code while in the DAT7 repo:
```
grep -ir "directory" . | grep -ci "directory"
23
```

**Question 4: (bonus)**  
Something 'interesting' about the Chipotle data:  
The top 5 most frequently ordered items are:  
1. Chicken Bowl  
2. Chicken Burrito  
3. Chips and Guacamole  
4. Steak Burrito  
5. Canned Soft Drink  







