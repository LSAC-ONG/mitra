async def create_and_move(channels, message):
    for i,channel in enumerate(channels):
        voice_channel = await message.guild.create_voice_channel(f"Mitra_Room_{i+1}")
        for member in channel:
            await member.move_to(voice_channel)