from unittest.mock import patch
from unittest import TestCase
from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCards


class TestDeckOfCard(TestCase):
    def setUp(self):
        self.tester = DeckOfCards()

    def test_sum_cards(self):
        """בודקת האם בחפיסה חדשה שנוצרת יש 52 קלפים"""
        deck1 = DeckOfCards()
        self.assertEqual(len(deck1.cards), 52)

    def test_shuffle(self):
        """בודקת האם החפיסה לפני הערבוב שווה לחפיסה חדשה, ובודקת האם החפיסה אחרי הערבוב לא שווה לחפיסה חדשה לפני ערבוב"""
        deck1 = DeckOfCards()
        self.assertEqual(deck1.cards, self.tester.show())
        self.tester.shuffle()
        self.assertNotEqual(deck1.cards, self.tester.show())

    @patch("games_cards.DeckOfCards.DeckOfCards.random_for_deal_one", return_value=1)
    def test_deal_one1(self, mock_rand):
        """בודקת אם הפונקציה מחזירה לי בהגרלה את אינדקס 1 האם זה באמת אותו קלף"""
        c = self.tester.cards[1]
        b = self.tester.deal_one()
        print(c, b)
        self.assertEqual(b, c)

    def test_deal_one2(self):
        """בודקת לי האם הקלף שהוצאתי כבר לא נמצא בחפיסה"""
        a = self.tester.deal_one()
        self.assertNotIn(a, self.tester.show())

    def test_deal_one3(self):
        """בודק לי האם החפיסה ירדה בכמות באחד אחרי שהוצאתי קלף"""
        len1 = len(self.tester.show())
        self.tester.deal_one()
        len2 = len(self.tester.show())
        self.assertEqual(len1 - 1, len2)

    def test_show(self):
        """בודקת האם הקלף הספיציפי נמצא בתוך חפיסת הקלפים"""
        self.card1 = Card(1, 1)
        self.assertIn(self.card1, self.tester.show())
