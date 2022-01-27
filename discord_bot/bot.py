#!/usr/bin/python
# bot.py
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import date
import threading
import aiofiles
import json
import aiohttp
from io import BytesIO
global members, memelist, creds, squad_names, orders_list, exclude_list


intents = discord.Intents.default()
intents.typing = False
intents.members = True
intents.reactions = True
intents.messages = True
intents.guilds =True

def get_prefix(client, message):
    prefixes = ['12!'] # Allow multiple prefixes
    if not message.guild:
        prefixes = ['12!'] # Only respond to this prefix in direct messages
    return commands.when_mentioned_or(*prefixes)(client, message) # Allow @Bot to trigger commands

cogs = ['cogs.teams']
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=get_prefix, description='CFB Risk Service Bot',intents=intents)

# Print ready message and load cogs.
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
bot.run(TOKEN, bot=True, reconnect=True)