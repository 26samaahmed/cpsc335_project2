import os
import heapq
from collections import Counter, namedtuple

"""
NOTES

added a getfilepath() for convenience
file size takes a file path, you can store the path gotten by getfilepath and call size with that

FOR BACKEND:
decompress_file looks for a binary file called 'compressed.bin' (binary) and another file 'huffman_dict.txt'

FOR FRONTEND:
There is a function that determines if output == input, feel free to use it if you want, thought
it might help if you wanted the GUI to display that they are equal
"""

def getfilepath(filename):
    return os.path.abspath(filename)

def getfilesize(file_path):
    if not os.path.exists(file_path):
        return 0
    else:
        return os.path.getsize(file_path)
    
def decompress_file():
    try:
        with open("huffman_dict.txt", "r", encoding='utf-8') as dict_file:
            huffman_codes = {}
            for line in dict_file:
                char, code = line.strip().split(":")
                huffman_codes[code] = char
    except FileNotFoundError:
        print("File huffman_dict.txt not found")
        return None, False
    
    try:
        with open("compressed.bin", "rb") as bin_file:
            byte_data = bin_file.read()
    except FileNotFoundError:
        print("Error: Compressed binary file not found.")
        return None, False
    
    binary_string = ''.join(f"{byte:08b}" for byte in byte_data)

    decoded_text = ""
    temp_code = ""
    for bit in binary_string:
        temp_code += bit
        if temp_code in huffman_codes:
            decoded_text += huffman_codes[temp_code]
            temp_code = ""
    return decoded_text

def output_equals_input(decoded_text):
    try:
        with open("input.txt", "r", encoding ="utf-8") as f:
            original_text = f.read()
    except FileNotFoundError:
        print("Could not find input.txt")
        return False
    
    return decoded_text == original_text