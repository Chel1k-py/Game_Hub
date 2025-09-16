import json
import os
import sys
import traceback
from pygame.sprite import Group
from screeninfo import get_monitors
from aim import Aim
from center import *
from follower import Follower
import tkinter as tk
from tkinter import messagebox
import settings_stats
from hearts import Hearts
from score import Score


monitor = get_monitors()[0]
master_root = tk.Tk()
master_root.withdraw()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def PATH_FILE(NAME):
    return os.path.join(BASE_DIR, NAME)


def run():
    pygame.init()
    master = pygame.display.set_mode((monitor.width // 4, monitor.height // 2))
    pygame.display.set_caption("Beat Shooter, record:{x}".format(x=settings_stats.stat['record']))
    settings_stats.update_stat()

    aim = Aim(master)
    hearts = Hearts(master)
    score = Score(master)
    followers = Group()
    enemies = Group()
    create_enemy(master, enemies)
    new_follower = Follower(master, aim)
    followers.add(new_follower)
    effects_group = Group()

    while settings_stats.stat['running']:
        stat = settings_stats.stat
        events(aim)
        followers.update(aim)
        aim.update_aim()
        count_frame(master, enemies)
        run_update_enemies(enemies, followers, effects_group)
        update_display(master, aim, enemies, followers, effects_group, hearts, score)
        pygame.time.Clock().tick(stat["fps"])

        if stat['heart'] == 0:
            stat["running"] = False
            if stat["score"] > stat["record"]:
                with open(PATH_FILE("stats.json"), "r+") as file:
                    out_file = json.load(file)
                    out_file["record"] = stat["score"]
                    file.seek(0)
                    json.dump(out_file, file, indent=4)
                    file.truncate()

    pygame.display.quit()

def ask_to_continue():
    return tk.messagebox.askyesno("Игра", "Начинаем?")

def kmain():
    while True:
        if ask_to_continue():
            run()
        else:
            break
    master_root.destroy()

if __name__ == "__main__":
    kmain()
