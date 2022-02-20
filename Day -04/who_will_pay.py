import random

a = input("Give everybody's name sparated by comma : ")
names = a.split(", ")

print(names)

# b = random.choice(names)

num = len(names)
ran = random.randint(0,num-1)
name = names[ran]
print(f"{name} will pay")