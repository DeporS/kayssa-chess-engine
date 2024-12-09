import zstandard as zstd

input_path = 'files/lichess_db_standard_rated_2016-02.pgn.zst'
output_path = 'files/2016-02.pgn'

with open(input_path, 'rb') as compressed_file, open(output_path, 'wb') as decompressed_file:
    dctx = zstd.ZstdDecompressor()
    dctx.copy_stream(compressed_file, decompressed_file)

print("Decompression complete!")
