import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import games
from config import ERR

def initBot(bot, message):
    return 'test'

def game(bot, message):
    command = message.content.split(" ")
    if bot["channel"] != None:
        if command[2] == "speed_dating":
            bot["game"] = games["speed_dating"]
            return bot["game"]["tutorial"]
        else:
            return ERR["NO_GAME"]
    else:
        return ERR["NOT_INIT"]

def start(bot, message):
    command = message.content.split(" ")
    if bot["channel"] != None:
        if bot["game"] != None:
            return bot["game"]["start"](bot, message)
        else:
            return ERR["NO_GAME_SELECTED"]
    else:
        return ERR["NO_INIT"]

