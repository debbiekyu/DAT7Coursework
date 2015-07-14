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
#loop through the rows 
#then add those total values per order and divide by 1834
order_list_totals = [float(order[4][1:]) for order in order_data]
average_price = round(sum(order_list_totals)/(len(set(order_num))), 2)
#ANSWER: Average price is $18.81

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
#go through each row. If it has 'Canned Soda' or 'Canned Soft Drink', in 2nd column, pull
#3rd column value into empty list.  If that value is in the list, don't add. 
         
uniq_drinks = [row[3] for row in order_data if "Canned" in row[2]]
print set(uniq_drinks)		
#ANSWER: set(['[Lemonade]', '[Dr. Pepper]', '[Diet Coke]', '[Nestea]', '[Mountain Dew]', '[Diet Dr. Pepper]', '[Coke]', '[Coca Cola]', '[Sprite]'])

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
#go through each row to see if it has "burrito" in row[2], get total lines
#get total toppings count via # of commas per burrito line, total them and divide by
#total list of burrito lines

burrito_count = [1 for row in order_data if "Burrito" in row[2]]
topping_count = [row[3].count(",") +1 for row in order_data if "Burrito" in row[2]]
avg_burrito_toppings= round(float(sum(topping_count))/sum(burrito_count), 2)
#ANSWER: avg_burrito_toppings is 5.4 toppings

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
#create a key for each unique chip order
#loop through rows in order_data, if there is a chip order, create a key
#provided the key does not already exist, otherwise, add to value to existing key

#using default dict:
from collections import defaultdict
chips_dict = defaultdict(int)
for row in order_data:
    if "Chips" in row[2]:
        chips_dict[row[2]] =  chips_dict[row[2]] + int(row[1])
        
#ANSWER: defaultdict(<type 'int'>, {'Chips and Roasted Chili-Corn Salsa': 18, 'Chips and Tomatillo-Red Chili Salsa': 25, 'Chips and Mild Fresh Tomato Salsa': 1, 'Chips and Guacamole': 506, 'Chips and Fresh Tomato Salsa': 130, 'Chips and Tomatillo Red Chili Salsa': 50, 'Chips and Tomatillo-Green Chili Salsa': 33, 'Side of Chips': 110, 'Chips and Roasted Chili Corn Salsa': 23, 'Chips': 230, 'Chips and Tomatillo Green Chili Salsa': 45})
        
#not using default dict:
chips_dict = {}
for row in order_data:
    if "Chips" in row[2]:
        if row[2] in chips_dict:
            chips_dict[row[2]] =  chips_dict[row[2]] + int(row[1])
        else:
            chips_dict[row[2]] = int(row[1])

#ANSWER: {'Chips': 230,
# 'Chips and Fresh Tomato Salsa': 130,
# 'Chips and Guacamole': 506,
# 'Chips and Mild Fresh Tomato Salsa': 1,
# 'Chips and Roasted Chili Corn Salsa': 23,
# 'Chips and Roasted Chili-Corn Salsa': 18,
# 'Chips and Tomatillo Green Chili Salsa': 45,
# 'Chips and Tomatillo Red Chili Salsa': 50,
# 'Chips and Tomatillo-Green Chili Salsa': 33,
#'Chips and Tomatillo-Red Chili Salsa': 25,
# 'Side of Chips': 110}
'''
BONUS: Think of a question about this data that interests you, and then answer it!