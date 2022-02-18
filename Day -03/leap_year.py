year = int (input("Enter any year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is leap year")
        else:
            print("Not leap year")
    else: 
        print("Leap Year")
else:
    print("The year is not leap year")