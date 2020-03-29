import random
from typing import List
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Card:
    def __init__(self, rank, suit):
        """
        Define a single card
        @ Parameters
        |   rank : can be in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        |   suit : can be in ['S', 'H', 'C', 'D']
        """
        self.rank = rank
        self.suit = suit
        self.image_link = 'pic/{}{}.png'.format(self.rank, self.suit)

    def __repr__(self):
        uni = {'S': '♠', 'H': '♥', 'C': '♣', 'D': '♦'}
        return self.rank + uni[self.suit]
    
    def show_image(self, fig=None, ax=None):
        if fig is None:
            fig, ax = plt.subplots(figsize=(4, 6))
        ax.imshow(mpimg.imread(self.image_link))
        ax.set_axis_off()

def display_cards(cards: List[Card]):
    if len(cards) == 1:
        fig, ax = plt.subplots(figsize=(4, 6))
        cards[0].show_image(fig, ax)
    else:
        fig, ax = plt.subplots(ncols=len(cards), figsize=(len(cards)*4, 6))
        for i, card in enumerate(cards):
            card.show_image(fig, ax[i])
    fig.canvas.draw()
    fig.canvas.flush_events()
    
class Deck:    
    def __init__(self):
        RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        SUITS = ['S', 'H', 'C', 'D']
        self.deck = [Card(r, s) for r in RANKS for s in SUITS]
        random.shuffle(self.deck)
        
    def draw(self):
        return self.deck.pop()

    def show(self):
        print(self.deck)
        
        