import chess


class Board:
    def __init__(self):
        # initialize empty board
        self.board = chess.Board()

    def display(self):
        # print board state
        print(self.board)

    def is_checkmate(self):
        # check if checkmate
        return self.board.is_checkmate()

    def is_stalemate(self):
        # check if stalemate
        return self.board.is_stalemate()

    def is_check(self):
        # check if check
        return self.board.is_check()

    def legal_moves(self):
        # return legal moves list
        return self.board.legal_moves

    def make_move(self, move):
        # make move
        try:
            self.board.push(move)
        except ValueError:
            print("Illegal move")

    def undo_move(self):
        # undo last move
        try:
            self.board.pop()
        except ValueError:
            print("No moves made yet")

    def get_fen(self):
        # return fen of position
        return self.board.fen()

    def set_fet(self, fen):
        # sets board with given fen
        self.board.set_fen(fen)
