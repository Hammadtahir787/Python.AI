import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Simple Greeting App")

# Create a label with initial text "Welcome!"
label = tk.Label(root, text="Welcome!")
label.pack(pady=20)  # Add vertical padding for spacing

# Create a button that changes the label text when clicked
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=10)  # Add vertical padding for spacing

# Start the GUI event loop
root.mainloop()