"""
file: games.py
author: Corban Pendrak
date: 27Apr24
purpose: Create games available for all pets
"""
import random


def math_game(pet):
    print("Let's play a math game!")
    rounds = 3
    score = 0

    for i in range(rounds):
        print(f"Round {i+1} / {rounds}:")
        base = 10 ** pet.level
        num1 = random.randint(base, base * 2)
        num2 = random.randint(base, base * 2)

        user_guess = input(f"\t{num1} + {num2} = ")

        if user_guess.isnumeric and int(user_guess) == num1 + num2:
            print("\nCorrect!")
            score += 1
        else:
            print("\nIncorrect!")

    print(f"\nYou got scored {score} / {rounds} rounds!")
    return {"happiness": 2 + score + pet.level // 2}


# List of available games formatted with (level_available, name, method)
game_items = [(0, "Math Game", math_game),]
