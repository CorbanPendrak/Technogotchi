"""
file: main.py
author: Corban Pendrak
date: 25Apr25
purpose: Run Technogotchi interactive digital pet
"""
from BasicPet import BasicPet
from TerminalInteraction import TerminalInteraction

pet_types = {"Basic": BasicPet}
interaction = TerminalInteraction(pet_types)

