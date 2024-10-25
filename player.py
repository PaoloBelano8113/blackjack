from participant import Participant

class Player(Participant):
    def __init__(self,name,bankroll):
        super().__init__()
        self.name = name
        self.bankroll = bankroll
        self.bet = 0
