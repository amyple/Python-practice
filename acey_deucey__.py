###Acey-Deucey card game, based on https://en.wikipedia.org/wiki/Acey_Deucey_(card_game)

from Deck import *

def acey_deucey():
    deck = Deck()
    deck.shuffle()

    pocket = 0 #the player's pocket
    while True:
        card1 = deck.deal()
        card2 = deck.deal()
        print("The two cards:", card1,card2)

        if card1.rank > card2.rank:
            card1, card2 = card2, card1
        else:
            card1, card2 = card1, card2
        
        bet = int(input('Enter the amount that you bet:'))

        card3 = deck.deal()
        print("The next card is", card3)
              
        if card3.rank > card1.rank and card3.rank < card2.rank:
            print("You win")
            pocket = pocket + bet
            print(pocket)
        elif card3.rank < card1.rank or card3.rank > card2.rank:
            print("You lose")
            pocket = pocket - bet
            print(pocket)
        elif card3.rank == card1.rank or card3.rank ==card2.rank:
            print("You lose")
            pocket = pocket - bet*2
            print(pocket)
        elif card3.rank == card1.rank and card3.rank ==card2.rank:
            bet = bet*3
            print("You have to bet:", bet)

acey_deucey()
    
    
