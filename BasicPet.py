"""
file: BasicPet.py
author: Corban Pendrak
date: 27Apr24
purpose: Create Basic Technogotchi pet
"""
from Pet import Pet


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
