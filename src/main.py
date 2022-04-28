import discord
import pickle
from fixpunct import fixpunctuation
from NE import NESampler

with open('out/pipe.p', 'rb') as fp:
    pipe = pickle.load(fp)

channels = open('id/channelID.txt', 'r+')
i = 0
num = i
client = discord.AutoShardedClient()

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_message(message):

    if message.author == client.user: return

    print(f'{message.guild} [{message.channel.name}] | {message.author}: {message.content}')

    if message.content.startswith('C ') or message.content.startswith('c '):
        if message.author.id == 'admin-aka-you-id' or message.channel.id in channels.read():
            mod = message.content[2:]
            p_resp = pipe.predict([mod])
            response = fixpunctuation(p_resp[0])
            print(f'reply: {response}')
            await message.channel.send(response)

    if message.content == '!add_channel':
        if 'napi' in [y.name.lower() for y in message.author.roles] or message.author.id == 261579086856585226:
            if message.channel.id in channels.read():
                message.author.send('you already have this channel added!')
                print('channel added error')
            else:
                channels.write(f'{message.channel.id}\n')
                print('channel added.')
                await message.channel.send('channel added!!')


client.run('token goes here')
