import sys
import asyncio
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import *

players_map = {}

async def roundEndedTask(bot, message):
    await asyncio.sleep(10)
    await message.channel.send("Round ended. Hope you made some friends! :) To start a new round, run !mitra start.")
    bot["active_speed_dating_round"] = False

def start(bot, client, message):
    if bot["active_speed_dating_round"]:
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
        bot["active_speed_dating_round"] = True
        client.loop.create_task(roundEndedTask(bot, message))

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

def pair_players(player_map, players):
    # if len(players_map[players[0]]) == len(players):
    #     return None

    groups = []

    for i,speaker in enumerate(players):
        for j,talker in enumerate(players):
            if talker not in players_map[speaker]:
                players_map[speaker].append(talker)
                players_map[talker].append(speaker)
                groups.append([talker, speaker])
                players.remove(talker)
                players.remove(speaker)
                break
    return groups
