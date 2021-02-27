async def create_and_move(bot, channels, message):
    rooms = bot["rooms"]
    while len(rooms) < len(channels):
        voice_channel = await message.guild.create_voice_channel(f"Mitra_Room_{len(rooms) + 1}")
        bot["rooms"].append(voice_channel)


    for i, channel in enumerate(channels):
        for member in channel:
            await member.move_to(bot["rooms"][i])