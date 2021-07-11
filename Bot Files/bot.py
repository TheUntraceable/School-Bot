import discord
import json
import os

from discord.ext import commands

bot = commands.Bot(command_prefix="sir, ",intents = discord.Intents.all())

try:
    with open("config.json","r") as f:
        CurrentData = json.load(f)
except KeyError:
    print("Make sure you add data to config.json!")
    exit()


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.fil{file[:-3]}")

bot.run("token")