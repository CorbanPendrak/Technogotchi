"""
file: Pet.py
author: Corban Pendrak
date: 25Apr25
purpose: Create the basic pet functionality for Technogotchi
"""


def describe_attribute(attribute):
    if attribute <= 3:
        return "not"
    elif attribute <= 7:
        return "somewhat"
    else:
        return "very"


class Pet:
    """
    This is the underlying pet class for the Technogotchi.

    Attributes:
    - age (int): Age of pet in days.
    - happiness (int): Happiness of pet
    - food (int): Food supply of pet
    - water (int): Water supply of pet
    - clean (int): Cleanliness of pet
    - mistakes (int): Mistakes in care of pet
    - level (int): Level of pet
    - food (list(list(level, food_name))): List of foods
    - games (list(list(level, game_name))): List of games
    - type (str): Type of pet (set to empty)
    - image (str): Pet Image (set to empty)

    Magic Methods:
    - Property values for each attribute
    - Setter methods for each attribute
    - String representation of class
    - Programming representation of class
    - Comparison between class instances

    Methods
    -

    """
    def __init__(self):
        self.__age = 0
        self.__happiness = 0
        self.__food = 0
        self.__water = 0
        self.__clean = 0
        self.__mistakes = 0
        self.__level = 0

        # Should be overwritten in new pets
        self.type = ""
        self.image = ""

        # Can be overwritten in new pets
        self.age_levelup = [4, 8] # when pet levels up based on age
        self.age_levelup_advanced = 5 # when pet levels up after passing final age_levelup

    def __str__(self):
        return (f"Basic Technogotchi {self.__age} days old, "
                f"{describe_attribute(self.__happiness)} happy, "
                f"{describe_attribute(self.__food)} fed, "
                f"{describe_attribute(self.__water)} hydrated, "
                f"{describe_attribute(self.__clean)} clean, "
                f"{describe_attribute(self.__mistakes)} mistakes, "
                f"level {self.__level}.")

    def __repr__(self):
        return (f"{type(self).__name__}(age={self.__age}, happiness={self.__happiness}, "
                f"food={self.__food}, water={self.__water}, clean={self.__clean}, "
                f"mistakes={self.__mistakes}, level={self.__level})")

    # Age property
    @property
    def age(self):
        return self.__age

    # Age setter property
    @age.setter
    def age(self, age):
        self.__age = age

        if age > self.age_levelup[-1]:
            # Age is beyond custom levels
            self.level = len(self.age_levelup) + (age - self.age_levelup[-1]) % self.age_levelup_advanced
        else:
            # Age is within custom levels
            for index, age_levelup in enumerate(self.age_levelup):
                if age < age_levelup:
                    self.level = index

        # Happiness property
    @property
    def happiness(self):
        return self.__happiness

        # Happiness setter property
    @happiness.setter
    def happiness(self, happiness):
        self.__happiness = happiness

    @property
    def food(self):
        return self.__food

    @food.setter
    def food(self, food):
        self.__food = food

    @property
    def water(self):
        return self.__water

    @water.setter
    def water(self, water):
        self.__water = water

    @property
    def clean(self):
        return self.__clean

    @clean.setter
    def clean(self, clean):
        self.__clean = clean

    @property
    def mistakes(self):
        return self.__mistakes

    @mistakes.setter
    def mistakes(self, mistakes):
        self.__mistakes = mistakes

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    def print_box(self):
        image_width = max([len(line) for line in self.image])
        print("-" * (image_width + 5))
        for line in self.image:
            print("|", line.replace("\n", " "), " " * (image_width - len(line)), "|")
        print("-" * (image_width + 5))


if __name__ == "__main__":
    pet1 = Pet()
    print("Pet:\n")
    print(pet1)

    print("Pet age set to 14:")
    pet1.age = 14
    print(pet1)