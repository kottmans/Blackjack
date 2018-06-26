from card import *

class Player:
    def __init__(self):

        self.money = 2000
        self.wins = 0
        self.losses = 0
        self.currentHand = []

    def getHandValue(self):
        total = 0
        for card in self.currentHand:
            total += card.rank

        return total

    def addMoney(self, amountToAdd):
        self.money = self.money + amountToAdd

    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1

    def addCard(self, card):
        self.currentHand.append(card)

    def resetHand(self):
        self.currentHand = []

    def resetRecords(self):
        self.money = 2000
        self.wins = 0
        self.losses = 0
