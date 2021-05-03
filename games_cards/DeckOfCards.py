# [{1:Club},{2:Club},...]
from games_cards.Card import Card
from random import shuffle, randint, randrange

class DeckOfCard():
    def __init__(self):
        """מגדירה חפיסת קלפים חדשה עם 52 קלפים"""
        self.cards=[]
        for i in range(1,5):
            for c in range(1,14):
                self.cards.append(Card(c,i))

    def shuffle(self):
        """מערבבת את כל הקלפים שבחפיסה"""
        shuffle(self.cards)

    def deal_one(self):
        """שולפת ומחזירה קלף אקראי מתוך החפיסה ומוחקת אותו מהחפיסה"""
        one=self.cards.pop(randint(0,len(self.cards)-1))
        return one

    def show(self):
        """מציגה את הקלפים שנותרו בחפיסה"""
        return self.cards