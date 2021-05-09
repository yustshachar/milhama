from games_cards.Card import Card
from random import shuffle, randint

class DeckOfCards:
    def __init__(self):
        """מגדירה חפיסת קלפים חדשה עם 52 קלפים"""
        self.cards = []
        for i in range(1, 5):
            for c in range(1, 14):
                self.cards.append(Card(c, i))

    def shuffle(self):
        """מערבבת את כל הקלפים שבחפיסה"""
        shuffle(self.cards)

    def random_for_deal_one(self, end):
        """מקבלת מספר לקצה עליון ומחזירה מספר אקראי בין 0 אליו"""
        return randint(0, end)

    def deal_one(self):
        """שולפת ומחזירה קלף אקראי מתוך החפיסה ומוחקת אותו מהחפיסה"""
        card_one = self.cards.pop(self.random_for_deal_one(len(self.cards) - 1))
        return card_one

    def show(self):
        """מציגה את הקלפים שנותרו בחפיסה"""
        return self.cards