from dealer import Dealer
from player import Player

class BlackJack:
    def __init__(self,dealer,players,min_bet,max_bet):
        self.dealer = dealer
        self.players = players
        self.minimum_bet = min_bet
        self.maximum_bet = max_bet
    
    def start_game(self):
        self.initial_betting_phase()
        self.dealer_phase()
        self.player_phase()

    def initial_betting_phase(self):
        for player in self.players:
            print(f"House rule: Minimum bet is ${self.minimum_bet} Maximum bet is ${self.maximum_bet}")
            print(f"{player.name}: You have a total bankroll of ${player.bankroll}")
            
            while True:
                try:
                    player.bet = float(input("Place bet within the range: $"))
                    if (self.minimum_bet <= player.bet <= self.maximum_bet) and (player.bet <= player.bankroll):
                        player.bankroll -= player.bet 
                        print(f"{player.name} has placed a bet of ${player.bet}. Remaining bankroll: ${player.bankroll}.\n")
                        break  
                    else:
                        print(f"Invalid bet! Your bet must be between ${self.minimum_bet} and ${self.maximum_bet} and cannot exceed your bankroll of ${player.bankroll}.")
                except ValueError:
                    print("Please enter a valid number for your bet.")

    def dealer_phase(self):
        self.dealer.deck_shuffle()
        self.initial_dealing_of_cards()
        self.show_cards()
        
    def initial_dealing_of_cards(self):
        for _ in range(2):
            for player in self.players:
                player.dealt_cards(self.dealer.deal_card())
            self.dealer.dealt_cards(self.dealer.deal_card())
        self.dealer.hide_card()

    def show_cards(self):
        print(f"Dealer: {self.dealer.show_hands()} Count: {self.dealer.count_hands()}")
        for player in self.players:
            print(f"{player.name}: {player.show_hands()}  Count: {player.count_hands()}")

    def player_phase(self):
        for player in self.players:
            end_turn = False
            print(f"\nDealer: {self.dealer.show_hands()} Count: {self.dealer.count_hands()}")
            print(f"{player.name}'s turn Current hand:  {player.show_hands()}  Count: {player.count_hands()}")
            while (end_turn == False):
                print("\nChoose your move: \n 1. Hit \n 2. Stand \n 3. Double Down")
                choice = input("Enter your move (1 for Hit, 2 for Stand, 3 for Double): ")

                if choice == "1":
                    end_turn = self.player_hit(player)
                elif choice == "2":
                    end_turn = self.player_stand(player)
                elif choice == "3":
                    end_turn = self.player_double(player)
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
                end_turn = self.check_cards(player)


    def player_hit(self,player):
        player.dealt_cards(self.dealer.deal_card())
        print(f"\nDealer: {self.dealer.show_hands()} Count: {self.dealer.count_hands()}")
        print(f"{player.name}: {player.show_hands()}  Count: {player.count_hands()}")
        print(f"{player.name} bet is ${player.bet}. Remaining bankroll: ${player.bankroll}.")
    
    def player_stand(self,player):
        print(f"\nDealer: {self.dealer.show_hands()} Count: {self.dealer.count_hands()}")
        print(f"{player.name}: {player.show_hands()}  Count: {player.count_hands()}")
        print(f"{player.name} bet is ${player.bet}. Remaining bankroll: ${player.bankroll}.")
        return True

    def player_double(self,player):
        if player.bet * 2 <= player.bankroll:
            player.dealt_cards(self.dealer.deal_card())
            player.bankroll -= player.bet
            player.bet *= 2
            print(f"\nDealer: {self.dealer.show_hands()} Count: {self.dealer.count_hands()}")
            print(f"{player.name}: {player.show_hands()}  Count: {player.count_hands()}")
            print(f"{player.name} bet is ${player.bet}. Remaining bankroll: ${player.bankroll}.")
            return True
        else:
            print(f"{player.name} bet is ${player.bet}. Remaining bankroll: ${player.bankroll}.")
            print(f"You cannot double down. Your bankroll is only ${player.bankroll}. Please choose another action.")

    def check_cards(self,player):
        if (player.count == 21):
            print("You got a BlackJack")
            return True
        elif (player.count > 21):
            print("You got a Bust")
            return True




dealer = Dealer()
players = [Player("Player 1",1000)]
game = BlackJack(dealer, players,5,1000)
game.start_game()

    
