miles_per_gallon = float(input())

dollars_per_gallon = float(input())

#Calculate the unit cost.

unit_cost = dollars_per_gallon / miles_per_gallon

#Evaluate the cost for 20 miles.

your_value1 = unit_cost * 20

#Evaluate the cost for 75 miles.

your_value2 = unit_cost * 75

#Evaluate the cost for 500 miles.

your_value3 = unit_cost * 500

#Print the result and format the

#output up to 2 decimal places.

print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))
