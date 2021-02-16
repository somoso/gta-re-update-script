import winreg
import platform
from re_common import get_config


def get_steam_dir():
    st_dir = None
    if platform.system() == "Windows":
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        try:
            key = winreg.OpenKey(reg, r"SOFTWARE\Wow6432Node\Valve\Steam")
            st_dir = winreg.QueryValueEx(key, "InstallPath")[0]
        except OSError:
            key = winreg.OpenKey(reg, r"SOFTWARE\Valve\Steam")
            st_dir = winreg.QueryValueEx(key, "InstallPath")[0]

    if st_dir is None:
        config = get_config("steam")
        if "steam" in config and "dir" in config["steam"]:
            st_dir = config["dir"]

    return st_dir