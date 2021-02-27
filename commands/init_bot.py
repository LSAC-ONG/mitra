async def initBot(bot, message):
    voice = message.author.voice

    if voice != None and voice.channel != None:
        voice_client = await voice.channel.connect()
        bot['channel'] = voice_client
        return 'Successfuly connected to channel!'

    return 'Please join a voice channel first!'

async def disconnect(bot, message):
    if bot['channel'] != None:
        await bot['channel'].disconnect()
        bot['channel'] = None
        return 'Hope you had fun! Mitra going dark...'

    return 'Can\'t disconnect if not already assigned to a voice channel'

def game(bot, command):
    pass
