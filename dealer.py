from participant import Participant
from deck import Deck
import random

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.deck = Deck() 

    def deck_shuffle(self):
        random.shuffle(self.deck.cards)
    
    def deal_card(self):
        if self.deck:
            return self.deck.cards.pop()
        return None

    def hide_card(self):
        if self.cards[0].rank in ["Jack", "Queen", "King"] and self.cards[1].rank != "Ace":
            self.cards[1].hidden = True
        elif self.cards[0].rank not in ["Jack", "Queen", "King"]: 
            self.cards[1].hidden = True

    def show_hands(self):
        cards = [self.cards[0], "hidden" if self.cards[1].hidden == True else self.cards[1]]  
        return cards
   