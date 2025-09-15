import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os

WINDOW_TITLE = "Game Hub"
IMAGE_PATH = "img/b_s.png"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "BeatShooter", "main.py")

def open_file(event=None):
    os.startfile(FILE_PATH)

root = tk.Tk()
root.title(WINDOW_TITLE)
root.geometry("400x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Добро пожаловать в игру!", font=("Arial", 18))
title_label.pack(pady=20)

original_image = Image.open(IMAGE_PATH)
resized_image = original_image.resize((200, 100))
photo = ImageTk.PhotoImage(resized_image)

image_label = Label(root, image=photo, cursor="hand2")
image_label.pack(pady=10)
image_label.bind("<Button-1>", open_file)

root.mainloop()
