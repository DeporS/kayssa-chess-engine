from kayssa import Board, evaluate_board, Engine
import chess


def main():
    # Initiate board
    board = Board()

    # Set FEN position
    fen = "rnbqkbnr/1p1p1ppp/p1p5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 4"
    board.set_fen_position(fen)

    # print(f"Legal moves: {list(board.board.legal_moves)}")

    # Starting position
    print(board.display())

    # Initiate engine
    engine = Engine(board)

    # Get best move
    # while not board.is_checkmate() or not board.is_stalemate():
    for i in range(10):
        print(f"{'White' if board.get_turn() else 'Black'} moves")
        best_move = engine.get_best_move()
        print(f"Best move: {best_move}")
        board.make_move(best_move)
        print(board.display())
        print(f"Evaluation: {evaluate_board(board)}")


if __name__ == "__main__":
    main()
