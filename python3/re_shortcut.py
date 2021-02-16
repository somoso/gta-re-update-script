import os, winshell, win32com.client, Pythoncom
from re_common import get_config
import platform


def create_shortcut(link_name, link_target_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(link_name)
    shortcut.Targetpath = link_target_path
    shortcut.IconLocation = link_target_path
    shortcut.save()

def create_game_shortcut(steam_dir):
    if platform.system() == "Windows":
        config = get_config("rc")
        create_shortcut = True
        if not ("extra" in config and "createShortcut" in config["extra"]):
            create_shortcut = True
        create_shortcut = config["extra"]["createShortcut"]

        if create_shortcut:
            desktop = winshell.desktop()
            path = os.path.join(desktop, 'GTA3 Remastered.lnk')
            target = os.path.join(steam_dir, "steamapps", "common", "Grand Theft Auto 3", "re3.exe")
            create_shortcut(path, target)

            path = os.path.join(desktop, 'GTA VC Remastered.lnk')
            target = os.path.join(steam_dir, "steamapps", "common", "Grand Theft Auto Vice City", "reVC.exe")
            create_shortcut(path, target)
