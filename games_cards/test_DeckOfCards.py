from unittest.mock import patch
from unittest import TestCase
from games_cards.Card import Card
from games_cards.DeckOfCards import DeckOfCard


class TestDeckOfCard(TestCase):
    def setUp(self):
        self.tester=DeckOfCard()

    def test_sum_cards(self):
        """בודקת האם בחפיסה חדשה שנוצרת יש 52 קלפים"""
        deck1 = DeckOfCard()
        self.assertEqual(len(deck1.cards),52)

    def test_shuffle(self):
        """בודקת האם החפיסה לפני הערבוב שווה לחפיסה חדשה, ובודקת האם החפיסה אחרי הערבוב לא שווה לחפיסה חדשה לפני ערבוב"""
        deck1=DeckOfCard()
        self.assertEqual(deck1.cards, self.tester.show())
        self.tester.shuffle()
        self.assertNotEqual(deck1.cards, self.tester.show())

    # @mock.patch("random.randint", return_value=1)
    def test_deal_one1(self):
        with patch("random.randint") as mock1:
            mock1.return_value=1
        """לא עובד המוק עדיין"""
        c=self.tester.cards[1]
        b=self.tester.deal_one()
        print(c, b)
        self.assertEqual(b,c)

    def test_deal_one2(self):
        """בודקת לי האם הקלף שהוצאתי כבר לא נמצא בחפיסה"""
        a=self.tester.deal_one()
        self.assertNotIn(a, self.tester.show())

    def test_deal_one3(self):
        """בודק לי האם החפיסה ירדה בכמות באחד אחרי שהוצאתי קלף"""
        len1=len(self.tester.show())
        self.tester.deal_one()
        len2=len(self.tester.show())
        self.assertEqual(len1-1, len2)


    def test_show(self):
        """בודקת האם הקלף הספיציפי נמצא בתוך חפיסת הקלפים"""
        self.card1 = Card(1, 1)
        self.assertIn(self.card1, self.tester.show())
