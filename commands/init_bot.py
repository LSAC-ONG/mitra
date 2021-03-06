import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import games
from config import ERR

commands = [
    "init - connects Mitra to the voice channel you are in",
    "status - displays the status of the bot(selected game and channel connected to)",
    "help - displays the list of available commands",
    "list - displays the list of available commands",
    "disconnect - disconnect Mitra from your voice channel",
    "game name_of_game - tells Mitra that you are going to play name_of_game",
    "start -  Mitra will start the selected game for you"
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
        if command[2] == "speed_dating":
            bot["game"] = games["speed_dating"]
            return bot["game"]["tutorial"]
        elif command[2] == "skribbl":
            bot["game"] = games["skribbl"]
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
    channels = bot["rooms"]
    while len(channels) > 0:
        await channels[0].delete()
        channels.remove(channels[0])
    return "Everything clear"