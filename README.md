# Texas Poker email version

Creater: Jun Yang  
Date   : 2020-04-07

I was playing Texas Poker one day, and felt lazy to shuffle and distribute the cards, and therefore thought of making an email version.

This program automatically shuffles the deck, and distribute the private cards to each player through email. The shared cards will be displayed as the game progress, assited by the main program.

**Disclaimer:** This program uses the python default random module for shuffling, and does not guarantee any true randomness or fairness of the game.

This program also does not replace the physical table where players all sit around, with poker chips, tasty snacks, trash talk, all the usual. That's where the fun is, isn't it?

### File Structure
**game.py**
```
|   class Game:
|       Control the overall progress of the game
```
**email_server.py**
```
|   class Server:
|       Control communication through emails
```
**poker_deck.py**
```
|   class Card:
|       Define each individual card with suit and rank
|   def display_cards(cards: List[Card]):
|       helper function to display cards
|   class Deck:
|       Define a shuffled deck
```