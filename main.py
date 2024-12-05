from kayssa import Board, evaluate_board, Engine
import chess


def main():
    # Initiate board
    board = Board()

    # Set FEN position
    fen = "rnk3B1/pP2R2p/3Q2pB/5pP1/8/2N4P/PPP5/4R1K1 b - - 0 26"
    board.set_fen_position(fen)

    # print(f"Legal moves: {list(board.board.legal_moves)}")

    # Starting position
    print(board.display())

    # Initiate engine
    engine = Engine(board)

    # Get best move
    # while not board.is_checkmate() or not board.is_stalemate():
    for i in range(1):
        print(f"{'White' if board.get_turn() else 'Black'} moves")
        best_move = engine.get_best_move()
        print(f"Best move: {best_move}")
        board.make_move(best_move)
        print(board.display())
        print(f"Evaluation: {evaluate_board(board)}")


if __name__ == "__main__":
    main()
