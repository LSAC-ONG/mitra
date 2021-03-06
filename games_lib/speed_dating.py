import sys
import asyncio
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import *
from .utils import create_and_move
from .utils import move_back

import time, threading
import random

players_map = {}

async def roundEndedTask(bot, message, groups):
    await asyncio.sleep(10)
    await message.channel.send("Round ended. Hope you made some friends! :) To start a new round, run !mitra start.")
    bot["active_speed_dating_round"] = False
    await move_back(bot["channel"].channel, groups)

async def start(bot, client, message):
    if bot["active_speed_dating_round"]:
        return "Round already in progress. Please wait :)"

    players = get_players(bot, client)
    
    for player in players:
        if player not in players_map:
            players_map[player] = []
            #players_map[player].append(player)
    
    groups, players = pair_players(players_map, players)

    if len(players) == 1:
        groups[-1].append(players[0])
        player = players[0]
        for existing_player in groups[-1]:
            players_map[existing_player].append(player)
            players_map[player].append(existing_player)

    if len(groups) > 0:
        await create_and_move(bot, groups, message)
        bot["active_speed_dating_round"] = True
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

def extract_pair(players):
    for speaker in players:
        for talker in players:
            if talker not in players_map[speaker] and talker != speaker:
                players_map[speaker].append(talker)
                players_map[talker].append(speaker)
                pair = [talker, speaker]
                players.remove(talker)
                players.remove(speaker)
                return pair, players
    return (None, [])          

# this could be done WAY smarter, but because it's a hackathon
# we decided to stick with this very barbaric way :)
def pair_players(player_map, players):
    global players_map
    backup_players_map = players_map
    backup_players = players
    maxlen = 0
    longest_match = [[]]
    longest_match_players = []

    for i in range(20):
        groups = []
        random.shuffle(players)

        while len(players) > 1:
            pair, players = extract_pair(players)
            if pair != None:
                groups.append(pair)

        if len(groups) > maxlen:
            maxlen = len(groups)
            longest_match = groups
            longest_match_players = players

        players = backup_players
        players_map = backup_players_map

    return longest_match, longest_match_players
