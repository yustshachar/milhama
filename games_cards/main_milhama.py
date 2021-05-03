from games_cards.CardGame import CardGame

play1=CardGame("dima","shachar")
print(play1.player_1.show())
print(play1.player_2.show())

for i in range(1,11):
    print(f"round {i}!!!")
    card1=play1.player_1.get_card()
    print(f"card of {play1.player_1.name}: {card1}")
    card2=play1.player_2.get_card()
    print(f"card of {play1.player_2.name}: {card2}")
    if card1 > card2:
        play1.player_2.add_card(card1)
        play1.player_2.add_card(card2)
        print(f"the winner is {play1.player_1.name}")
    else:
        play1.player_1.add_card(card1)
        play1.player_1.add_card(card2)
        print(f"the winner is {play1.player_2.name}")
    print(play1.player_1.show())
    print(play1.player_2.show())
    print("=====================")

print()
if play1.get_winner() == None:
    print("draw")
else:
    print("the winner in game is" ,play1.get_winner())


