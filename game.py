"""A number-guessing game."""

import random

print("Welcome to the number guessing game!")

x = 1
y = 100

number = random.randint(1, 100)

def get_player_name():
    """Get player name"""

    player_name = input("What is your name?\n> ")

    return player_name

def choose_number():
    """Give instructions to pick a number."""

    print(f"{get_player_name()}, choose a number from {x} to {y}.")
    player_choice = input("> ")

    return player_choice

choose_number()

print(number)