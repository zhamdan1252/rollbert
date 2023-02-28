from botCmds import rolling
from botCmds import spells
import config

import discord
import random
import os
import requests
import json


TOKEN = "MTA3ODc4Njk0MzU1NjUyMjA0NQ.GzEXyc.WjqdH9zEWqg_Rof0EByC22UA0avKXAR8aaabAA"
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    userMessage = str(message.content)
    channel = str(message.channel.name)

    if (message.author == client.user):
        return

    if message.channel.name == 'dice-rolling':

        if userMessage.lower().startswith("!roll"):
            print(f'{username}: {userMessage} ({channel})')
            await message.channel.send(rolling.roll(userMessage))

        if userMessage.lower().startswith('!spell'):
            spellName = userMessage.lower().split("!spell", 1)
            spellName = spellName[1].split(" ")
            spellName = spellName[1:]
            spellName = "-".join(map(str, spellName))
            await message.channel.send(spells.getSpell(spellName))


client.run(config.TOKEN)