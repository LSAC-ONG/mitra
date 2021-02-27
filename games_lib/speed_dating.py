import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../config.py')

from config import *
import time, threading
import asyncio

players_map = {}

def start(bot, client, message):
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

    pairs = ""
    for group in groups:
        for user in group:
            pairs = pairs + user.name + " "
        pairs = pairs + "\n"

    response = "started game: " + bot["game"]["name"] + "\n" + pairs
    
    return response

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
