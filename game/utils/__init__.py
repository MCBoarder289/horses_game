import random


def roll_dice() -> (int, int):
    return random.randint(1, 6), random.randint(1, 6)
