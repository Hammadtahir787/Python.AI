import tkinter as tk
import random

def change_background_color():

    new_color = (f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}'
                 f'{random.randint(0, 255):02x}')
    root.config(bg=new_color)
    print(f"New background color: {new_color}")


root = tk.Tk()
root.title("Color Change App")


button = tk.Button(root, text="Change Color", command=change_background_color)
button.pack(pady=20)  # Add vertical padding for spacing


root.mainloop()
