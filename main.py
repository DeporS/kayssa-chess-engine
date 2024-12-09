from kayssa import Board, evaluate_board, Engine
import chess


def main():
    # Initiate board
    board = Board()

    # Set FEN position
    fen = "k1K5/P7/pP1b4/8/3B4/8/8/8 w - - 0 1"
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
        print(f"Best move: {best_move}")
        board.make_move(best_move)
        print(board.display())
        print(f"Evaluation: {evaluate_board(board)}")


if __name__ == "__main__":
    main()
