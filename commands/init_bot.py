import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import games
from config import ERR

commands = [
    "init - ",
    "status - ",
    "help - ",
    "disconnect - ",
    "game - ",
    "start - "
]

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
        if command[2] == "speed-dating":
            bot["game"] = games["speed-dating"]
            return bot["game"]["tutorial"]
        elif command[2] == "skribbl":
            bot["game"] = games["skribbl"]
            return bot["game"]["tutorial"]
        elif command[2] == "cs-go":
            bot["game"] = games["cs-go"]
            return bot["game"]["tutorial"]
        elif command[2] == "minecraft":
            bot["game"] = games["minecraft"]
            return bot["game"]["tutorial"]
        else:
            return ERR["NO_GAME"]
    else:
        return ERR["NO_INIT"]

async def start(bot, client, message):
    command = message.content.split(" ")
    if bot["channel"] != None:
        if bot["game"] != None:
            return await bot["game"]["start"](bot, client, message)
        else:
            return ERR["NO_GAME_SELECTED"]
    else:
        return ERR["NO_INIT"]

async def status(bot, client, message):
    if bot["channel"] is None:
        channel_name = "Not connected"
    else:
        channel_name = bot["channel"].channel.name

    if bot["game"] is None:
        game_selected = "No game selected"
    else:
        game_selected = bot["game"]["name"]
    response = "Status: \n" + "Active on: " + channel_name + "\nGame selected: " + game_selected
    return response


async def list_games(bot, client, message):
    response = "Available games: "
    for game in games:
        response = response + "\n" + str(game)
    return response

async def help(bot, client, message):
    response = "Available commands: \n"
    for command in commands:
        response = response + command + "\n"
    return response

async def reset(bot, client, message):
    bot["session"] = False
    channels = bot["rooms"]
    while len(channels) > 0:
        channels.remove(channels[0])
        await channels[0].delete()
    return "Everything clear"