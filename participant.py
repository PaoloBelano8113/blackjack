class Participant:
    def __init__(self):
        self.cards = []
        self.count = 0

    def dealt_cards(self,card):
        self.cards.append(card)

    def show_hands(self):
        return self.cards

    def count_hands(self):
        count = 0
        for card in self.cards:
            if card.hidden:
                continue
            elif card.rank.isdigit():
                count += int(card.rank)  
            else:
                if card.rank in ["Jack", "Queen", "King"]:
                    count += 10
                elif card.rank == "Ace":
                    if count + 11 > 21:
                        count += 1
                    else:
                        count += 11
        self.count = count
        return self.count