import tkinter as tk
import random

def generate_number():
    numbers = []
    for i in range(6):
        numbers.append(random.randint(1, 99))
    number_label.config(text=numbers)

root = tk.Tk()
root.title("Random Number Generator")
root.geometry("200x100")

generate_button = tk.Button(root, text="Generate Number", command=generate_number)
generate_button.pack(pady=10)

number_label = tk.Label(root, text="")
number_label.pack()

root.mainloop()
