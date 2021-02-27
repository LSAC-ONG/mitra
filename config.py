from games_lib import speed_dating

games = {
    'speed_dating': {
        'name': "Speed dating",
        'tutorial': "Pair with a random person form this channel and talk about anything for 10 minutes",
        "time": 5,
        "pairs": None,
        "start": speed_dating.start
    },
    'pacpac': {
        'name': "XD",
        'tutorial': "Pair with a random person form this channel and talk about anything for 10 minutes",
        "time": 5,
        "pairs": None,
        "start": None
    },
    'xd': {
        'name': "XD",
        'tutorial': "Pair with a random person form this channel and talk about anything for 10 minutes",
        "time": 5,
        "pairs": None,
        "start": None
    }
}

ERR = {
    "NO_INIT": "Mitra is not initialised, to start Mitra functionality use \n!mitra init\nwhile connected to a voice channel",
    "NO_GAME_SELECTED": "Mitra doesnt have any game selected, use !mitra list to see available games",
    "NO_GAME": "Mitra could not find this game, use !mitra list to see available games",
    "NO_VOICE": "Please join a voice channel first!",
    "ALREADY_VOICE": "Can't disconnect if not already assigned to a voice channel"
}
