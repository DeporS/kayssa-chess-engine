import chess
from .board import Board
from .evaluation import evaluate_board


class Engine:
    def __init__(self, board):
        self.board = board
        self.depth = 3  # depth of searching
        self.prune_depth = 0

    def get_best_move(self):
        """
        This function selects the best move based on the minimax algorithm
        """
        legal_moves = self.board.legal_moves()
        best_move = None
        # White is maximizing (best_score = -inf)
        # Black is minimizing (best_score = inf)
        best_score = -float('inf') if self.board.get_turn() else float('inf')

        for move in legal_moves:
            # print(f"Evaluating move: {move}, Turn: {
            #      'White' if self.board.turn else 'Black'}")
            if self.board.get_turn():
                self.board.make_move(move)  # simulate the move
                # White moved so calc the move for black next (False)
                score = self.minimax(
                    self.depth, self.prune_depth, -float('inf'), float('inf'), False)
                self.board.undo_move()

                if score > best_score:  # Whites turn -> maximize score
                    best_score = score
                    best_move = move
            else:
                self.board.make_move(move)  # simulate the move
                # Black moved so calc the move for white next (True)
                score = self.minimax(
                    self.depth, self.prune_depth, -float('inf'), float('inf'), True)
                self.board.undo_move()

                if score < best_score:  # Blacks turn -> minimize score
                    best_score = score
                    best_move = move

        return best_move

    def minimax(self, depth, prune_depth, alpha, beta, maximizing_player):
        # Minimax function
        if depth == 0 or self.board.check_for_checkmate() or self.board.check_for_stalemate():
            return evaluate_board(self.board)

        if maximizing_player:
            max_eval = -float('inf')
            legal_moves = self.board.legal_moves()
            for move in legal_moves:
                self.board.make_move(move)
                eval = self.minimax(
                    depth - 1, prune_depth + 1, alpha, beta, False)
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
                eval = self.minimax(
                    depth - 1, prune_depth + 1, alpha, beta, True)
                self.board.undo_move()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
