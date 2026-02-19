# CS1026 Assignment 4 Blackjack
# Author: Hamza Al-Sharafi
# Student Number: 251479205
# File: Hand.py
# Date: December 4, 2025

from Card import *

class Hand:
    def __init__(self):
        # list of Card objects
        self._cards = []

    def add_card(self, card):
        # add a Card into the hand
        self._cards.append(card)

    def total(self):
        # compute total value
        total_no_aces = 0
        num_aces = 0

        for card in self._cards:
            rank = card.get_rank()
            if rank == 'A':
                num_aces += 1
            elif rank in ['J', 'Q', 'K']:
                total_no_aces += 10
            else:
                total_no_aces += int(rank)

        if num_aces == 0:
            # no aces, return a single int
            return total_no_aces

        # treat all aces as 1 for the lower value
        low = total_no_aces + num_aces
        # treat one ace as 11 and the rest as 1 for the higher value
        high = total_no_aces + 11 + (num_aces - 1)

        return (low, high)

    def __str__(self):
        if len(self._cards) == 0:
            return "Empty hand"

        card_strings = []
        for card in self._cards:
            card_strings.append(str(card))

        cards_part = "{%s}" % ", ".join(card_strings)
        return f"{cards_part}, Total: {self.total()}"
