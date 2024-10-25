class Card:
    def __init__(self, suit, rank, hidden = False):
        self.suit = suit
        self.rank = rank
        self.hidden = hidden

    def __repr__(self):
        return f"{self.rank} of {self.suit}" if not self.hidden else "hidden"
    