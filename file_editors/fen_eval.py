import chess.pgn
import csv

# Write fen position and eval to csv file
with open("files/2016-02_with_eval.pgn", "r") as pgn_file, open("files/positions_with_eval.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["FEN", "Eval"])

    while True:
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break

        for move in game.mainline():
            if "[%eval" in move.comment:
                eval_comment = move.comment.split("[%eval")[1].split("]")[0].strip()
                try:
                    evaluation = float(eval_comment) if eval_comment[0] != "#" else 1000 if eval_comment[1:] == "+" else -1000 # forced check mates
                    writer.writerow([move.board().fen(), evaluation])
                except ValueError:
                    pass