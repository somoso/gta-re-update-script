import os
from zipfile import ZipFile


def extract_gta3(three, steam_dir):
    with ZipFile(three, 'r') as zipObj:
        zipObj.extractall(os.path.join(steam_dir, "steamapps", "common", "Grand Theft Auto 3"))


def extract_gtavc(vc, steam_dir):
    with ZipFile(vc, 'r') as zipObj:
        zipObj.extractall(os.path.join(steam_dir, "steamapps", "common", "Grand Theft Auto Vice City"))


def extract_files(three, vc, steam_dir):
    extract_gta3(three, steam_dir)
    extract_gtavc(vc, steam_dir)
