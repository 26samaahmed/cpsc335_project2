from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog


def compress_file(file_path):
    pass

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        print(f"Selected file: {file_path}")
        popup = Toplevel(root)
        popup.title("File Selected")
        popup.geometry('300x250')
        popup.configure(background='white')
        Label(popup, text=f"Selected file: {file_path}", wraplength=250).pack()
        compress_button = Button(popup, text="Compress File", command=lambda: compress_file(file_path))
        Label(popup, text=f"Compressed file saved as 'compressed.bin'").pack()
        Button(popup, text="OK", command=popup.destroy).pack()
    else:
        print("No file selected")


def decompress_file():
    pass

root = Tk()
root.title("Huffman Compression Tool Project 2 Team 1")
root.geometry('700x550')
root.configure(background='white')

Label(root, text="📦 Huffman Coding Compression Tool", font=("Courier New", 18, "bold"), wraplength=500, justify="center", bg='white').pack()

selected_file_button = Button(root, text="📩 Select File", command=select_file)
selected_file_button.pack(pady=10)
selected_file_button.configure(background='white', font=("Courier New", 12, 'bold'), fg='black', padx=10, pady=5, bg='white')

# Text box with scrollbar for huffman binary code
Label(root, text="Huffman Codes:", font=("Courier New", 16, "bold"), wraplength=500, justify="center", background="white").pack()
text_frame = Frame(root)
text_frame.pack(pady=20)
text_frame.configure(background='white', borderwidth=1)
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)
text_box = Text(text_frame, height=10, width=50, yscrollcommand=scrollbar.set)
text_box.pack(side=LEFT, fill=Y)
scrollbar.config(command=text_box.yview, background='white')



decompress_file_button = Button(root, text="🔄 Decompress File", command=decompress_file)
decompress_file_button.pack(pady=20)
decompress_file_button.configure(background='white', font=("Courier New", 12, 'bold'), fg='black', padx=10, pady=5, bg='white')

Label(root, text="Decoded Text:", font=("Courier New", 16, "bold"), wraplength=500, justify="center", background="white").pack()
text_frame = Frame(root)
text_frame.pack(pady=20)
text_frame.configure(background='white', borderwidth=1)
scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)
text_box = Text(text_frame, height=5, width=50, yscrollcommand=scrollbar.set)
text_box.pack(side=LEFT, fill=Y)
scrollbar.config(command=text_box.yview)


root.mainloop()