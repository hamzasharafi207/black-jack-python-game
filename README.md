Blackjack Game – Object-Oriented Python

A console-based Blackjack game built in Python using object-oriented programming principles.
This project simulates a full player vs dealer Blackjack experience with proper game rules and modular class design.

Overview

This implementation models a real deck of cards and separates game logic into structured components. The game runs in the terminal and follows standard Blackjack rules, including dealer drawing behavior and Ace value handling.

Project Structure

Card.py
Defines the Card class representing an individual playing card.

Deck.py
Creates and manages a 52-card deck, including shuffling and dealing functionality.

Hand.py
Represents a player's or dealer's hand and calculates total value with dynamic Ace adjustment (1 or 11).

Game.py
Controls overall gameplay, player decisions, and win/loss logic.

Features

Full 52-card deck simulation

Randomized shuffling

Player vs dealer gameplay

Dealer logic (hits until rule threshold)

Automatic Ace value adjustment

Modular, class-based architecture

Concepts Demonstrated

Object-Oriented Programming (OOP)

Class design and modular code structure

Encapsulation of game logic

Control flow (loops and conditionals)

Random module usage

How to Run

Ensure all four files are in the same directory.

Run the following command in the terminal:

python Game.py


The game will launch in the console.

Author

Hamza Al-Sharafi
Computer Science Student @ Western University