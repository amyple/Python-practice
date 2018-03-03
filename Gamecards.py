class Card():
    suit_name = ["C", "D", "H", "S"]
    rank_name = ["0","2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def __str__(self):
        aCard = self.rank_name[self.rank] + self.suit_name[self.suit]
        return aCard

class Deck():
    def __init__(self):
        self.deck =[]
        for rank in range(1,14):
            for suit in range(4):
                card = Card(rank,suit)
                self.deck.append(card)

    def deal(self):
        return self.deck.pop() ## return the card on top
          
    def shuffle(self):
        import random
        random.shuffle(self.deck)
           
    def fan(self):
        for card in self.deck:
            print(card)

    def IsOrder(self, other): ###compare the rank then compare the suit
        if self.rank < other.rank:
            return True
        elif self.rank > other.rank:
            return False
        elif self.rank == other.rank and self.suit < other.suit:
            return True
        else:
            return False
        
    def Order(self):
        return self.deck.sort()
                       
