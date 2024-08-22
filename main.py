import discord
from commands import *
from discord.ext import commands
import os

DISCORD_API_KEY = os.environ['DISCORD_API_KEY']

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

client.add_command(ping)
client.run(DISCORD_API_KEY)
