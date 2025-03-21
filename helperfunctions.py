# This script contains helper functions for file handling and decompression
# used in the Huffman Compression Tool GUI.

import os
from tkinter import *

"""
NOTES

You can store the path gotten by getfilepath and call size with that
You can use the displayfile to display the contents of the file to a
 specified text box

FOR BACKEND:
decompress_file looks for a binary file called 'compressed.bin'
 (binary) and another file 'huffman_dict.txt'

FOR FRONTEND:
There is a function that determines if output == input, feel free to
 use it if you want, thought it might help if you wanted the GUI to
 display that they are equal
"""

def getfilepath(filename):
    """
    Returns the absolute path of the given filename.
    """
    return os.path.abspath(filename)

def getfilesize(file_path):
    """
    Returns the size of the file at the given path.
    If the file does not exist, returns 0.
    """
    if not os.path.exists(file_path):
        return 0
    else:
        return os.path.getsize(file_path)
    
def displayfile(file_path, text_box):
    """
    Reads the content of the file at the given path and inserts it into the specified text box.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            text_box.insert(END, content)
    except FileNotFoundError:
        print("File not found")

def decompress_file():
    """
    Decompresses the 'compressed.bin' file using the Huffman codes from 'huffman_dict.txt'.
    Returns the decompressed text.
    """
    try:
        # Read Huffman codes from the dictionary file
        with open("huffman_dict.txt", "r", encoding='utf-8') as dict_file:
            huffman_codes = {}
            padding_length = 0
            for line in dict_file:
                line = line.rstrip()
                if not line:
                    continue
                if line.startswith('padding'):
                    padding_length = int(line.split(':')[1])
                else:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        char, code = parts
                        if char == "\\n":
                            char = "\n"
                        huffman_codes[code] = char
                    else:
                        print(f"Malformed line, skipping: {line}")
    except FileNotFoundError:
        print("File huffman_dict.txt not found")
        return None, False
    
    try:
        # Read binary data from the compressed file
        with open("compressed.bin", "rb") as bin_file:
            byte_data = bin_file.read()
    except FileNotFoundError:
        print("Error: Compressed binary file not found.")
        return None, False
    
    # Convert binary data to a binary string
    binary_string = ''.join(f"{byte:08b}" for byte in byte_data)

    # Remove padding bits
    if padding_length > 0:
        binary_string = binary_string[:-padding_length]

    # Decode the binary string using Huffman codes
    decoded_text = ""
    temp_code = ""
    for bit in binary_string:
        temp_code += bit
        if temp_code in huffman_codes:
            decoded_text += huffman_codes[temp_code]
            temp_code = ""
    print(decoded_text)
    return decoded_text

def output_equals_input(decoded_text):
    """
    Compares the decompressed text with the original input text.
    Returns True if they are equal, False otherwise.
    """
    try:
        with open("input.txt", "r", encoding ="utf-8") as f:
            original_text = f.read()
    except FileNotFoundError:
        print("Could not find input.txt")
        return False
    
    return decoded_text == original_text