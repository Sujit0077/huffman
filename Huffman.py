import heapq
from collections import Counter, defaultdict

# Function to build the Huffman Tree and generate codes
def huffman_encoding(text):
    # Calculate frequency of each character
    frequency = Counter(text)
    
    # Create a priority queue (min-heap) of tuples (frequency, character)
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)
    
    # Build the Huffman Tree
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Generate Huffman codes
    huffman_codes = {char: code for char, code in heap[0][1:]}
    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes

# Function to decode the encoded text using Huffman codes
def huffman_decoding(encoded_text, huffman_codes):
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    decoded_text, code = "", ""
    for bit in encoded_text:
        code += bit
        if code in reverse_codes:
            decoded_text += reverse_codes[code]
            code = ""
    return decoded_text

# Example usage
text = "huffman encoding example"
encoded_text, huffman_codes = huffman_encoding(text)
print("Huffman Codes:", huffman_codes)
print("Encoded text:", encoded_text)

decoded_text = huffman_decoding(encoded_text, huffman_codes)
print("Decoded text:", decoded_text)
