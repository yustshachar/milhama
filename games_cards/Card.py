from sys import exit

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.suits={1:"Diamond", 2:"Spade", 3:"Heart", 4:"Club"}
        self.values={1:"Ace",2:"2",3:"3",4:'4',5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"Jack", 12:"Queen", 13:"King"}

    def __repr__(self):
        """הפונקציה מחזירה את השם של הקלף שהמשתמש רואה לעומת הקוד של הקלף"""
        return f'{self.values[self.value]} {self.suits[self.suit]}'

    def __gt__(self, other):
        """מגדירה איך לבדוק האם קלף אחד יותר גדול מקלף שני (אס הקלף הכי חזק, ואם הם שווים אז לפי הסוג של הקלף)"""
        if type(self.value) != int or type(self.suit) != int or type(other.value) != int or type(other.suit) != int:
            exit("ERROR")
        else:
            while self.value < 1 or self.value > 13 or self.suit < 1 or self.suit > 4 or other.value < 1 or other.value > 13 or other.suit < 1 or other.suit > 4:
                exit("ERROR")
            else:
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