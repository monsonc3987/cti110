Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Adding the title comment
pring("The program calculate and display travel expenses")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    pring("The program calculate and display travel expenses")
NameError: name 'pring' is not defined. Did you mean: 'print'?
print("The program calculate and display travel expenses")
The program calculate and display travel expenses
#taking input budget from user
budget=float(input("Enter the budget:$300"))
Enter the budget:$300
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    budget=float(input("Enter the budget:$300"))
ValueError: could not convert string to float: ''
budget=input("Enter the budget:$300")
Enter the budget:$300
#taking input destination from user
dest=input("Enter your travel destination:Florida")
Enter your travel destination:Florida
#taking input fuel from user
gas=input("How much do you think you will spend on gas? $300")
How much do you think you will spend on gas? $300
#taking input fuel from user
#taking input accomodation from user
hotel=input("Last, how much do you need for food? $400")
Last, how much do you need for food? $400
#taking input accomodation from user
hotel=input("Approximately, how much will you need for accomodation/hotel? $700")
Approximately, how much will you need for accomodation/hotel? $700
#taking input food from user
food=input("Last, how much do you need for food?")
Last, how much do you need for food?
#printing travel expenses
print("---------Travel Exenses---------")
---------Travel Exenses---------
#printing Location and Budget
pring("Location: Florida", dest)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    pring("Location: Florida", dest)
NameError: name 'pring' is not defined. Did you mean: 'print'?
print("Location: Florida", dest)
Location: Florida 
print("Initial Budget: $2000", budget)
Initial Budget: $2000 
#moving cursor to next line as per question
print("\n");


#printing fuel, accomodation,food
print("Fuel: $300",gas)
Fuel: $300 
#calculationg total_expense
total_expense=gas+hotel+food
#calculation total_expense
total_expense=gas+hotel+food

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000 


Fuel: $300 
Acoomodation: $700 
Food: $400 
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 27, in <module>
    rem=budget-total_expense
TypeError: unsupported operand type(s) for -: 'str' and 'str'


============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000   
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000    


Fuel: $300 
Acoomodation: $700 
Food: $400 
Traceback (most recent call last):

  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 26, in <module>
    print("The addition of those 3 numbers is" +total)
NameError: name 'total' is not defined. Did you mean: 'hotel'?

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000 


Fuel: $300 
Acoomodation: $700 
Food: $400 
The addition of those 3 numbers is
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 28, in <module>
    rem=budget-total_expense
TypeError: unsupported operand type(s) for -: 'str' and 'str'

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000   
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000    


Fuel: $300 
Acoomodation: $700 
Food: $400 
$300:
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 25, in <module>
    gas=int(input("$300:"))
ValueError: invalid literal for int() with base 10: ''

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000 


Fuel: $300 
Acoomodation: $700 
Food: $400 
$300
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 25, in <module>
    gas=int(input("$300"))
ValueError: invalid literal for int() with base 10: ''

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000 


Fuel: $300 
Acoomodation: $700 
Food: $400 
$300
$700
$400
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 29, in <module>
    print("The addition of those 3 numbers is" + total_expense)
NameError: name 'total_expense' is not defined

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000 


Fuel: $300 
Acoomodation: $700 
Food: $400 
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 25, in <module>
    rem=budget-total_expense
NameError: name 'total_expense' is not defined


============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000rem=budget-total_expense
NameError: name 'total_expense' is not defined
Enter your travel destination:FloridaHow much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida NameError: name 'total_expense' is not defined
Initial Budget: $2000 rem=budget-total_expense


Fuel: $300 
Acoomodation: $700 
Food: $400 
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 25, in <module>
    rem=budget-total_expense
NameError: name 'total_expense' is not defined



============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas? $300
Approximately, how much will you need for accomodation/hotel? $700
Last, how much do you need for food? $400
---------Travel Exenses---------
Location: Florida 
Initial Budget: $2000 


Fuel: $300 
Acoomodation: $700 
Food: $400 
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 25, in <module>
    rem=budget-total_expense
NameError: name 'total_expense' is not defined


============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 4, in <module>
    budget=int(input("Enter the budget:$"))
ValueError: invalid literal for int() with base 10: ''


============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 6, in <module>
    dest=int(input("Enter your travel destination:Florida"))
ValueError: invalid literal for int() with base 10: ''

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 8, in <module>
    gas=Int(input("How much do you think you will spend on gas?"))
NameError: name 'Int' is not defined. Did you mean: 'int'?

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas?30
Approximately, how much will you need for accomodation/hotel?400
Last, how much do you need for food? $400
============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:400
How much do you think you will spend on gas?300
Approximately, how much will you need for accomodation/hotel?400
Last, how much do you need for food?200
---------Travel Exenses---------
Location: Florida 400
Initial Budget: 2000


Fuel:  300
Acoomodation:  400
Food: 200
Traceback (most recent call last):
  File "C:/Users/deber/OneDrive/Desktop/attempt 2.py", line 25, in <module>
    rem=budget-total_expense
NameError: name 'total_expense' is not defined

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:300
How much do you think you will spend on gas?400
Approximately, how much will you need for accomodation/hotel?200
Last, how much do you need for food?100
---------Travel Exenses---------
Location: Florida 300
Initial Budget: 2000


Fuel:  400
Acoomodation:  200
Food: 100


1300

============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas?300
Approximately, how much will you need for accomodation/hotel?200
Last, how much do you need for food?300
---------Travel Exenses---------
Location: Florida Florida
Initial Budget: 2000


Fuel:  300
Acoomodation:  200
Food: 300


Remaining balance:  1200
>>> 
============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:300
How much do you think you will spend on gas?400
Approximately, how much will you need for accomodation/hotel?200
Last, how much do you need for food?300
---------Travel Exenses---------
Location:  300
Initial Budget: 2000


Fuel:  400
Acoomodation:  200
Food: 300


Remaining balance:  1100
>>> 
============= RESTART: C:/Users/deber/OneDrive/Desktop/attempt 2.py ============
The program calculates and displays travel exenses
Enter the budget:$2000
Enter your travel destination:Florida
How much do you think you will spend on gas?300
Approximately, how much will you need for accomodation/hotel?200
Last, how much do you need for food?300
---------Travel Exenses---------
Location:  Florida
Initial Budget: $ 2000


Fuel: $ 300
Acoomodation: $ 200
Food: $ 300


Remaining balance: $ 1200
