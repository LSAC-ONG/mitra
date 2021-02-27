# bot.py
import os
import discord
from commands import init_bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

bot = {
    "channel": None,
    "game": None,
}

commandsFunctions = {
    'init': init_bot.initBot,
    'disconnect': init_bot.disconnect,
    'game': init_bot.game,
    'start': init_bot.start
}

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!mitra '):
        command = message.content.split(' ')

        if command[1] in commandsFunctions:
            response = await commandsFunctions[command[1]](bot, message)

            if response != None:
                await message.channel.send(response)
        else:
            await message.channel.send(f"!mitra {command[1]} is not a recognized command!")

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    online_users = list(filter(
        lambda m : m.status != discord.Status.offline,
        guild.members
    ))

    members = '\n - '.join([member.name for member in online_users])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)