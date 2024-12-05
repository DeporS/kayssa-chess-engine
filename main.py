from kayssa import Board, evaluate_board
import chess


def main():
    # Tworzymy instancję szachownicy
    board = Board()

    # Zaczynamy grę, np. wykonujemy ruchy
    print("Początkowa pozycja na szachownicy:")
    print(board.display())

    # Oceniamy pozycję szachownicy
    evaluation = evaluate_board(board)
    print(f"Wartość oceny pozycji: {evaluation}")

    # Przykład wykonania ruchu
    move = board.board.push_san("e2e4")  # Ruch białych: pionek z e2 na e4
    print(f"Po wykonaniu ruchu {move}:")
    print(board.display())
    move = board.board.push_san("d7d5")  # Ruch białych: pionek z e2 na e4
    print(f"Po wykonaniu ruchu {move}:")
    print(board.display())

    # Ponownie oceniamy pozycję
    evaluation = evaluate_board(board)
    print(f"Wartość oceny pozycji po ruchu: {evaluation}")


if __name__ == "__main__":
    main()
