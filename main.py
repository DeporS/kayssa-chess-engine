from kayssa import Board, evaluate_board, Engine, feature_extractor
import chess
import pandas as pd
import numpy as np
from tensorflow import keras

def main():
    # Initiate board
    board = Board()

    # Set FEN position
    fen = "rnbqkbnr/pppp1ppp/8/4p2Q/4P3/8/PPPP1PPP/RNB1KBNR b KQkq - 1 2"
    board.set_fen_position(fen)

    # print(f"Legal moves: {list(board.board.legal_moves)}")

    # Starting position
    print(board.display())

    # Initiate engine
    engine = Engine(board)

    # Get best move
    # while not board.is_checkmate() or not board.is_stalemate():
    for i in range(5):
        print(f"{'White' if board.get_turn() else 'Black'} moves")
        best_move = engine.get_best_move()
        if best_move == None:
            if board.check_for_checkmate():
                print(f"\nCheckmate! {'White' if board.get_turn() else 'Black'} won!")
                break
            else:
                print("\nStalemate!\n")
                break
        else:
            print(f"Best move: {best_move}")
            board.make_move(best_move)
            print(board.display())
            print(f"Evaluation: {evaluate_board(board)}")

def test_model():
    model = keras.models.load_model("chess_model.keras")
    fen_new = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    vector_new = feature_extractor.board_vector_from_fen(fen_new)
    eval_pred = model.predict(np.array([vector_new]))  # Przewidywana ocena
    print(f"Predykcja oceny: {eval_pred}")

if __name__ == "__main__":
    test_model()
