
import random
from replit import clear
from art import logo


players_cards = []
dealers_cards = []

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(dealers_hand, players_hand):
    if dealers_hand == players_hand:
        return "It's a draw - Push!"
    elif dealers_hand == 0:
        return "You lose, dealer has blackjack."
    elif players_hand == 0:
        return "You win! Blackjack!"
    elif players_hand > 21:
        return "Player busted, you lose"
    elif dealers_hand > 21:
        return "Dealer busted, you win!"
    elif players_hand > dealers_hand:
        return "You win!"
    else:
        return "You lose!"


def blackjack():
    game_over = False
    players_cards = []
    dealers_cards = []
    for _ in range(2):
        players_cards.append(deal_card())
        dealers_cards.append(deal_card())
    while not game_over:
        players_score = calculate_score(players_cards)
        dealers_score = calculate_score(dealers_cards)
        print(f" Your card: {players_cards}, current score: {players_score}")
        print(f"Dealer's first card: {dealers_cards[0]}")

        if players_score == 0 or dealers_score == 0 or players_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                players_cards.append(deal_card())
                players_score = calculate_score(players_cards)
            else:
                game_over = True
    while dealers_score != 0 and dealers_score < 17:
        dealers_cards.append(deal_card())
        dealers_score = calculate_score(dealers_cards)

    print(f"Your final hand: {players_cards}, final score: {players_score}")
    print(f"Dealer's final hand: {dealers_cards}, final score: {dealers_score}")
    print(compare(dealers_score, players_score))
    if input("Want to play another game?"):
        clear()
        print(logo)
        blackjack()

print(logo)    
blackjack()

