from player import Human, ComputerAi
from game import Board


def play(game, x_player, o_player):
    game.print_board()

    letter = "X"

    while game.is_empty():
        if letter == "X":
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.add_to_board(square, letter):
            print(f"{letter} has moved to square {square}")
            game.print_board()

        if game.is_win(letter):
            print(f"{letter} has won, congrats!")
            return letter

        letter = "O" if letter == "X" else "X"

    print("Game has ended in a draw, there are no available squares")


if __name__ == "__main__":
    game = Board()
    x_player = Human("X")
    o_player = ComputerAi("O")
    play(game, x_player, o_player)
