from tkinter import *
from tkinter import filedialog
from huffmanencoding import compress_file
from helperfunctions import *

def select_file_button():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        print(f"Selected file: {file_path}")
        popup = Toplevel(root)
        popup.title("File Selected")
        popup.geometry('300x250')
        popup.configure(background='white')
        Label(popup, text=f"Selected file: {file_path}", wraplength=250).pack()
        compress_file(file_path) # Looking at the Demo Video there isn't a button to compress
        displayfile(getfilepath("huffman_dict.txt"), text_box1)
        Label(popup, text=f"Compressed file saved as 'compressed.bin'").pack()
        Button(popup, text="OK", command=popup.destroy).pack()
        input_size = getfilesize(file_path)
        output_size = getfilesize(getfilepath("compressed.bin"))
        global comparison_line
        ratio = (1-(output_size/input_size)) * 100 # This ratio shows how much of the original file was compressed
        comparison_line = f"Original: {input_size} bytes | Compressed: {output_size} bytes | Ratio: {ratio:.2f}%"
        comparison_label.config(text=comparison_line)  # Update the GUI comparison line

    else:
        print("No file selected")

def decompression_button():
    decompressed_text = decompress_file()
    if decompressed_text:
        text_box2.delete(1.0, END)
        text_box2.insert(END, decompressed_text)
    else:
        print("Decompression failed")


root = Tk()
root.title("Huffman Compression Tool Project 2 Team 1")
root.geometry('700x700')
root.configure(background='#002438')

Label(root, text="📦 Huffman Coding Compression Tool", font=("Courier New", 18, "bold"), fg="white", wraplength=500, justify="center", bg='#002438', pady=10).pack()
selected_file_button = Button(root, text="📩 Select File", command=select_file_button)
selected_file_button.pack(pady=10)
selected_file_button.configure(background='#002438', font=("Courier New", 12, 'bold'), fg='black', padx=10, pady=5, bg='#002438')

# Text for size comparisons
comparison_line = f"Compression details will appear here."
comparison_label = Label(root, text=comparison_line, font=("Courier New", 10, "bold"), wraplength=500, justify="center", background="#002438", fg="white", pady=10)
comparison_label.pack()

# Text box with scrollbar for huffman binary code
Label(root, text="Huffman Codes:", font=("Courier New", 16, "bold"), fg="white", wraplength=500, justify="center", background="#002438").pack()
text_frame = Frame(root)
text_frame.pack(pady=10)
text_frame.configure(background='#002438', borderwidth=1)
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)
text_box1 = Text(text_frame, height=10, width=50, yscrollcommand=scrollbar.set)
text_box1.pack(side=LEFT, fill=Y)
scrollbar.config(command=text_box1.yview, background='#002438')

# Decompress file button
decompress_file_button = Button(root, text="🔄 Decompress File", command=decompression_button)
decompress_file_button.pack(pady=20)
decompress_file_button.configure(background='white', font=("Courier New", 12, 'bold'), fg='black', padx=10, pady=5, bg='#002438')

Label(root, text="Decoded Text:", font=("Courier New", 16, "bold"), fg="white", wraplength=500, justify="center", background="#002438").pack()
text_frame = Frame(root)
text_frame.pack(pady=10)
text_frame.configure(background='#002438', borderwidth=1)
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)
text_box2 = Text(text_frame, height=10, width=50, yscrollcommand=scrollbar.set)
text_box2.pack(side=LEFT, fill=Y)
scrollbar.config(command=text_box2.yview)

root.mainloop()
