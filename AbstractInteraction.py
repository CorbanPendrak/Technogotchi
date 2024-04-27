"""
file: AbstractInteraction.py
author: Corban Pendrak
date: 27Apr24
purpose: The abstract class for interactions.
"""
import abc


class AbstractInteraction(metaclass=abc.ABCMeta):
    """
    This class should not be implemented directly but inherited from.

    Attributes:
    - Pet: Technogotchi pet

    Methods:
    - create_pet: creates a new Pet
    - main: main interaction method
    - play: Play with pet
    - feed: Feed pet

    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'main') and
                hasattr(subclass, 'play') and
                hasattr(subclass, 'feed') or
                NotImplemented)

    @abc.abstractmethod
    def main(self):
        """
        Main interaction method.
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def play(self):
        """
        Play with pet.
        :return: None
        """
        raise NotImplementedError

    @abc.abstractmethod
    def feed(self):
        """
        Feed pet.
        :return: None
        """
        raise NotImplementedError
