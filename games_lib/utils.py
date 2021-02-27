async def create_and_move(channels, message):
    for i,channel in enumerate(channels):
        voice_channel = await message.guild.create_voice_channel(f"Mitra_Room_{i+1}")
        for member in channel:
            await member.move_to(voice_channel)

async def move_back(channel, groups):
    for group in groups:
        for member in group:
            await member.move_to(channel)