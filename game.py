import matplotlib.pyplot as plt
from datetime import datetime
from poker_deck import Deck, display_cards

class Game:
    def __init__(self, players, server):
        self.players = players
        self.server = server
        self.num_games = 0
        
    def start_new_game(self):
        self.num_games += 1
        # Create new deck of shuffled cards
        deck = Deck()
        # Draw 2 cards for each player
        for player in self.players:
            card1 = deck.draw()
            card2 = deck.draw()
            from datetime import datetime
            subject = 'Texas Poker Game # {:d} @ {:s}'.format(self.num_games, datetime.now().strftime('%H:%M:%S'))
            self.server.send_message(player, subject, [card1, card2])
        # Game starts
        common_cards = []
        # Preflop
        if input('Preflop betting starts from person after big blind.\nGame ends? Y/N ') == 'Y':
            return
        
        # Flop
        common_cards = [deck.draw(), deck.draw(), deck.draw()]
        fig = display_cards(common_cards)
        if input('Flop betting starts from small blind.\nGame ends? Y/N ') == 'Y':
            return
        
        # Turn
        common_cards.append(deck.draw())
        plt.close(fig)
        fig = display_cards(common_cards)
        if input('Turn betting starts from small blind.\nGame ends? Y/N ') == 'Y':
            return
        
        # River
        common_cards.append(deck.draw())
        plt.close(fig)
        fig = display_cards(common_cards)
        print('River betting starts from small blind.')
        
        # End
        