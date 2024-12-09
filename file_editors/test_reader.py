import chess.pgn

# Test if decompression was succesful
with open("files/2016-02.pgn", "r") as pgn_file:
    # Example
    first_game = chess.pgn.read_game(pgn_file)
    print(first_game)

    # Get x first headers
    for i in range(5):
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break
        print(game.headers) 
