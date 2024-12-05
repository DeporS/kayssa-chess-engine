import chess
from .board import Board


def evaluate_board(board):
    """
    Function that evaluates position only by material
    Returns numeric value based on pieces on the board
    """
    material = 0

    for square in chess.SQUARES:
        piece = board.board.piece_at(square)
        if piece is not None:
            # Add piece value based on color
            if piece.color == chess.WHITE:
                material += get_piece_value(piece)
            else:
                material -= get_piece_value(piece)

            # Add value based on occupying center
            if piece.color == chess.WHITE:
                if piece.piece_type == chess.PAWN:
                    if chess.square_name(square) in ["c4", "d4", "e4", "f4"]:
                        material += 0.2
            else:
                if piece.piece_type == chess.PAWN:
                    if chess.square_name(square) in ["c5", "d5", "e5", "f5"]:
                        material -= 0.2

            # Add value for checkmate
            if piece.color == chess.WHITE:
                if board.check_for_checkmate():
                    material += 1000
            else:
                if board.check_for_checkmate():
                    material -= 1000

    return material


def get_piece_value(piece):
    """
    Function that returns material value of a piece
    """
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 1000
    }
    return values.get(piece.piece_type, 0)
