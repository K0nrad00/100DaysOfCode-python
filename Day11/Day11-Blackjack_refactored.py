## Demo of final project: https://appbrewery.github.io/python-day11-demo/
from random import sample, choice

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def who_wins(your_cards, your_sum, pc_cards, pc_sum, continue_game):
    # continue_game = False
    if your_sum > 21:
        print(f"Your cards are {your_cards} and their sum is {your_sum} \n -You loose :(")
        print(f"Computer's draw: {pc_cards} and score is {pc_sum}")
        continue_game = False
    elif pc_sum > 21 and your_sum <= 21:
        print(f"Your cards are {your_cards} with score of: {your_sum}\n - YOU WIN")
        print(f"Computer cards were {pc_cards} and score of {pc_sum}")
        continue_game = False
    elif your_sum <= 21 and your_sum > pc_sum:
        print(f"Your cards are {your_cards} with score of: {your_sum}\n - YOU WIN")
        print(f"Computer cards were {pc_cards} and score of {pc_sum}")
        continue_game = False
    else:
        print(f"Your cards are {your_cards} with score of: {your_sum}\n - YOU'VE LOST :( ")
        print(f"Computer cards were {pc_cards} and score of {pc_sum}")
        continue_game = False



continue_play = True
# if wanna_play == "y":
while continue_play:
    wanna_play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wanna_play == "y":
        print("\n" * 20)

        print(logo)
        users_cards = sample(cards, 2)
        user_sum = 0
        for item in users_cards:
            user_sum += item
        print(f"Your cards {users_cards}, current score: {user_sum}")

        computer_cards = sample(cards, 2)
        computer_sum = sum(computer_cards) # Different way of getting sum from list of items
        print(f"Computer's first card: {computer_cards[0]} ") #and current score: {computer_sum}

        continue_card_draw = True

        while continue_card_draw:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                users_cards.append(choice(cards))
                computer_cards.append(choice(cards))
                user_sum += users_cards[-1]
                computer_sum = sum(computer_cards)
                who_wins(users_cards, user_sum, computer_cards, computer_sum, continue_card_draw)
                continue_card_draw = False
            if another_card == "n":
                computer_cards.append(choice(cards))
                computer_sum = sum(computer_cards)
                who_wins(users_cards, user_sum, computer_cards, computer_sum, continue_card_draw)
                continue_card_draw = False
    else:
        continue_play = False










