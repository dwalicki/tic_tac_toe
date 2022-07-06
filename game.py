class Board:
    def __init__(self, desired_board=3):
        self.desired_board = desired_board
        self.board = [" " for _ in range(desired_board**2)]

    def print_board(self):
        for idx, i in enumerate(self.board):
            end = "\n" if idx % self.desired_board == self.desired_board - 1 else ""
            print(i if i != " " else idx, end=end)

    def available_moves(self):
        return [i for i, square in enumerate(self.board) if square == " "]

    def add_to_board(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.is_win(letter):
                return True
            return True
        return False

    def is_empty(self):
        return " " in self.board

    def is_win(self, letter):
        for win_condition in [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]:
            result = True
            for item in win_condition:
                if self.board[item] != letter:
                    result = False
            if result == True:
                return True
        return False
