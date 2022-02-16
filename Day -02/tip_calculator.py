print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? "))

people = int(input("How many people to split the bill? "))

perce = bill * (tip/100)

pay = (bill + perce)/people

# result = round(pay,2)

result = "{:.2f}".format(pay)

print (f"Each person should pay: ${result}")