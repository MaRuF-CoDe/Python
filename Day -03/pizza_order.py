from re import M, S


print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you wamt? S, M, or L ")
add_p = input("Do you want pepperoni? Y or N ")
extra_ch = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S" : 
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
if add_p == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_ch =="Y":
    bill += 1

print(f"YOur final bill is :{bill}")