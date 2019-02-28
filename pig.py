import random

class Game:
    """
    The Game class represents what is required for the game to function and flow.
    """
    def __init__(self, human, computer):
        self.human = human
        self.computer = computer


class Human:
    """
    The Human class represents the human player and what is required for the player make 
    choices, score points, and ultimately win or lose.
    """
    def __init__(self):
        self.score = 0
        # self.turn == 0
        # self.die == 
        # self.choice == 


# class Die:
#     """
#     A 6-sided die is rolled to accumulate points.  If a 1 value is rolled, turn is over, 
#     points awared during the turn are negated of player who rolled.
#     """
#     def roll_die():
#     return random.randint(1, 6)


# if __name__ == "__main__":
