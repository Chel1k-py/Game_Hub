import os, sys, json

def resource_path(relative_path):
    """Возвращает корректный путь к ресурсам и при запуске .py, и при запуске .exe"""
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS   # папка, куда PyInstaller распаковывает временные файлы
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def update_stat():
    global stat
    with open(resource_path("stats.json"), "r") as out_file:
        stat = json.load(out_file)
