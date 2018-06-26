class Card:
    def __init__(self, rank, suit):
        
        # check to see if card is legal
        suits = ("Spades", "Hearts", "Clubs", "Diamonds")
        if rank not in range(1, 14):
            raise TypeError("Rank must be an integer value between 1 and 13")
        if suit not in suits:
            raise TypeError("Suit must be found in suits")

        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Returns a string containing the card's name
        """
        if self.rank == 1:
            rankName = "Ace"
        elif self.rank == 11:
            rankName = "Jack"
        elif self.rank == 12:
            rankName = "Queen"
        elif self.rank == 13:
            rankName = "King"
        else:
            rankName = str(self.rank)

        return "{rank} of {suit}".format(rank = rankName, suit = self.suit)
    
