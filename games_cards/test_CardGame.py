from unittest import TestCase
from games_cards.CardGame import CardGame
from games_cards.Card import Card

class TestCardGame(TestCase):
    def setUp(self):
        self.game_test=CardGame("dima","shachar")

    def test_num_cards_not_int(self):
        """בודקת שהמערכת מציגה שגיאה כאשר כמות הקלפים לחלוקה אינו מספר תקין"""
        with self.assertRaises(SystemExit):
            self.game_test=CardGame("dima", "shachar", "bdika")

    def test_no_name_input(self):
        """בודקת האם המשחק עובד כאשר לא מזינים בכלל פרטים כולל שמות שחקנים"""
        self.game_test=CardGame()
        self.assertEqual(self.game_test.player_1.name, "player-1")
        self.assertEqual(self.game_test.player_2.name, "player-2")

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
        with self.assertRaises(SystemExit):
            self.game_test.new_game()

    def test_new_game_20(self):
        """בודקת שבאמת מחלקת את כמות הקלפים שהמשתמש ביקש"""
        self.game_test = CardGame("dima", "shachar", 20)
        self.assertEqual(len(self.game_test.player_1.player_deck),20)
        self.assertEqual(len(self.game_test.player_2.player_deck),20)

    def test_new_game_10(self):
        """בודקת שבמידה ולא הזנו מספר קלפים לחלוקה, כל שחקן יקבל 10 קלפים"""
        self.assertEqual(len(self.game_test.player_1.player_deck),10)
        self.assertEqual(len(self.game_test.player_2.player_deck),10)

    def test_new_game_0(self):
        """בודקת שמחזירה שגיאה כאשר מספר הקלפים לחלוקה הוא 0"""
        with self.assertRaises(SystemExit):
            self.game_test = CardGame("dima", "shachar", 0)

    def test_new_game_minus(self):
        """בודקת שמחזירה שגיאה כאשר מספר הקלפים לחלוקה הוא מינוס"""
        with self.assertRaises(SystemExit):
            self.game_test = CardGame("dima", "shachar", -5)

    def test_new_game_30(self):
        """בודקת מה קורה אם הזנו מעל 26 קלפים לכל אחד"""
        self.game_test = CardGame("dima", "shachar", 30)
        self.assertEqual(len(self.game_test.player_1.player_deck), 26)