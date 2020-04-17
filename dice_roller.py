#!/usr/bin/env python3

import discord
import random
import json

def roll(die):
    result = [random.randint(1,int(die[1])) for i in range(int(die[0]))]
    return result + [sum(result)]

def array2str(arr):
    st = ''
    for value in arr:
        st += f' [{value}] '
    return st

def DiceRoller():
    # pylint: disable=unused-variable

    with open('token.json','r') as f:
        TOKEN = json.load(f)['token']

    client = discord.Client()

    @client.event
    async def on_message(message):

        # Get user name
        id = message.author.id   
        name = message.server.get_member(id).nick

        # Get message content
        content = message.content

        if message.author == client.user:
            return

        if message.content.startswith('!rollf'):
            try:
                die = ['-', '-', ' ', ' ', '+', '+']
                result = [random.choice(die) for i in range(4)]
                res = 0
                for i in result:
                    if i == '+':
                        res += 1
                    elif i == '-':
                        res -= 1
                msg = f'{name} rolled {res} ({array2str(result)}).'
                await client.send_message(message.channel, msg)
            except:
                await client.send_message(message.channel, 'Invalid roll.')
                return
        elif message.content.startswith('!roll help'):
            msg = 'Commands:\n+ !rollf: Rolls 4df\n+ !roll <n>d<k>: Rolls k sided die n times. ex: !roll 2d5\n'
            await client.send_message(message.channel, msg)
        elif message.content.startswith('!roll'):
            try:
                die = content.split(' ')[1].split('d') # Getting die information
                result = roll(die)
                msg = f'{name} rolled {result[-1]} ({array2str(result[:-1])}).'
                await client.send_message(message.channel, msg)
            except:
                await client.send_message(message.channel, 'Invalid roll.')
                return

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
    
    client.run(TOKEN)


if __name__ == "__main__":
    DiceRoller()
