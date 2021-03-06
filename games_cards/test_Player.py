from unittest import TestCase, mock
from games_cards.Player import Player
from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCards


class TestPlayer(TestCase):
    def setUp(self):
        self.player_1 = Player("dima", 2)
        self.player_2 = Player("shahar", 27)
        self.deck_cards = DeckOfCards()
        self.card_1 = Card(1, 3)
        self.card_2 = Card(2, 1)

    @mock.patch("games_cards.DeckOfCards.DeckOfCards.deal_one", return_value=Card(2, 1))
    def test_set_hand(self, mock_1):
        """בודקת האם CARD נמצא בPLAYER_DECK"""
        card = Card(2, 1)
        self.player_1.set_hand(self.deck_cards)
        self.assertIn(card, self.player_1.player_deck)

    def test_set_hand_2(self):
        """בודקת האם בPLAYER DECK לא יהיה יותר מ26 קלפים"""
        self.player_2.set_hand(self.deck_cards)
        self.assertEqual(26, len(self.player_2.player_deck))

    def test_set_hand_3(self):
        """בודקת אם נכנס לחפיסה משהו שהוא לא אובייקט Card"""
        deck_cards = DeckOfCards()
        deck_cards.cards.append(1)  # מכניסים סתם מספר במקום אובייקט
        with self.assertRaises(SystemExit):
            self.player_1.set_hand(deck_cards)

    @mock.patch("games_cards.Player.Player.random_get_card", return_value=1)
    def test_get_card(self, mock_rand):
        """בדיקה האם פונקציה מחזירה קלף אשר נמצא במקום השני ברשימת PLAYER_DECK """
        self.player_1.player_deck = [self.card_1, self.card_2]
        self.assertIs(self.card_2, self.player_1.get_card())

    def test_add_card(self):
        """בודקת האם ADD_CARD מוסיפה CARD1"""
        self.player_1.set_hand(self.deck_cards)
        self.player_1.add_card(self.card_1)
        self.assertIn(self.card_1, self.player_1.player_deck)