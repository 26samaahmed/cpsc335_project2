from tkinter import *
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

Label(root, text="📦 Huffman Coding Compression Tool", font=("Courier New", 18, "bold"), wraplength=500, justify="center").pack()

selected_file_button = Button(root, text="📩 Select File", command=select_file)
selected_file_button.pack(pady=10)
selected_file_button.configure(background='white', font=("Courier New", 12, 'bold'), fg='black', padx=10, pady=5)

decompress_file_button = Button(root, text="🔄 Decompress File", command=decompress_file)
decompress_file_button.pack(pady=20)
decompress_file_button.configure(background='white', font=("Courier New", 12, 'bold'), fg='black', padx=10, pady=5)



root.mainloop()