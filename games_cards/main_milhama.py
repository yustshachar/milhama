from games_cards.CardGame import CardGame

play1=CardGame("dima","shachar", 10)
print(play1.player_1.show())
print(play1.player_2.show())
print("=====================")
count=0

for i in range(1,11):
    count+=1  #count בודקת לנו האם המשחק רץ לפחות סיבוב אחד
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
    if len(play1.player_1.player_deck) == 0 or len(play1.player_2.player_deck) == 0: #אם לאחד מהשחקנים נגמר הקלפים המשחק נגמר והוא המנצח
        print("\ngame over")
        break

if count > 0:
    if play1.get_winner() == None:
        print("\ndraw")
    else:
        print("\nthe winner in game is" ,play1.get_winner())
else:
    print("חייבים לשחק לפחות סיבוב אחד בשביל לקבוע מי מנצח")