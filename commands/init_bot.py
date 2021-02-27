import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import games
from config import ERR

async def initBot(bot, client, message):
    voice = message.author.voice

    if voice != None and voice.channel != None:
        voice_client = await voice.channel.connect()
        bot['channel'] = voice_client
        return 'Successfuly connected to channel!'

    return ERR["NO_VOICE"]

async def disconnect(bot, client, message):
    if bot['channel'] != None:
        await bot['channel'].disconnect()
        bot['channel'] = None
        return 'Hope you had fun! Mitra going dark...'

    return ERR["ALREADY_VOICE"]

async def game(bot, client, message):
    command = message.content.split(" ")
    if bot["channel"] != None:
        if command[2] == "speed_dating":
            bot["game"] = games["speed_dating"]
            return bot["game"]["tutorial"]
        else:
            return ERR["NO_GAME"]
    else:
        return ERR["NO_INIT"]

async def start(bot, client, message):
    command = message.content.split(" ")
    if bot["channel"] != None:
        if bot["game"] != None:
            return bot["game"]["start"](bot, client, message)
        else:
            return ERR["NO_GAME_SELECTED"]
    else:
        return ERR["NO_INIT"]