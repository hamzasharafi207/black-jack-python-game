# Author: Hamza Al-Sharafi
# File: Card.py

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suit

    def __str__(self):
        # Example: Ace of spades -> "AS"
        return str(self._rank) + self._suit[0].upper()

    def __eq__(self, other):
        return isinstance(other, Card) and \
               self._rank == other._rank and \
               self._suit == other._suit
