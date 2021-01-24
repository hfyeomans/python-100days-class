#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
from replit import clear
print(logo)

def difficulty(level):
    if level == "easy":
        return 10
    elif level == "hard":
        return 5

def compare(player_numb, computer_numb):
    if player_numb > computer_numb:
        return "Too high."
    elif player_numb < computer_numb:
        return "Too low"


computers_number = random.randint(1, 100)
players_difficulty = input("Choose a level. Type 'easy or 'hard': ")
print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")
print(f"Computers_number is {computers_number}")

def pick_number():
    turns_remaining = difficulty(players_difficulty)
    game_over = False
    while not game_over:
        print(f"You have {turns_remaining} remaining.")
        guess_number = int(input("Make a guess:  "))
        if turns_remaining == 0:
            print("Ran out of guesses you lose!")
            game_over = True
        if guess_number == computers_number:
            print(f"You win! The number was {computers_number}.")
            game_over = True
        else:
            turns_remaining -= 1
            compare(guess_number, computers_number)
            if turns_remaining == 0:
                print(f"You ran out of guesses. The number was {computers_number}")
                game_over = True
                if input("Want to play again? Type 'y' or 'n': ") == 'y':
                    clear()
                    print(logo)
                    pick_number()
pick_number()
        
