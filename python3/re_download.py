import tempfile
import os
from urllib.request import urlretrieve
from re_common import get_config

def download_files():
    t_dir = tempfile.gettempdir()
    three = download_gta3_rc(t_dir)
    vc = download_gtavc_rc(t_dir)
    return three, vc


def download_gta3_rc(temp):
    config = get_config("rc")
    if not ("rc" in config and "three" in config["rc"]):
        print("rc.ini file needs to have two entries under [rc]: 'three' and 'vc' pointing to builds")
        exit(1)
    url = config["rc"]["three"]
    dst = os.path.join(temp, "gta3.zip")
    urlretrieve(url, dst)
    return dst


def download_gtavc_rc(temp):
    config = get_config("rc")
    if not ("rc" in config and "three" in config["rc"]):
        print("rc.ini file needs to have two entries under [rc]: 'three' and 'vc' pointing to builds")
        exit(1)
    url = config["rc"]["vicecity"]
    dst = os.path.join(temp, "gtavc.zip")
    urlretrieve(url, dst)
    return dst
