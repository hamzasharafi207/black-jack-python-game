# CS1026 Assignment 4 Blackjack
# Author: Hamza Al-Sharafi
# Student Number: 251479205
# File: Game.py
# Date: December 4, 2025

from Deck import *
from Hand import *

class Game:
    def __init__(self, num_decks=1):
        self._deck = Deck(num_decks)
        self._deck.shuffle()

        self._player_hand = Hand()
        self._comp_hand = Hand()

        self._player_active = False
        self._comp_active = False

        # list of tuples like (winner, player_final, comp_final)
        self._results = []

    def play(self):
        # main game loop
        while True:
            self.play_round()
            again = input("Do you want to play again? (yes/no): ").lower()
            if again == "no":
                break

        # ask for filename
        filename = input("Enter filename (ending in .txt) for the game results: ")
        while not filename.endswith(".txt"):
            filename = input("Enter filename (ending in .txt) for the game results: ")
        self.output_game_results(filename)

    def _best_value(self, total):
        # convert Hand.total() result into a single best value or -1 for bust
        if isinstance(total, tuple):
            low, high = total
        else:
            low = total
            high = total

        if high <= 21:
            return high
        if low <= 21:
            return low
        # bust
        return -1

    def play_round(self):
        # reset hands
        self._player_hand = Hand()
        self._comp_hand = Hand()

        # deal 2 cards each, alternating
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())
        self._player_hand.add_card(self._deck.draw_card())
        self._comp_hand.add_card(self._deck.draw_card())

        self._player_active = True
        self._comp_active = True

        # show initial hands
        print("Player:", self._player_hand)
        print("Computer:", self._comp_hand)

        # turns
        while self._player_active or self._comp_active:
            # player turn
            if self._player_active:
                print("What do you want to do? Type 'hit' for another card or 'stand' if you are done.")
                choice = input().lower()

                if choice == "hit":
                    self._player_hand.add_card(self._deck.draw_card())
                elif choice == "stand":
                    self._player_active = False

                # check bust
                player_best = self._best_value(self._player_hand.total())
                if player_best == -1:
                    self._player_active = False

                print("Player:", self._player_hand)
                print("Computer:", self._comp_hand)

            # computer turn
            if self._comp_active:
                print("Determine what computer will do (hit/stand)")

                comp_total = self._comp_hand.total()
                if isinstance(comp_total, tuple):
                    low, high = comp_total
                else:
                    low = comp_total
                    high = comp_total

                # decide hit or stand
                if high == 21:
                    decision = "stand"
                elif low < 17:
                    decision = "hit"
                else:
                    decision = "stand"

                print(decision)

                if decision == "hit":
                    self._comp_hand.add_card(self._deck.draw_card())

                comp_best = self._best_value(self._comp_hand.total())
                if comp_best == -1 or decision == "stand":
                    # bust or stand ends computer activity
                    self._comp_active = False

                print("Player:", self._player_hand)
                print("Computer:", self._comp_hand)

        # decide winner after round
        player_best = self._best_value(self._player_hand.total())
        comp_best = self._best_value(self._comp_hand.total())

        if player_best == -1 and comp_best == -1:
            winner = "Neither"
        elif player_best != -1 and comp_best != -1 and player_best == comp_best:
            winner = "Draw"
        elif player_best != -1 and (comp_best == -1 or player_best > comp_best):
            winner = "Player"
        else:
            winner = "Computer"

        print(f"The round has ended. Winner: {winner}")

        # store results, keep -1 for busts
        self._results.append((winner, player_best, comp_best))

    def output_game_results(self, filename):
        with open(filename, "w") as f:
            for i, (winner, player_val, comp_val) in enumerate(self._results, start=1):
                f.write(f"Round {i}\n")

                if player_val == -1:
                    f.write("Player: bust\n")
                else:
                    f.write(f"Player: {player_val}\n")

                if comp_val == -1:
                    f.write("Computer: bust\n")
                else:
                    f.write(f"Computer: {comp_val}\n")

                f.write(f"Winner: {winner}\n\n")