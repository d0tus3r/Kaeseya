import configparser
from os import path

CONFIG = configparser.ConfigParser()
CONFIG.read(path.expanduser('~/.bms.ini'))
