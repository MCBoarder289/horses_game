from typing import List


class Player:
    def __init__(self,
                 name: str,
                 starting_amount: int):
        self.name: str = name
        self.hand: List[int] = []
        self.wallet = starting_amount
        self.is_dealer = False


class Horse:
    def __init__(self, number: int):
        self.number = number
        self.is_racing = True
        self.is_winner = False
        self.penalty_price = 0
        self.winning_count = get_winning_count(number)

    def set_penalty_price(self, penalty: int):
        self.penalty_price = penalty

    def move_forward(self):
        self.winning_count -= 1
        if self.winning_count == 0:
            self.is_winner = True

    def reset_status(self):
        self.is_racing = True
        self.is_winner = False
        self.penalty_price = 0
        self.winning_count = get_winning_count(self.number)


def get_winning_count(number: int):
    if number == 2 or number == 12:
        return 2
    if number == 3 or number == 11:
        return 3
    if number == 4 or number == 10:
        return 4
    if number == 5 or number == 9:
        return 5
    if number == 6 or number == 8:
        return 6
    if number == 7:
        return 7
    else:
        raise ValueError(f"Must only use horse numbers 2-12. Attempted {number}")


class Game:
    def __init__(self, players: List[Player], horses: List[Horse], turns_per_player: int = 5):
        self.players = players
        self.horses = horses
        self.is_elimination_round = True
        self.elimination_penalty = 1
        self.is_racing_round = False
        self.pot = 0
        self.turns_per_player = turns_per_player
        self.deck = self._create_deck()

    def start_racing(self):
        self.is_elimination_round = False
        self.is_racing_round = True
        print("TIME TO START RACING!")

    def _create_deck(self):
        return [x for x in range(2, 13)] * 4

    def _get_rolled_horse(self, roll: int):
        return next(horse for horse in self.horses if horse.number == roll)

    def _process_penalty(self, rolled_horse: Horse, player: Player):
        print(f"Horse #{rolled_horse.number} already eliminated")
        print(f"{player.name} places {rolled_horse.penalty_price} in the pot")
        player.wallet -= rolled_horse.penalty_price
        self.pot += rolled_horse.penalty_price

    def _reset_horses(self):
        for horse in self.horses:
            horse.reset_status()

    def elimination_round_roll(self, player: Player, roll: int):
        rolled_horse = self._get_rolled_horse(roll)
        # Check if horse is not racing (already eliminated)
        if not rolled_horse.is_racing:
            self._process_penalty(rolled_horse=rolled_horse, player=player)

        else:
            print(f"Horse #{rolled_horse.number} is eliminated, with a price of {self.elimination_penalty}")
            rolled_horse.is_racing = False
            rolled_horse.penalty_price = self.elimination_penalty
            self.elimination_penalty += 1
            if self.elimination_penalty >= 5:  # 4 is the maximum penalty and signals we can move to the racing round
                self.start_racing()

    def racing_round_roll(self, player: Player, roll: int):
        rolled_horse = self._get_rolled_horse(roll)
        if not rolled_horse.is_racing:
            self._process_penalty(rolled_horse=rolled_horse, player=player)

        else:
            print(f"Horse #{rolled_horse.number} Advances!")
            rolled_horse.move_forward()
            if rolled_horse.is_winner:
                print(f"Horse #{rolled_horse.number} WINS!")




"""
Horse Number to win
{
    2: 2
    3: 3
    4: 4
    5: 5
    6: 6
    7: 7
    8: 6
    9: 5
    10: 4
    11: 3
    12: 2
}
"""
