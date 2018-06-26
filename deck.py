from card import *
from random import shuffle

class Deck:
    def __init__(self):
        suits = ("Spades", "Hearts", "Clubs", "Diamonds")
        cardList = []
        for suit in suits:
            for rank in range(1,14):
                cardList.append(Card(rank, suit))

        self.cardList = cardList

    def shuffleDeck(self):
        for i in range(0, 5): # shuffle multiple times to improve randomness
            shuffle(self.cardList)

    def draw(self):
        return self.cardList.pop()

    def printDeck(self):
        for card in self.cardList:
            print(str(card))
