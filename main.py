#Author: spasemax0
#main section of discord bot, declares intents and creates events, customize as needed
import discord
import os
from generate_text import generate_text

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$generate_text'):
        prompt = message.content[14:]
        response = generate_text(prompt)
        await message.channel.send(response)

client.run('bot token here, or put the bot token in .env file and call it here for extra security')
