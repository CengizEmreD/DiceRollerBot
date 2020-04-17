#!/usr/bin/env python3

import discord
import random
import json

def DiceRoller():
    # pylint: disable=unused-variable

    with open('token.json','r') as f:
        TOKEN = json.load(f)['token']

    client = discord.Client()

    @client.event
    async def on_message(message):

        # id = message.author.id   # TODO Will use to include username in the message
        
        if message.author == client.user:
            return

        if message.content.startswith('!rollf'):
            try:
                dice = ['-', '-', ' ', ' ', '+', '+']
                msg = f'Rolled [{random.choice(dice)}][{random.choice(dice)}][{random.choice(dice)}][{random.choice(dice)}]'
                await client.send_message(message.channel, msg)
            except:
                return
        elif message.content.startswith('!rolld'):
            pass


    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
    
    client.run(TOKEN)


if __name__ == "__main__":
    DiceRoller()
