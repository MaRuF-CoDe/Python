import random
import os
clear = lambda: os.system('cls')
from art import logo

def deal_card():
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card  = random.choice(cards)
    return card

def calculate_scores(cards):
    
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,comp_score):
    if user_score==comp_score:
        return "Draw 🙃"
    elif comp_score==0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score==0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():

    print(logo)
    user = []
    computer = []
    is_game_over = False

    for _ in range(2):
        user.append(deal_card())
        computer.append(deal_card())

    while not is_game_over:
        user_score = calculate_scores(user)
        comp_score = calculate_scores(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            more = input("Type 'y' to get another card, type 'n' to pass: ")
            if more == 'y':
                user.append(deal_card())
            else:
                is_game_over = True
    while comp_score !=0 and comp_score < 17:
        computer.append(deal_card())
        comp_score = calculate_scores(computer)
    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") =='y':
    clear()
    play_game()
