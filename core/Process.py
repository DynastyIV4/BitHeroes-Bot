from core.constants.ConfigData import BIT_HEROES_PROCESS_NAME, BIT_HEROES_WINDOW_TITLE

import psutil, subprocess
import time
import win32gui

def start_game(game_path: str):
    for proc in psutil.process_iter():
        if BIT_HEROES_PROCESS_NAME.lower() in proc.name().lower():
            return
    subprocess.Popen(game_path)

    while not win32gui.IsWindowVisible(win32gui.FindWindow(None, BIT_HEROES_WINDOW_TITLE)):
        time.sleep(0.1)

def kill_game_process():
    for proc in psutil.process_iter():
        if BIT_HEROES_PROCESS_NAME.lower() in proc.name().lower():
            proc.kill()
