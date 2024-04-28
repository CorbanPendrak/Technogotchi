"""
file: BasicPet.py
author: Corban Pendrak
date: 27Apr24
purpose: Create Basic Technogotchi pet
"""
from Pet import Pet


def bread():
    print("Your pet quickly swallows the tasty fish.")
    return {"happiness": 2, "food": 3}


class BasicPet(Pet):
    """
    This is the basic pet class.

    Attributes:
    -

    Methods:
    -
    """
    def __init__(self):
        super().__init__()
        self.type = "Basic Pet"

        with open("basic-pet-image.txt", "r") as file:
            self.image = file.readlines()

        self.recipes = (0, "Bread", bread)
