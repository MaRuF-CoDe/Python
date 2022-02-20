import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all = [rock,paper,scissors]
num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if num >=3 or num < 0:
    print("You typed an invalid number, you lose!")
else:

    print(all[num])

    num_items = len(all)
    cp = random.randint(0,num_items-1)
    print("Computer chose:\n")
    print(all[cp])


    if num == 0 and cp == 2:
        print("You win")
    elif cp==0 and num == 2:
        print("You lose")
    elif num > cp:
        print("You win")
    elif cp > num:
        print("You lose")
    elif num == cp :
        print("It's a draw")


print("\n-")
