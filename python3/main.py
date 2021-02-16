from re_find_steam import get_steam_dir
from re_download import download_files
from re_extract import extract_files


def download_re_updates():
    steam_dir = get_steam_dir()
    if steam_dir is None:
        print("Steam folder not found.")
        exit(1)
    (three, vc) = download_files()
    extract_files(three, vc, steam_dir)


if __name__ == '__main__':
    download_re_updates()
