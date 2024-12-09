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
    # for testing
    model = keras.models.load_model("kayssa.keras")
    fen_new = "R7/ppp2kpp/5p2/8/2pQ2P1/1P6/PBP2P1P/RN4K1 b - - 0 17"
    vector_new = feature_extractor.board_vector_from_fen(fen_new)
    eval_pred = model.predict(np.array([vector_new]))  
    print(f"Evaluation prediction: {eval_pred}")

    fen_new = "r4rk1/ppp1Rppp/8/8/2pQ2P1/1P6/PBP2P1P/RN4K1 b - - 0 14"
    vector_new = feature_extractor.board_vector_from_fen(fen_new)
    eval_pred = model.predict(np.array([vector_new]))  
    print(f"Evaluation prediction: {eval_pred}")

    fen_new = "6k1/ppR2ppp/8/8/2p3P1/1P6/PBP2P1P/RN1r2K1 w - - 1 17"
    vector_new = feature_extractor.board_vector_from_fen(fen_new)
    eval_pred = model.predict(np.array([vector_new]))  
    print(f"Evaluation prediction: {eval_pred}")

if __name__ == "__main__":
    test_model()
