from unittest import TestCase
from games_cards.Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card_1 = Card(1, 3)  # Ace:Heart
        self.card_2 = Card(5, 1)  # 5:Diamond
        self.card_3 = Card(3, 2)  # 3:Spade
        self.card_4 = Card(5, 4)  # 5:Club
        self.card_5 = Card(1, 2)  # Ace:Spade

    def test_Card_1(self):
        """בודקת האם CARD1 יותר גדול מCARD2"""
        # Ace:Heart > 5:Diamond
        self.assertGreater(self.card_1, self.card_2)

    def test_Card_2(self):
        """CARD3 אמור להיות יותר גדול מ CARD4"""
        # 5:Club > 3:Spade
        self.assertGreater(self.card_4, self.card_3)

    def test_Card_3(self):
        """CARD2 אמור להיות יותר גדול מ CARD4"""
        # 5:Club > 5:Diamond
        self.assertGreater(self.card_4, self.card_2)

    def test_Card_4(self):
        """CARD5 אמור להיות יותר גדול מ CARD1"""
        # Ace:Heart > Ace:Spade
        self.assertGreater(self.card_1, self.card_5)

    def test_Card_5(self):
        """CARD3 אמור להיות יותר גדול מ CARD4"""
        # 5:Club > 3:Spade
        self.assertGreater(self.card_4, self.card_3)

    def test_Card_Invalid(self):
        """INVALID value and/or suit"""
        with self.assertRaises(SystemExit):
            card_6 = Card(3, -50)
        with self.assertRaises(SystemExit):
            card_6 = Card(-50, 4)

    def test_Card_not_int(self):
        """Invalid value and/or suit"""
        with self.assertRaises(SystemExit):
            card = Card("123", 4334)
        with self.assertRaises(SystemExit):
            card_1 = Card("13434", "3434")
        with self.assertRaises(SystemExit):
            card_2 = Card(123, "123")