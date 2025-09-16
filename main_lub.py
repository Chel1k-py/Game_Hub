import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os

title = "Game Hub"
image_path = "img/b_s.png"
base = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base, "BeatShooter", "dist", "main.exe")

def open_file(event=None):
    os.startfile(file_path)

root = tk.Tk()
root.title(title)
root.geometry("400x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Hello, world!", font=(None, 18))
title_label.pack(pady=20)

original_image = Image.open(image_path)
resized_image = original_image.resize((200, 100))
photo = ImageTk.PhotoImage(resized_image)

image_label = Label(root, image=photo, cursor="hand2")
image_label.pack(pady=10)
image_label.bind("<Button-1>", open_file)

root.mainloop()
