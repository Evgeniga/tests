import sys  
import random 
import json

card_deck = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 
             'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
             'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10',
             'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10']
user_list = dict()


user_command = sys.argv[1]
if user_command == "start":
    count_cards_player = int(sys.argv[2])
    count_players = int(sys.argv[3])
    if count_players <= len(card_deck)/count_cards_player:
       i = 0
       while i < count_players:
        user_cards = []
        j = 0
        while j < count_cards_player:
          random_card = random.choice(card_deck)
          user_cards.append(random_card)
          card_deck.remove(random_card)
          j = j + 1
        user_list[i + 1] = user_cards
        i = i + 1
       print(user_list)
       json.dump(user_list, open("user_list.json", "w"))

    else:
        print('карт не хватит на всех игроков')   

if user_command == "get-cards":
    user_list = json.load(open("user_list.json"))
    player_nomber = sys.argv[2]
    
    if player_nomber in user_list:
       print (user_list[player_nomber])
    else:
       print("нет игрока")
