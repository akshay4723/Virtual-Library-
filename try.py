import tkinter as tk
from tkinter import messagebox

def add_data():
    name = name_entry.get()
    author = author_entry.get()
    content = content_entry.get()
    if not name or not author or not content:
        messagebox.showwarning("Input Error", "Please fill out all fields")
        return
    
    with open("books.txt", "a") as file:
        file.write(f"{name},{author},{content}\n")
    
    clear_entries()
    messagebox.showinfo("Success", "Book added successfully")

def clear_entries():
    name_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    content_entry.delete(0, tk.END)

def show_add_books():
    add_books_window = tk.Toplevel(root)
    add_books_window.title("Add Books")
    add_books_window.geometry("400x300")
    
    global name_entry, author_entry, content_entry

    tk.Label(add_books_window, text="Book Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky='w')
    name_entry = tk.Entry(add_books_window, font=("Helvetica", 12))
    name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    tk.Label(add_books_window, text="Author:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky='w')
    author_entry = tk.Entry(add_books_window, font=("Helvetica", 12))
    author_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

    tk.Label(add_books_window, text="Content:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky='w')
    content_entry = tk.Entry(add_books_window, font=("Helvetica", 12))
    content_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')

    submit_button = tk.Button(add_books_window, text="Submit", command=add_data, font=("Helvetica", 12), bg="blue", fg="white")
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    add_books_window.grid_columnconfigure(1, weight=1)

def show_view_books():
    view_books_window = tk.Toplevel(root)
    view_books_window.title("View Books")
    view_books_window.geometry("400x300")

    listbox = tk.Listbox(view_books_window, width=50, height=15, font=("Helvetica", 12))
    listbox.pack(padx=10, pady=10)

    try:
        with open("books.txt", "r") as file:
            for idx, line in enumerate(file, 1):
                name, author, content = line.strip().split(",")
                listbox.insert(tk.END, f"{idx}. {name} by {author} - {content}")
    except FileNotFoundError:
        messagebox.showwarning("File Error", "No data file found")

root = tk.Tk()
root.title("Library Management System")
root.geometry("400x200")

tk.Label(root, text="Library Management System", font=("Helvetica", 16)).pack(pady=20)
tk.Button(root, text="Add Books", command=show_add_books, font=("Helvetica", 12), width=15, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="View Books", command=show_view_books, font=("Helvetica", 12), width=15, bg="orange", fg="white").pack(pady=5)

root.mainloop()
