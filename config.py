from games_lib import speed_dating
from games_lib import online_games
from games_lib import pc_games

games = {
    'speed-dating': {
        'name': "Speed dating",
        'tutorial': "Pair with a random person form this channel and talk about anything for 10 minutes!",
        "time": 5,
        "pairs": None,
        "start": speed_dating.start
    },
    'minecraft': {
        'name': "Minecraft",
        'tutorial': "Generated rooms for playing Minecraft.",
        "time": 5,
        "pairs": None,
        "start": pc_games.start
    },
    'cs-go': {
        'name': "Counter-Strike: Global Offensive",
        'tutorial': "Generated rooms for playing Counter-Strike: Global Offensive.",
        "time": 5,
        "pairs": None,
        "start": pc_games.start
    },
    'skribbl': {
        'name': "Skribbl",
        'tutorial': "Generated rooms for playing Skribbl.\n\nLink: https://skribbl.io/",
        "time": 5,
        "pairs": None,
        "start": online_games.start
    }
}

ERR = {
    "NO_INIT": "Mitra is not initialised, to start Mitra functionality use \n!mitra init\nwhile connected to a voice channel",
    "NO_GAME_SELECTED": "Mitra doesnt have any game selected, use !mitra list to see available games",
    "NO_GAME": "Mitra could not find this game, use !mitra list to see available games",
    "NO_VOICE": "Please join a voice channel first!",
    "ALREADY_VOICE": "Can't disconnect if not already assigned to a voice channel"
}
