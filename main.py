from kayssa import Board
import chess

board = Board()

print("Starting the game")
board.display()

# Sprawdzamy legalne ruchy
legal_moves = board.legal_moves()
print("Legal moves:", legal_moves)

move = chess.Move.from_uci("e2e4")
print(f"Move {move} is being made")
board.make_move(move)

# Wykonujemy ruch i wyświetlamy planszę
board.display()
