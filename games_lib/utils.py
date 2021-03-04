async def create_and_move(bot, channels, message):
    rooms = bot["rooms"]
    while len(rooms) < len(channels):
        voice_channel = await message.guild.create_voice_channel(f"Mitra_Room_{len(rooms) + 1}")
        bot["rooms"].append(voice_channel)

    for i, channel in enumerate(channels):
        for member in channel:
            await member.move_to(bot["rooms"][i])

async def move_back(channel, groups):
    for group in groups:
        for member in group:
            await member.move_to(channel)

async def end_session(bot):
    bot["session"] = False
    channels = bot["rooms"]
    while len(channels) > 0:
        await channels[0].delete()
        channels.remove(channels[0])