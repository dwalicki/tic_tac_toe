import random


class Player:
    def __init__(self, letter):
        # X or O
        self.letter = letter

    def get_move(self, game):
        pass


class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        is_valid_square = False
        val = None
        while not is_valid_square:
            square = input("Please select an available square from 0 to 8.\n")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                is_valid_square = True
            except ValueError:
                print("This is not a valid square, please select a valid square.")
        return val


class ComputerAi(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
