import discord
from discord.ext import commands
import os
from src.cml_account import CMLAccountManager
import json

DISCORD_API_KEY = os.environ['DISCORD_API_KEY']
DB_USERNAME = 'web'
DB_PASSWORD = os.environ['DISCORD_BOT_DB_PASSWORD']

cml_manager = CMLAccountManager(DB_USERNAME, DB_PASSWORD)

if __name__ == '__main__':
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix='/', intents=intents)

    from src.commands import ping, bind
    client.add_command(ping)
    client.add_command(bind)
    client.run(DISCORD_API_KEY)
