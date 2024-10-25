from card import Card 

class Deck:
    def __init__(self):
       self.cards = self.create_deck()

    def create_deck(self):
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        return [Card(suit, rank) for suit in suits for rank in ranks]

    def __repr__(self):
            return f"Deck of cards: {self.cards}"