from games_cards.DeckOfCards import DeckOfCard
from games_cards.Player import Player
from sys import exit

class CardGame:
    def __init__(self,name1, name2, num_cards=10):
        """מקבלת כמה קלפים לחלק לכל שחקן, מגדירה 2 שחקנים, יוצרת חפיסה ומתחילה משחק חדש"""
        self.num_cards=num_cards
        self.player_1=Player(name1,self.num_cards)
        self.player_2=Player(name2,self.num_cards)
        self.deck_cards=DeckOfCard()
        self.new_game()

    def get_winner(self):
        """בודקת את אורך הרשימה של שחקן אחד לעומת אורך הרשימה של השחקן השני, ומחזיקה את השם של השחקן עם הרשימה הקצרה ביותר או אם הם שווים"""
        if len(self.player_1.player_deck) < len(self.player_2.player_deck):
            return self.player_1.name
        elif len(self.player_1.player_deck) == len(self.player_2.player_deck):
            return None
        else:
            return self.player_2.name

    def new_game(self):
        """מערבבת את החפיסה השלימה ומחלקת קלפים לשני השחקנים, במידה והפונקציה הופעלה במהלך המשחק היא תציג שגיאה"""
        if len(self.deck_cards.show()) == 52:
            self.deck_cards.shuffle()
            self.player_1.set_hand(self.deck_cards)
            self.player_2.set_hand(self.deck_cards)
        else:
            exit("Error!")