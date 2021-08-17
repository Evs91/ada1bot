import discord
from discord.ext.commands import Bot
from discord import Intents
import os


intents = Intents.all()

#configure bot
bot = Bot(intents=intents, command_prefix='|') #this is a pipe btw

#read tokens for APIs
discord_token = open('/var/run/secrets/discord_bot_token','r').read()
bungie_token = open('/var/run/secrets/bungie_api_token','r').read()








#run Ada1Bot on Discord
bot.run(discord_token)
