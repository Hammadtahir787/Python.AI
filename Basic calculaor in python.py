import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            raise ZeroDivisionError
        result = float(entry1.get()) / denominator
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero")

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root, width=10)
entry2 = tk.Entry(root, width=10)
entry1.pack(pady=5)
entry2.pack(pady=5)

add_button = tk.Button(root, text="Add", command=add)
subtract_button = tk.Button(root, text="Subtract", command=subtract)
multiply_button = tk.Button(root, text="Multiply", command=multiply)
divide_button = tk.Button(root, text="Divide", command=divide)

add_button.pack(pady=5)
subtract_button.pack(pady=5)
multiply_button.pack(pady=5)
divide_button.pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

root.mainloop()
