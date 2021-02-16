import configparser


def get_config(file):
    ini_parse = configparser.ConfigParser()
    ini_parse.read(f"{file}.ini")
    return ini_parse
