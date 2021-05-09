from random import randint
from games_cards.Card import Card
from sys import exit

class Player:
    def __init__(self, name, num_cards=10):
        self.name = name
        self.num_cards = num_cards
        self.player_deck = []

    def set_hand(self, deck_cards):
        """מקבלת חפיסת קלפים ומחלקת אותם לשחקן. אפשר מקסימום 26 קלפים לשחקן"""
        for i in deck_cards.cards:
            if type(i) != Card:
                exit("ERROR")
        for i in range(self.num_cards):
            self.player_deck.append(deck_cards.deal_one())
            if len(self.player_deck) == 26:
                break

    def random_get_card(self, end):
        """מחזירה ערך אקראי לצורך בדיקה"""
        return randint(0, end)

    def get_card(self):
        """שולפת קלף מהחבילה של השחקן ומחזיר אותו"""
        player_card = self.player_deck.pop(self.random_get_card(len(self.player_deck)-1))
        return player_card

    def add_card(self, card):
        """מוסיפה קלף חדש לחפיסה של השחקן"""
        self.player_deck.append(card)

    def show(self):
        """מציגה את שם השחקן ואת הקלפים שלו"""
        return f'Name of player - {self.name}. Cards of player - {self.player_deck}'