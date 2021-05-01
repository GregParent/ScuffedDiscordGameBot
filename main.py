# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import discord
import json

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

with open('token.json') as json_file:
    token_json = json.load(json_file)
    token = token_json['token']
client.run(token)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
