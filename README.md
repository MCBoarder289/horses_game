# Horses Game

## Overview
Played a simple game of chance for multiple players that simulates horse racing.
Believe this is called `Quarter Horses`, but thought it would be fun to try and program an interactive game.

## Game Rules
Game involves everyone having a set amount of chips that fund the payouts, two dice, and a subset of cards (2s-Queens).

There is a set of 12 horses, each representing the sum of all possibilities of 2 dice rolls.


Game consistes of two major rounds:

All of the cards (or a subset if few players?) are dealt to everyone.

Initial round is an elimination round:
    
* A player rolls the dice.
* That number horse is now eliminated, and an initial penalty amount is set.
    * First penalty is 1, then 2, then 3, then 4.
    * This number is removed from all hands
* Next player rolls the dice
    * If the horse is already eliminated, player puts the penalty price into the winnings pot.
    * Continues until the 4 horses are eliminated
    
Ending round is the "Horse Race":
    
* Players take turns rolling the dice
    * If they roll an eliminated horse, then they put the penalty price into the winnings pot.
    * Else that horse advances towards victory
* Horses have a set number of rolls that determine if they cross the finish line based on their probability
    * ```
      { 
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 6,
        9: 5,
        10: 4,
        11: 3,
        12: 2,
      }
      ```
* Once a non-eliminated horse hits enough times, the pot is divided equally amongst players holding those horse cards.
    
## Ideas

### Initial Goals
* Build out backend logic to play/simulate the game
* Maybe make it a simple CLI + basic UI game?

### Stretches
* Would be amazing to have this be a website game so that people can play together online
* Controlling a rolling action from their device, watching the UI keep track of winnings/progress etc.
* Cool UI/UX for the game (but start super simple)

## Environment Setup
1. Ensure pyenv is installed:
    * `curl https://pyenv.run | bash`
2. Ensure pyenv activated in your bash/shell profile:
    *   This is added to your profile:
        ```
        eval "$(pyenv init -) 
        eval "$(pyenv virtualenv-init -)"
        ```
        
3. Give proper permissions to `setup-dev.sh` and `remove-venv.sh`
    * ex: `chmod 755 remove-venv.sh`
    
4. Run `make setup-dev`

## Environment reset
1. Run `make reset-dev`

