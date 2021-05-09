from games_cards.DeckOfCards import DeckOfCards
from games_cards.Player import Player
from sys import exit

class CardGame:
    def __init__(self,name1="player-1", name2="player-2", num_cards=10):
        """מקבלת כמה קלפים לחלק לכל שחקן, מגדירה 2 שחקנים, יוצרת חפיסה ומתחילה משחק חדש"""
        if type(num_cards) == int: # נכנסת רק כאשר המספר הוא שלם ותקין
            if 1<=num_cards: #בודקת שכמות הקלפים היא תיקנית ולא פחות מ1
                if num_cards>26: # אם כמות הקלפים לחלוקה גדול מ26 היא תחלק רק 26 ותעדכן
                    print("only 26 cards dealt")
                self.num_cards=num_cards
                self.player_1=Player(name1,self.num_cards)
                self.player_2=Player(name2,self.num_cards)
                self.deck_cards=DeckOfCards()
                self.new_game()
            else:
                exit("ERROR!") # אם הכמות היא פחות מ1 תדפיס שגיאה
        else:
            exit("ERROR!")  # אם המספר אינו תיקני

    def get_winner(self):
        """בודקת את אורך הרשימה של שחקן אחד לעומת אורך הרשימה של השחקן השני, ומחזירה את השם של השחקן עם הרשימה הקצרה ביותר או אם הם שווים"""
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