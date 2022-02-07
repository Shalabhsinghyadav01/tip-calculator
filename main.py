print("elcome to the tip calculator.")
bill = float(input("what is your bill? $ ")) #it is float because it is created for us for india this value should be in int
tip = int(input("how much tip you like to give ? 10% , 12% , 15%  "))
split = int (input("amoung how much people you want to split the bill?"))
new_bill =  float(bill * (1+(tip/100))) # here the percentage of tip is being added to the bill to give the bill with th tip added 
result = new_bill / split # now the new bill after the tip is added is being split amoung the people 
new_result = round(result,2) # here whatever the value is generated is being round off upto 2 decimal places 
print(f"Each person should pay: $ {new_result}")

# print(type(new_bill)) this is to chech type of variable like int vhar etc.
