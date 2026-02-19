# Author: Hamza Al-Sharafi
# File: Deck.py

from Card import *
import random

# deck holds all Card objects
class Deck:
    def __init__(self, num_decks):
        # only instance variable as required
        self._cards = []

        suits = ["clubs", "diamonds", "hearts", "spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K"]

        # build decks in required order
        for d in range(num_decks):
            for suit in suits:
                for rank in ranks:
                    self._cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self._cards)

    def draw_card(self):
        # remove and return top card, or None if empty
        if len(self._cards) == 0:
            return None
        return self._cards.pop(0)
