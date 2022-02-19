print("Welcome to love calculator!")

name1 = input("Enter your name : ").lower()
name2 = input("Enter his/her name : ").lower()

name = name1 + name2

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')

true = t+r+u+e
true = str(true)

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')

love = l+o+v+e
love= str(love)

cal = (true+love)
cal = int(cal)
if cal < 10 or cal>90 :
    print(f"Your score is {cal},You go together like a coke and mentos")
elif cal > 40 and cal < 50 :
    print(f"YOur score is {cal},you are alright together.")
else:
    print("Your score is {cal}.")
