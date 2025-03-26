import random
from art import logo

def deal_card():
    cards  = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lost. The opponent has BlackJack"
    elif u_score == 0:
        return "Win with a BlackJack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"You're cards are: {user_cards} and your score is: {user_score}")
        print(f"The computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score > 0 and user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or type 'n' to pass\n")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, and your final score is: {user_score}")
    print(f"The computer's final hand is: {computer_cards}, and the computer's final score is: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you wanna play a BlackJack game, type 'y' to play and type 'n' to not play\n") == "y":
    print("\n" * 20)
    play_game()