import sys
import asyncio
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import *
from .utils import create_and_move
from .utils import move_back
from random import choice

import time, threading

players_map = {}

async def roundEndedTask(bot, message, groups):
    await message.channel.send("Let's start games! :)")
    bot["session"] = False

async def start(bot, client, message):
    if bot["session"]:
        return "Round already in progress. Please wait :)"

    players = get_players(bot, client)
    
    groups = pair_players(players)

    if len(groups) > 0:
        await create_and_move(bot, groups, message)

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

def pair_players(players):
    groups = []

    while players:
        pair = []

        user1 = choice(players)
        players.remove(user1)
        pair.append(user1)
        if players:
            user2 = choice(players)
            players.remove(user2)
            pair.append(user2)
        if players:
            user3 = choice(players)
            players.remove(user3)
            pair.append(user3)
        if players:
            user4 = choice(players)
            players.remove(user4)
            pair.append(user4)

        groups.append(pair)

    return groups