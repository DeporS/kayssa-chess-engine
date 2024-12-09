import chess.pgn

# Code made to extract games with eval saved to them

games_with_eval = []
with open("files/2016-02.pgn", "r") as pgn_file:
    
    for i in range(10000):
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break
        
        has_eval = any("[%eval" in move.comment for move in game.mainline())
        
        if has_eval: games_with_eval.append(game)


with open("files/2016-02_with_eval.pgn", "w") as output_file:
    for game in games_with_eval:
        output_file.write(str(game) + "\n\n")
        
        
