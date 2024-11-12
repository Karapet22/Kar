def lz77_compress(data, window_size=4096, lookahead_size=18):
    i = 0
    compressed_data = []
    
    while i < len(data):

        search_window = data[max(0, i - window_size):i]
        lookahead_buffer = data[i:i + lookahead_size]

        match_length = 0
        match_distance = 0
        for j in range(1, len(lookahead_buffer) + 1):
            substring = lookahead_buffer[:j]
            if substring in search_window:
                match_length = j
                match_distance = len(search_window) - search_window.rfind(substring)
        if match_length > 0:
            next_symbol = lookahead_buffer[match_length] if match_length < len(lookahead_buffer) else ''
            compressed_data.append((match_length, match_distance, next_symbol))
            i += match_length + (1 if next_symbol else 0)
        else:
            compressed_data.append((0, 0, lookahead_buffer[0]))
            i += 1
    
    return compressed_data

def lz77_decompress(compressed_data):
    decompressed_data = []
    
    for length, distance, symbol in compressed_data:
        if length > 0:

            start = len(decompressed_data) - distance
            for i in range(length):
                decompressed_data.append(decompressed_data[start + i])
        if symbol:
            decompressed_data.append(symbol)
    
    return ''.join(decompressed_data)

input_data = "ABABABABAABCABCABABABA"
print("Input Data:", input_data)

compressed = lz77_compress(input_data)
print("Compressed Data:", compressed)

decompressed = lz77_decompress(compressed)
print("Decompressed Data:", decompressed)
