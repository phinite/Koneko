import discord
import asyncio
import json

from discord import channel
from discord.ext import commands


with open("token.json", "r") as tk:
    token = json.loads(tk.read())
    tk.close()

bot = commands.Bot(command_prefix = ";;", help_command = None)
cogs_list = { "cogs.admin", "cogs.fun" }


if __name__ == '__main__':
    for cog in cogs_list:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f"\nCouldn't load cog {cog}:\t{e}")

@bot.event
async def on_ready():
    print("Ready.")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, \
            name=f"for ;;"), status=discord.Status.online)

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    await bot.process_commands(ctx)

bot.run(token['token'])
