"""
file: TerminalInteraction.py
author: Corban Pendrak
date: 27Apr24
purpose: Implement interaction for Technogotchi via terminal interface
"""
from AbstractInteraction import AbstractInteraction
from Pet import Pet


def print_menu(options: list, input_prompt:str="Choice: ") -> str:
    """
    Prints the list formatted as a menu, accepts user input as number
    or case-sensitive match, and returns option.

    :param options: List of options for menu
    :param input_prompt: Input prompt for user
    :return: Option chosen by user
    """

    for index, choice in enumerate(options):
        print(f"\t{index + 1}. {choice}")
    print()

    while True:
        user_choice = input(input_prompt + " ")

        if user_choice in options:
            return user_choice
        elif user_choice.isnumeric() and 1 <= int(user_choice) <= len(choice):
            return options[int(user_choice) - 1]
        else:
            print("Please enter a valid option!")


class TerminalInteraction(AbstractInteraction):
    """
    This class implments a terminal interaction with the Technogotchi
    """
    def __init__(self, pet_types: dict):
        self.pet_types = pet_types

        self.pet: Pet = self.create_pet()
        self.main()

    def create_pet(self):
        print("Let's create a new pet!")
        print("Available pets:")
        available_pets = list(self.pet_types.keys())
        return self.pet_types[print_menu(available_pets, "Pet type:")]()

    def main(self):
        print()
        while True:
            self.pet.print_box()

            options = ["Play", "Feed", "Display stats", "Quit"]

            user_choice = print_menu(options, "What do you want to do?")
            print()

            match user_choice:
                case "Play":
                    self.play()
                case "Feed":
                    self.feed()
                case "Display stats":
                    self.display_stats()
                case "Quit":
                    print("Thank you for playing!")
                    return
                case _:
                    print("Sorry! Please choose from the menu")

    def play(self):
        print("Your pet loves you!\n")

    def feed(self):
        foods = self.pet.recipes
        print("Available food items:")
        food_choice = print_menu([food[1] for food in foods])
        food_method = next(food[2] for food in foods if food[1] == food_choice)
        self.pet.update_dict(food_method())
        print()

    def display_stats(self):
        print("Your pet's stats:")
        print(self.pet)
        print()
