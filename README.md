# kayssa-chess-engine

1. Place .pgn.zst files in the files directory.
2. Run decompressor.py to decompress to .pgn files:
python decompressor.py
3. Extract games with evaluations using eval_extractor.py:
python eval_extractor.py
4. Save fen and eval data with fen_eval.py:
python fen_eval.py
5. Train or fine-tune the model using train.py:
python train.py
6. Test the model or play a game using main.py:
python main.py