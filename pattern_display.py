"""
Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

# Set variables. Since using range function in for loop
# Upper limit is non-inclusive
# To calculate MAX = max number of '*' in middle row + 2
MIN=2
MAX=12
AVG=int(MAX/2)

for number_of_iter in range(MIN, MAX):

 # Init row to be printed
 row_to_print = ""

 if number_of_iter <= AVG:
  # For iterations 2,3,4,5 - Enter here
  upper_limit = number_of_iter
 else: 
  # For iterations 6,7,8,9,10,11 - Enter here
  upper_limit = MAX - number_of_iter
 
 # use range function: upper_limit is always non-inclusive
 # Corner cases will get eliminated
 for loopvar in range(1,upper_limit):
   row_to_print = row_to_print + " " + "*"

 # Remove preceeding space and nulls during print to console
 if len(row_to_print.strip()) > 0:
  print (row_to_print.strip())
