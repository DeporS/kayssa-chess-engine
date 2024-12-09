import chess

def extract_features_from_fen(fen):
    board = chess.Board(fen)
    features = []

    # Number of pieces White - "+" Black - "-"
    pieces = {
        chess.PAWN: 0,
        chess.KNIGHT: 0,
        chess.BISHOP: 0,
        chess.ROOK: 0,
        chess.QUEEN: 0,
        chess.KING: 0
    }
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            pieces[piece.piece_type] += 1 if piece.color == chess.WHITE else -1
    features.extend([
        pieces[chess.PAWN],
        pieces[chess.KNIGHT],
        pieces[chess.BISHOP],
        pieces[chess.ROOK],
        pieces[chess.QUEEN],
        pieces[chess.KING],
    ])

    # Structure of pawns
    features.append(board.piece_map())

    # Safety of king
    features.append(board.is_check())
    features.append(board.is_checkmate())

    return features

def board_vector_from_fen(fen):
    board = chess.Board(fen)

    # vector for chessboard representation
    vector = [0] * (64 * 12)

    pieces_map = {
        chess.PAWN: 0,
        chess.BISHOP: 1,
        chess.KNIGHT: 2,
        chess.ROOK: 3,
        chess.QUEEN: 4,
        chess.KING: 5
    }

    for square in chess.SQUARES:
        piece = board.piece_at(square)

        if piece:
            piece_type = piece.piece_type
            color_offset = 0 if piece.color == chess.WHITE else 6  # 0-5 dla białych, 6-11 dla czarnych
            
            index = square * 12 + (piece_type - 1 + color_offset)  # square * 12 + offset dla figury
            vector[index] = 1
        
    return vector
