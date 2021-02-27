import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import *

def start(bot, message):
    return "started game: " + bot["game"]["name"]
