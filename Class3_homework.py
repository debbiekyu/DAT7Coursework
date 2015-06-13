'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the data with csv.reader() and store it in a list of lists called 'data'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
#import csv module, split the data by "\t"
import csv
with open('chipotle.tsv', 'rU') as f:
	chipotle_data = csv.reader(f, delimiter="\t")
	data = [row for row in chipotle_data]
	    

'''
BASIC LEVEL
PART 2: Separate the header and data into two different lists.
'''
#splice the header row from the file into an empty list; the rest in the data list
header_list = data[0]
order_data = data[1:]


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
#loop through the rows, sum the prices associated with the same order ID, 
#then add those total values per order and divide by 1834
order_list = [row[0] for row in order_data]
order_list_totals = []
for order in order_data:
	if order_data[0] == order_list[0]:
		order_data[4]


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
#go through each row. If it has 'Canned Soda' or 'Canned Soft Drink', in 2nd column, pull
#3rd column value into empty list.  If that value is in the list, don't add. 

uniq_drinks=[]
for row in order_data:
    if "Canned Soda" == row[2]:
        uniq_drinks.append(row[3])
    elif "Canned Soft Drink" == row[2]:
        uniq_drinks.append(row[3])
          
print set(uniq_drinks)		


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''



'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''



'''
BONUS: Think of a question about this data that interests you, and then answer it!