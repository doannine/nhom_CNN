import tkinter as tk
from tkinter import messagebox

# Hàm để tạo bảng Playfair từ khóa
def create_playfair_table(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # Loại bỏ 'J' vì nó thường được thay thế bằng 'I' trong Playfair
    keyword = keyword.upper().replace('J', 'I')
    keyword_set = set()
    playfair_table = []
    for char in keyword:
        if char not in keyword_set and char in alphabet:
            keyword_set.add(char)
            playfair_table.append(char)
    for char in alphabet:
        if char not in keyword_set:
            playfair_table.append(char)
    return playfair_table

# Hàm để mã hóa một cặp ký tự
def encode_pair(pair, table):
    index_a = table.index(pair[0])
    index_b = table.index(pair[1])
    row_a, col_a = divmod(index_a, 5)
    row_b, col_b = divmod(index_b, 5)
    if row_a == row_b:
        return table[row_a * 5 + (col_a + 1) % 5] + table[row_b * 5 + (col_b + 1) % 5]
    elif col_a == col_b:
        return table[((row_a + 1) % 5) * 5 + col_a] + table[((row_b + 1) % 5) * 5 + col_b]
    else:
        return table[row_a * 5 + col_b] + table[row_b * 5 + col_a]

# Hàm giải mã một cặp ký tự
def decode_pair(pair, table):
    index_a = table.index(pair[0])
    index_b = table.index(pair[1])
    row_a, col_a = divmod(index_a, 5)
    row_b, col_b = divmod(index_b, 5)
    if row_a == row_b:
        return table[row_a * 5 + (col_a - 1) % 5] + table[row_b * 5 + (col_b - 1) % 5]
    elif col_a == col_b:
        return table[((row_a - 1) % 5) * 5 + col_a] + table[((row_b - 1) % 5) * 5 + col_b]
    else:
        return table[row_a * 5 + col_b] + table[row_b * 5 + col_a]

# Hàm để thực hiện mã hóa văn bản
def encode_text(text, table):
    encoded_text = ''
    text = text.upper().replace('J', 'I')
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]
        encoded_text += encode_pair(text[i:i + 2], table)
        i += 2
    return encoded_text

# Hàm để thực hiện giải mã văn bản
def decode_text(text, table):
    decoded_text = ''
    text = text.upper().replace('J', 'I')
    i = 0
    while i < len(text):
        decoded_text += decode_pair(text[i:i + 2], table)
        i += 2
    return decoded_text

# Hàm gọi khi nhấn nút Mã hóa
def encode_button_click():
    keyword = keyword_entry.get()
    plaintext = plaintext_entry.get()
    if not keyword or not plaintext:
        messagebox.showerror("Error", "Vui lòng nhập từ khóa và văn bản cần mã hóa.")
        return
    table = create_playfair_table(keyword)
    encoded_text = encode_text(plaintext, table)
    encoded_text_label.config(text=encoded_text)

# Hàm gọi khi nhấn nút Giải mã
def decode_button_click():
    keyword = keyword_entry.get()
    encoded_text = encoded_text_entry.get()
    if not keyword or not encoded_text:
        messagebox.showerror("Error", "Vui lòng nhập từ khóa và văn bản cần giải mã.")
        return
    table = create_playfair_table(keyword)
    decoded_text = decode_text(encoded_text, table)
    decoded_text_label.config(text=decoded_text)

# Tạo cửa sổ
window = tk.Tk()
window.title("Playfair Cipher")

# Tạo các widget
keyword_label = tk.Label(window, text="Từ khóa:")
keyword_label.grid(row=0, column=0, padx=5, pady=5)

keyword_entry = tk.Entry(window)
keyword_entry.grid(row=0, column=1, padx=5, pady=5)

plaintext_label = tk.Label(window, text="Văn bản cần mã hóa:")
plaintext_label.grid(row=1, column=0, padx=5, pady=5)

plaintext_entry = tk.Entry(window)
plaintext_entry.grid(row=1, column=1, padx=5, pady=5)

encode_button = tk.Button(window, text="Mã hóa", command=encode_button_click)
encode_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

encoded_text_label = tk.Label(window, text="", wraplength=300)
encoded_text_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

encoded_text_label_title = tk.Label(window, text="Văn bản đã mã hóa")
encoded_text_label_title.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

encoded_text_entry = tk.Entry(window)
encoded_text_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

decode_button = tk.Button(window, text="Giải mã", command=decode_button_click)
decode_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

decoded_text_label = tk.Label(window, text="", wraplength=300)
decoded_text_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

decoded_text_label_title = tk.Label(window, text="Văn bản đã giải mã")
decoded_text_label_title.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Chạy ứng dụng
window.mainloop()
