#Adding the title comment
print("The program calculates and displays travel exenses")
#taking input budget from user
budget=float(input("Enter the budget:$"))
#taking input destination from user
dest=input("Enter your travel destination:")
#taking input fuel from user
gas=float(input("How much do you think you will spend on gas?"))
#taking input accomodation from user
hotel=float(input("Approximately, how much will you need for accomodation/hotel?"))
#taking input food from user
food=float(input("Last, how much do you need for food?"))
#printing travel expenses
print("---------Travel Exenses---------")
#printing Location and Budget
print("Location: ", dest)
print("Initial Budget: $", budget)
#moving cursor to next line as per question
print("\n");
#printing fuel, accomodation,food
print("Fuel: $",gas)
print("Acoomodation: $",hotel)
print("Food: $",food)

#calculation Remaining Balance


total_expense=gas+hotel+food

rem=budget-total_expense
#moving cursor to next
print("\n");
#printing Remaining Balance

print("Remaining balance: $", rem)
