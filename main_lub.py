import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import os


title = "Game Hub"
base = os.path.dirname(os.path.abspath(__file__))

games = [
    {
        "name": "BeatShooter",
        "img": "img/b_s.png",
        "exe": os.path.join(base, "BeatShooter", "dist", "main.exe")
    },
    {"name": "stub", "img": None, "exe": None},
    {"name": "stub", "img": None, "exe": None},
    {"name": "stub", "img": None, "exe": None},
]


def open_file(path):

    if os.path.exists(path):

        os.startfile(path)


def open_folder(path):

    if os.path.exists(path):

        name = os.path.dirname(path)
        os.startfile(name)


def show_info(game):

    for widget in r_frame.winfo_children():
        widget.destroy()

    if os.path.exists(game["img"]):

        o_image = Image.open(game["img"])
        photo = ImageTk.PhotoImage(o_image.resize((200, 100)))

        image_l = Label(r_frame, image=photo)
        image_l.image = photo
        image_l.pack(pady=10)

    else:

        plug = Label(r_frame, text="Нет картинки", width=25, height=10, bg="gray")
        plug.pack(pady=10)

    label = tk.Label(r_frame, text=game["name"], font=(None, 14))
    label.pack(pady=5)

    if game["exe"]:

        btn_open = Button(
            r_frame, text="Открыть папку", command=lambda: open_folder(game["exe"])
        )
        btn_open.pack(pady=5)

        btn_play = Button(
            r_frame, text="Играть", command=lambda: open_file(game["exe"])
        )
        btn_play.pack(pady=5)

    else:

        Label(r_frame, text="Игра недоступна").pack(pady=10)


def location(container, game_list, columns=2):

    for i, game in enumerate(game_list):

        row = i // columns
        col = i % columns

        master = tk.Frame(container, padx=10, pady=10)
        master.grid(row=row, column=col, sticky="nsew")

        if game["img"] and os.path.exists(game["img"]):

            o_image = Image.open(game["img"])
            photo = ImageTk.PhotoImage(o_image.resize((150, 75)))

            image_l = Label(master, image=photo, cursor="hand2")
            image_l.image = photo
            image_l.pack()
            image_l.bind("<Button-1>", lambda e, g=game: show_info(g))

        else:

            plug = Label(master, text="Нет картинки", width=20, height=5, bg="gray")
            plug.pack()

        title_l = tk.Label(master, text=game["name"], font=(None, 12))
        title_l.pack(pady=5)


root = tk.Tk()
root.title(title)
root.geometry("1000x500")
root.resizable(False, False)

l_frame = tk.Frame(root, width=600, bg="white")
l_frame.pack(side="left", fill="both", expand=True)

r_frame = tk.Frame(root, width=400, bg="lightgray")
r_frame.pack(side="right", fill="both", expand=True)

title1 = tk.Label(l_frame, text="Выбери игру:", font=(None, 18))
title1.pack(pady=20)

master = tk.Frame(l_frame)
master.pack(expand=True, fill="both")

location(master, games, columns=2)

root.mainloop()
