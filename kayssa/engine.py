import chess
from .board import Board
from .evaluation import evaluate_board


class Engine:
    def __init__(self, board):
        self.board = board
        self.depth = 3

    def get_best_move(self):
        """
        This function selects the best move based on the minimax algorithm
        """
        legal_moves = self.board.legal_moves()
        best_move = None
        best_score = -float('inf')

        for move in legal_moves:
            self.board.make_move(move)  # simulate the move
            score = self.minimax(
                self.depth, -float('inf'), float('inf'), False)
            self.board.undo_move()

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, depth, alpha, beta, maximizing_player):
        # Minimax function
        if depth == 0 or self.board.is_checkmate or self.board.is_stalemate:
            return evaluate_board(self.board)

        if maximizing_player:
            max_eval = -float('inf')
            legal_moves = self.board.legal_moves()
            for move in legal_moves:
                self.board.make_move(move)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.board.undo_move()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            legal_moves = self.board.legal_moves()
            for move in legal_moves:
                self.board.make_move(move)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.board.undo_move()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
