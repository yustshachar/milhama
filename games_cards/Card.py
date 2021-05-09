from sys import exit


class Card:
    def __init__(self, value, suit):
        if type(value) != int or type(
                suit) != int or value < 1 or value > 13 or suit < 1 or suit > 4:  # בודקת שמספרי הקלף הם מספר שלם ושהם תקינים מבחינת מספר הסוג והערך
            exit("ERROR!")
        else:
            self.value = value
            self.suit = suit
            self.suits = {1: "Diamond", 2: "Spade", 3: "Heart", 4: "Club"}  # מתרגם את הספרות לשם של סוג הקלף
            self.values = {1: "Ace", 2: "2", 3: "3", 4: '4', 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10",
                           11: "Jack", 12: "Queen", 13: "King"}  # מתרגם את הספרות למספר הקלף

    def __repr__(self):
        """הפונקציה מחזירה את השם של הקלף שהמשתמש רואה לעומת הקוד של הקלף"""
        return f'{self.values[self.value]} {self.suits[self.suit]}'

    def __gt__(self, other):
        """מגדירה איך לבדוק האם קלף אחד יותר גדול מקלף שני (אס הקלף הכי חזק, ואם הם שווים אז לפי הסוג של הקלף)"""
        if self.value > other.value:
            if other.value == 1:
                return False
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        elif self.value == 1:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False
