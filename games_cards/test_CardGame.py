from unittest import TestCase
from games_cards.CardGame import CardGame
from games_cards.Card import Card
from sys import exit


class TestCardGame(TestCase):
    def setUp(self):
        self.game_test=CardGame("dima","shachar")

    def test_get_winner(self):
        """בודקת כאשר יש לשחקן השני פחות קלפים שהשם שלו חוזר"""
        card1 = Card(1, 1)
        card2 = Card(2, 2)
        card3 = Card(3, 5)
        self.game_test.player_1.player_deck = [card1, card2]
        self.game_test.player_2.player_deck = [card3]
        self.assertIn("shachar", self.game_test.get_winner())
        # self.assertIn(self.game_test.player_2.name, self.game_test.get_winner())

    def test_get_winner_none(self):
        """בודקת במידה והרשימות של שני השחקנים באותו אורך שהיא מחזירה none"""
        card1 = Card(1, 1)
        card2 = Card(2, 2)
        card3 = Card(3, 5)
        card4 = Card(3, 7)
        self.game_test.player_1.player_deck = [card1, card2]
        self.game_test.player_2.player_deck = [card3, card4]
        self.assertIsNone(self.game_test.get_winner())

    def test_new_game(self):
        """בודקת שבמידה והפונקציה לא הופעלה מהקונסטרקטור היא מחזירה שגיאה"""
        # self.assertRaises(self.game_test.new_game(), "Error")
        # self.assertIn(self.game_test.new_game(), "Error")
        with self.assertRaises(SystemExit):
            self.game_test.new_game()

    def test_new_game_10(self):
        """בודקת שבמידה ולא הזנו מספר קלפים לחלוקה, כל שחקן יקבל 10 קלפים"""
        self.assertEqual(len(self.game_test.player_1.player_deck),10)
        self.assertEqual(len(self.game_test.player_2.player_deck),10)

    def text_new_game_0(self):
        """בודקת מה קורה אם הזנו 0 במספר הקלפים לחלוקה"""
        self.game_test = CardGame("dima", "shachar", 0)
        self.assertEqual(len(self.game_test.player_1.player_deck), 0)
        #  צריכה לתת שגיאה שחייבים לחלק כמות מסויימת

    def text_new_game_30(self):
        """בודקת מה קורה אם הזנו מעל 26 קלפים לכל אחד"""
        self.game_test = CardGame("dima", "shachar", 30)
        self.assertEqual(len(self.game_test.player_1.player_deck), 26)
        #  צריכה לתת הערה ואז לחלק 26

