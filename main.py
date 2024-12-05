from kayssa import Board, evaluate_board, Engine
import chess


def main():
    # Initiate board
    board = Board()

    # Set FEN position
    fen = "r1bqk1r1/1ppp1Npp/2n2n2/p1b1p3/2B1P3/3P4/PPP2PPP/RNBQ1RK1 w q - 1 8"
    board.set_fen(fen)
    print(f"Legal moves: {list(board.board.legal_moves)}")

    # Starting position
    print(board.display())

    # Initiate engine
    engine = Engine(board)

    # Get best move
    best_move = engine.get_best_move()
    print(f"Best move: {best_move}")


if __name__ == "__main__":
    main()
