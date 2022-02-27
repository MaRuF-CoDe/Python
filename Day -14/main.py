from art import logo,vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')



def get_random():
    return random.choice(data)
def format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def compare(guess,a_followers,b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
def game():
    print(logo)
    score = 0
    game_is_running = True
    b_account = get_random()
    
    while game_is_running:
       
        a_account = b_account
        b_account = get_random()
        while a_account == b_account:
            b_account = get_random()

        print(f"Compare A : {format(a_account)}")
        print(vs)
        print(f"Against B : {format(b_account)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = a_account['follower_count']
        b_followers = b_account['follower_count']
        is_correct = compare(guess,a_followers,b_followers)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You are right . And Score is {score} ")
        else :
            
            print(f"You loose. Score is {score}")
            game_is_running = False
game()