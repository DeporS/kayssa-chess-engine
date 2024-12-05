import chess


class Board:
    def __init__(self):
        # initialize empty board
        self.board = chess.Board()

    def display(self):
        # print board state
        print(self.board)

    def get_turn(self):
        # White - True, Black - False
        return self.board.turn

    def check_for_checkmate(self):
        # check if checkmate
        return self.board.is_checkmate()

    def check_for_stalemate(self):
        # check if stalemate
        return self.board.is_stalemate()

    def check_for_check(self):
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

    def get_fen_position(self):
        # return fen of position
        return self.board.fen()

    def set_fen_position(self, fen):
        # sets board with given fen
        self.board.set_fen(fen)
