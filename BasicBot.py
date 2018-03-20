# -*- coding: utf-8 -*-
# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
from random import randint
from random import choice
from PyLyrics import *
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import wikipedia
# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="21Savage#1665", command_prefix="21", pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Usemessage.content[3:] this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Support Discord Server: https://discord.gg/FNNNgqb')
    print('Github Link: https://github.acom/Habchy/BasicBot')
    print('--------')
    print('You are running 21Savage v2.1') #Do not change this. This will really help us support you, if you need support.
    print('Created by 21Savage#1665')
    return await client.change_presence(game=discord.Game(name='PLAYING ROCKSTAR')) #This is buggy, let us know if it doesn't work.

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

    await client.say("I got 1 2 3 4 5 6 7 8 shooters ready to gun you down!")
    await asyncio.sleep(3)
    await client.say("I got 1 2 3 4 5 6 7 8 digits in my bank account")

@client.event
async def on_message(message):
    if message.content.startswith('!gangmessages'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} GANG messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping on dem haters')

    elif message.content.startswith('!21'):
        await client.send_message(message.channel, 'I got')
        x = 1
        while (x != 9):
            await asyncio.sleep(0.6)
            await client.send_message(message.channel, str(x))
            x += 1

        await asyncio.sleep(0.6)
        if randint(2, 3) == 2:
            comment = "Shooters ready to gun you down!"
        else:
            comment = "Digits in mah bank account!"
        await client.send_message(message.channel, comment)

    elif message.content.startswith('!flip'):
        await client.send_message(message.channel, 'Flipping...')
        await client.send_message(message.channel, choice(['Kruuna', 'Klaava']))

    elif message.content.startswith('!wp'):
        if message.content[3:]:
            try:
                await client.send_message(message.channel, wikipedia.summary(str(message.content[3:]), sentences=1))
            except:
                await client.send_message(message.channel, "Can't find the TING you are looking for\nReason: Irrelevant")
        else:
            await client.send_message(message.channel, "I need input bitch")

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, "COMMANDS YOU CAN USE\n!gangmessages = Displays GANGmessages\n!sleep = SLEEPS on dem haters\n!21 = Displays the best LYRICS of 2018\n!flip = FLIPS a coin\n!wp = Searches from WIKIPEDIA")

    elif message.content.startswith('!guess'):
        if message.content[6:]:
            try:
                answer = randint(1, 100)
                guess = message.content[3:]
                if guess == answer:
                    await client.send_message(message.channel, "YOU WON!!! Answer was:" + str(answer))
                elif guess < str(answer):
                    await client.send_message(message.channel, "You were too high :) \nAnswer:" + str(answer))
                elif guess > str(answer):
                    await client.send_message(message.channel, "You were too low :)) \nAnswer:" + str(answer))
                else:
                    await client.send_message(message.channel, "wtf did you do cuz i dont know")
            except Exception as e:
                await client.send_message(message.channel, "WTF DUDE " + str(e))
        else:
            await client.send_message(message.channel, "Guess works like this !guess [number] it has to be in the range from 1-100")

    elif message.content.startswith('!albums'):
        if message.content[7:]:
           try:
               user = message.content[7:]
               albums = PyLyrics.getAlbums(str(user))
               await client.send_message(message.channel, albums)
           except Exception as e:
                 await client.send_message(message.channel, "You did something wrong\n" + str(e))
        else:
             await client.send_message(message.channel, "Search for your artist like this\n !albums Post Malone")
# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.

client.run('NDE0Mzc5OTg3NDA0MzI0ODc0.DWmihw.76GQrIkWn4QkcSd2P1M_UmxISRY')

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
