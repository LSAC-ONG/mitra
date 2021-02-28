from games_lib import speed_dating
from games_lib import skribbl
from games_lib import minecraft
from games_lib import cs_go

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
        "start": minecraft.start
    },
    'cs-go': {
        'name': "Counter-Strike: Global Offensive",
        'tutorial': "Generated rooms for playing Counter-Strike: Global Offensive.",
        "time": 5,
        "pairs": None,
        "start": cs_go.start
    },
    'skribbl': {
        'name': "Skribbl",
        'tutorial': "Generated rooms for playing Skribbl.\n\nLink: https://skribbl.io/",
        "time": 5,
        "pairs": None,
        "start": skribbl.start
    }
}

ERR = {
    "NO_INIT": "Mitra is not initialised, to start Mitra functionality use \n!mitra init\nwhile connected to a voice channel",
    "NO_GAME_SELECTED": "Mitra doesnt have any game selected, use !mitra list to see available games",
    "NO_GAME": "Mitra could not find this game, use !mitra list to see available games",
    "NO_VOICE": "Please join a voice channel first!",
    "ALREADY_VOICE": "Can't disconnect if not already assigned to a voice channel"
}
