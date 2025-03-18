import heapq

'''Compression'''

# Step 1: Define Huffman Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Step 2: Build Huffman Tree
def build_huffman_tree(freq_map):
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)
    
    return heap[0]

# Step 3: Generate Huffman Code
def build_codes(node, prefix='', code_map={}):
    if node is None:
        return
    
    if node.char is not None:
        code_map[node.char] = prefix
    build_codes(node.left, prefix + '0', code_map) # left child (0)
    build_codes(node.right, prefix + '1', code_map) # right child (1)
    return code_map

# Step 4: Compress File
def compress_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Calculate frequency of each character
    freq_map = {}
    for char in text:
        if char not in freq_map:
            freq_map[char] = 0
        freq_map[char] += 1

    # Build Huffman Tree and Codes
    huffman_tree = build_huffman_tree(freq_map)
    huffman_codes = build_codes(huffman_tree)

    # Encode text
    encoded_text = ''.join(huffman_codes[char] for char in text)

    #Find padding
    padding_length = (8 - len(encoded_text) % 8) % 8
    padded_encoded = encoded_text + '0' * padding_length

    # Save encoded text to binary file
    with open('compressed.bin', 'wb') as bin_file:
        bin_file.write(int(encoded_text, 2).to_bytes((len(encoded_text) + 7) // 8, byteorder='big'))
    print("File compressed and saved as 'compressed.bin'")
    
    # Save Huffman dictionary
    with open('huffman_dict.txt', 'w') as dict_file:
        for char, code in huffman_codes.items():
            dict_file.write(f'{char}:{code}\n')
    print("Huffman dictionary saved as 'huffman_dict.txt'")