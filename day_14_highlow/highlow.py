from game_data import data
import random
from art import logo
from art import vs
from replit import clear



# Format the data
def format_data(choice):
    return f"{choice['name']}, a {choice['description']}, from {choice['country']}"

def compare(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
# Pick a random entry from the data
def random_choice():
    return random.choice(data)
# Keep the game running
def game():
    # Display logo
    print(logo)
    # Keep score
    score = 0
    game_continue = True
    # Pick A
    choice_a = random_choice()
    # Pick B
    choice_b = random.choice(data)
    while game_continue:
    # If they win compare the answer with the next one
        choice_a = random_choice()
        choice_b = random_choice()
        while choice_a == choice_b:
            choice_b = random_choice()
    # Print A
        print(f"Compare A: {format_data(choice_a)}")
    # Display vs
        print(vs)
    # Print B
        print(f"Compare B: {format_data(choice_b)}")
        player_guess = input("Who has more followers? 'A' or 'B': ").lower()
        # Set guess to lower case
        print(player_guess)
        choice_a_followers = choice_a["follower_count"]
        print(choice_a_followers)
        choice_b_followers = choice_b["follower_count"]
        print(choice_b_followers)
        guess_correct = compare(player_guess, choice_a_followers, choice_b_followers)
        print(guess_correct)
        clear()
        print(logo)
        # if they win increase the score and tell them the're right
        if guess_correct:
            score += 1
            print(f"You're right!! Current score: {score}.")
        # if they lose end the game with the score
        else:
            game_continue = False
            print(f"That's not right you lose!\nFinal score: {score}")
game()



















