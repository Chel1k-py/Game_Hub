import json, os

def PATH_FILE(NAME):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATS_PATH = os.path.join(BASE_DIR, f"{NAME}")
    return STATS_PATH

def update_stat():
    global stat
    out_file = open(PATH_FILE("stats.json"), "r")
    stat = json.load(out_file)
    out_file.close()


update_stat()
