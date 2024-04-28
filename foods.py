"""
file: foods.py
author: Corban Pendrak
date: 27Apr24
purpose: Create food functions for all pets
"""


def water():
    print("Your pet drinks some water.")
    return {"water": 3}


def candy():
    print("Your pet eats some tasty candy!")
    return {"happiness": 4, "food": 1}


def levelup_cake():
    print("Your pet really likes this cake!")
    return {"happiness": 5, "level": 2}


# List of available food items formatted with (level_available, name)
food_items = [(0, "Water", water), (5, "Candy", candy), (0, "Levelup", levelup_cake)]
