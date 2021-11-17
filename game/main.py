import random
import utils
from models import Horse, Player, Game

# Initialize Game
horses = [Horse(number=i) for i in range(2, 13)]

# TODO: Shuffle player order somehow
players = [
    Player("Player 1", starting_amount=80),
    Player("Player 2", starting_amount=80)
]

game = Game(players=players, horses=horses)

# elimination round
while game.is_elimination_round:
    # TODO: Keep track of whose turn it is
    for player in players:
        die_1, die_2 = utils.roll_dice()
        roll = die_1 + die_2
        game.elimination_round_roll(player=player, roll=roll)
        # Break to ensure that we don't keep running eliminate rolls
        # TODO: Handle this better
        if game.is_racing_round:
            break





