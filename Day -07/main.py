import os
clear = lambda: os.system('cls')

import random
import hangman_art
import hangman_word

print(hangman_art.logo)

chosen_word = random.choice(hangman_word.word_list)
print(chosen_word)

list = []
for n in range (len(chosen_word)):
    list += '_'
print(list)


end_of_game = False
lives = 6


while not end_of_game:  #alternate is end_of_game == False
    guess = input("Guess a letter : ").lower()
    clear()
    if guess in list:
        print(f"You've already guessed {guess}")
    for l in range (len(chosen_word)):
        letter = chosen_word[l]
        if letter == guess:
            list[l] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives==0:
            end_of_game = True
            print("You lose!")
           
    print(f"{' '.join(list)}")

    if "_" not in list:
        end_of_game = True
        print("You Win!!")
    print(hangman_art.stages[lives])