import random


logo1 = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0
    if sum(list) > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    return sum(list)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over, you lose"
    elif comp_score > 21:
        return "Opponent went over,You Win"
    elif user_score > comp_score:
        return "You Win"
    else:
        return "You lose"


def playgame():
    print(logo1)
    is_game_over = False
    while not is_game_over:
        user_cards = []
        comp_cards = []
        for i in range(2):
            user_cards.append(get_card())
            comp_cards.append(get_card())
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)

        print(f"your cards: {user_cards}")
        print(f"Computer's first card: {comp_cards[0]}")
        if user_score==0 or comp_score==0 or user_score >21:
            is_game_over = True
        else:
            ch = input("Type 'y' to get another card, type 'n' to pass:")
            if ch == 'y':
                user_cards.append(get_card())
                user_score = calc_score(user_cards)
            else:
                is_game_over = True

        while comp_score != 0 and comp_score < 17:
            comp_cards.append(get_card())
            comp_score = calc_score(comp_cards)
        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand:{comp_cards}")
        print(compare(user_score, comp_score))
        is_game_over = True


playgame()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
    playgame()
