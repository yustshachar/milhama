from unittest import TestCase
from games_cards.Card import Card

class TestCard(TestCase):
    def setUp(self):
        self.card_1 = Card(1, 3)  # Ace:Heart
        self.card_2 = Card(5, 1)  # 5:Diamond
        self.card_3 = Card(3, 2)  # 3:Spade
        self.card_4 = Card(5, 4)  # 5:Club
        self.card_5 = Card(1, 2)  # Ace:Spade
        self.card_6 = Card(100, -50)  # INVALID

    def test_Card_1(self):
        """בודקת האם CARD1 יותר גדול מCARD2"""
        self.assertGreater(self.card_1, self.card_2)

    def test_Card_2(self):
        """CARD3 אמור להיות יותר גדול מ CARD4"""
        self.assertGreater(self.card_4, self.card_3)

    def test_Card_3(self):
        """CARD2 אמור להיות יותר גדול מ CARD4"""
        self.assertGreater(self.card_4, self.card_2)

    def test_Card_4(self):
        """CARD5 אמור להיות יותר גדול מ CARD1"""
        self.assertGreater(self.card_1, self.card_5)

    def test_Card_5(self):
        """CARD3 אמור להיות יותר קטו מ CARD4"""
        self.assertGreater(self.card_4, self.card_3)

    def test_Card_6(self):
        """INVALID value and/or  suit"""
        with self.assertRaises(SystemExit):
            self.card_6.__gt__(self.card_3)
        with self.assertRaises(SystemExit):
            self.card_3.__gt__(self.card_6)

    def test_Card_7(self):
        """Invalid value and/or suit"""
        with self.assertRaises(SystemExit):
            card = Card("123", 4334)
        with self.assertRaises(SystemExit):
            card_1 = Card("13434", "3434")
        with self.assertRaises(SystemExit):
            card_2 = Card(123, "123")