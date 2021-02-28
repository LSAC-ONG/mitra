import sys
import asyncio
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import *
from .utils import create_and_move
from .utils import move_back

import time, threading

players_map = {}

async def roundEndedTask(bot, message, groups):
    await asyncio.sleep(600)
    await message.channel.send("Round ended! Hope you made some friends! :) To start a new round, run !mitra start.")
    bot["session"] = False
    await move_back(bot["channel"].channel, groups)

async def start(bot, client, message):
    if bot["session"]:
        return "Round already in progress. Please wait :)"

    players = get_players(bot, client)
    
    for player in players:
        if player not in players_map:
            players_map[player] = []
        players_map[player].append(player)
    
    groups = pair_players(players_map, players)

    if len(players) == 1:
        groups[-1].append(players[0])
        player = players[0]
        for existing_player in groups[-1]:
            players_map[existing_player].append(player)
            players_map[player].append(existing_player)

    if len(groups) > 0:
        await create_and_move(bot, groups, message)
        bot["session"] = True
        client.loop.create_task(roundEndedTask(bot, message, groups))

    pairs = ""
    for group in groups:
        for user in group:
            pairs += user.name + ', '
        pairs += '\n'

    if len(groups) == 0: 
        pairs = "No more possible allocations. Everyone should know each other now :)"
    
    return f"Started game: {bot['game']['name']}\n{pairs}"

def get_players(bot, client):
    channel = bot["channel"].channel

    online_users = list(filter(
        lambda m : m != client.user,
        channel.members
    ))
    return online_users

def roundEnded(bot, client, message, time):
    #collectPlayersBack(get_players(bot, client))

    message.channel.send("Round ended, to start next round use !mitra start")

def pair_players(player_map, players):
    # if len(players_map[players[0]]) == len(players):
    #     return None

    groups = []

    for speaker in players:
        for talker in players:
            if talker not in players_map[speaker] and speaker != talker:
                groups.append([talker, speaker])
                players_map[speaker].append(talker)
                players_map[talker].append(speaker)
                players.remove(talker)
                players.remove(speaker)
                break
    return groups