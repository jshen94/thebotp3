import discord
import asyncio
import builder
import generator
import random
from sympy import sympify

client = discord.Client()
token = 'Mjk3MTIwOTIwNzU2MTU4NDY0.C78LBA.UBxJvvNEFp1VzNCkvTVMw7sDm5o'


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('----------')


@client.event
async def on_message(message):
    commands = {'!test': 'Display the number of messages a user has posted\n',
                '!hello': 'is it me you\'re looking for\n',
                '!generate': 'creates a sequence of words based on the text the user has written\n',
                '!sleep': 'chills for a bit\n'}
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!hello'):
        msg = 'is it me you\'re looking for, {0.author.name}'
        await client.send_message(message.channel, msg.format(message))

    elif message.content.startswith('!generate'):
        num = message.content[9:].strip()
        try:
            num = int(num)
        except TypeError:
            num = 30
        file = open("user_log.txt", "w+")
        tmp = await client.send_message(message.channel, 'Generating messages...')
        async for log in client.logs_from(message.channel, limit=200):
            if log.author == message.author and not log.content.startswith('!'):
                file.write(log.content)
                file.write('\n')
        file.close()
        await client.edit_message(tmp, 'Building sequence....')
        chain = builder.build('user_log.txt')
        output = generator.generate(chain, randomizer, num, builder.NONWORD)
        await client.edit_message(tmp, output)

    elif message.content.startswith('!permissions'):
        await client.send_message(message.channel, message.channel.permissions_for(message.author))

    elif message.content.startswith('!summon'):
        gates = {'Rainbow': 'http://4.bp.blogspot.com/-Ee72-k33HtM/VD5fWC4EecI/AAAAAAAABFg/sPM_wwL4kkg/s1600/Screenshot_2014-09-06-01-56-56.png',
                 'Black': 'http://i.imgur.com/VCwiDSU.png'}
        await client.send_message(message.channel, gates['Black'])

    elif message.content.startswith('!commands'):
        await client.send_message(message.channel, str(commands))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')


def randomizer(bound):
    return random.randint(1, bound)


client.run(token)
