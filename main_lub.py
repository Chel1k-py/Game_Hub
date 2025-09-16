import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os

title = "Game Hub"
image_path = "img/b_s.png"
base = os.path.dirname(os.path.abspath(__file__))

games = [
    {"name": "BeatShooter",
     "img": "img/b_s.png",
     "exe": os.path.join(base, "BeatShooter", "dist", "main.exe")
     },
    {"name": "stub", "img": None, "exe": None},
    {"name": "stub", "img": None, "exe": None},
    {"name": "stub", "img": None, "exe": None},
]

def open_file(path):
    if path and os.path.exists(path):
        os.startfile(path)

def location(container, game_list, columns=2):
    for i, game in enumerate(game_list):
        row = i // columns
        col = i % columns

        master = tk.Frame(container, padx=10, pady=10)
        master.grid(row=row, column=col, sticky="nsew")

        if game["img"] and os.path.exists(game["img"]):
            o_image = Image.open(game["img"])
            r_image = o_image.resize((150, 75))
            photo = ImageTk.PhotoImage(r_image)

            image_l = Label(master, image=photo, cursor="hand2")
            image_l.image = photo
            image_l.pack()
            image_l.bind("<Button-1>", lambda e, path=game["exe"]: open_file(path))
        else:
            plug = Label(master, text="Нет картинки", width=20, height=5, bg="gray")
            plug.pack()

        title_l = tk.Label(master, text=game["name"], font=(None, 12))
        title_l.pack(pady=5)

root = tk.Tk()
root.title(title)
root.geometry("800x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Выбери игру:", font=(None, 18))
title_label.pack(pady=20)

master = tk.Frame(root)
master.pack(expand=True, fill="both", side="left")

location(master, games, columns=2)

root.mainloop()

