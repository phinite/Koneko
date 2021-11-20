import json
import random
import discord
from discord.ext import commands
from requests import get
from math import floor

nekoapi = "https://nekos.life/api/v2/img/"


class ToyBox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = 'howgay')
    async def howgay(self, ctx, who: discord.User = None):
        user = ctx.author if who == None else who
        gay_level = floor( random.randint(1, 101) / 4 )
        meter = f"[{'I'*gay_level}{'.'*(25-gay_level)}] :rainbow_flag:"
        embed = discord.Embed(title="Gay Meter", color=0x22ffdd, \
                description = f"{user.mention} is {gay_level*4}% gay!\n{meter}")
        await ctx.channel.send(embed = embed)
        
            


class Interactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = 'hug')
    async def hug(self, ctx, who: discord.User = None):
        if who is None:
            await ctx.channel.send("Who do you want to hug, nya?")
            return
        elif who == ctx.author:
            embed = discord.Embed(description="Poor thing ~I'll give you a hug~ <3", color=0x55ccff)
        else:
            embed = discord.Embed(description=f"{ctx.author} gave {who.mention} a hug! Awww~", color=0x55ccff)
        img = get(f'{nekoapi}hug').json()['url']
        embed.set_image(url = img)
        await ctx.channel.send(embed = embed)

    @commands.command(name = 'kiss')
    async def kiss(self, ctx, who: discord.User = None):
        if who is None:
            await ctx.channel.send("Who do you want to kiss, nya?")
            return
        elif who == ctx.author:
            await ctx.channel.send("You cant kiss yourself, nya :face_with_raised_eyebrow:")
            return
        img = get(f'{nekoapi}kiss').json()['url']
        embed = discord.Embed(description=f"{ctx.author} gave {who.mention} a kiss! Awww~", color=0xff317f)
        embed.set_image(url = img)
        await ctx.channel.send(embed = embed)



    @commands.command(name = 'pat')
    async def pat(self, ctx, who: discord.User = None):
        if who is None:
            await ctx.channel.send("Who do you want to pat, nya?")
            return
        elif who == ctx.author:
            embed = discord.Embed(description="Poor thing ~Here's a pat~ <3", color=0x55ccff)
        else:
            embed = discord.Embed(description=f"{ctx.author} patted {who.mention}! >w<", color=0x55ccff)
        img = get(f'{nekoapi}pat').json()['url']
        embed.set_image(url = img)
        await ctx.channel.send(embed = embed)
    

    @commands.command(name = 'neko', aliases = ["cat, kitty, koneko"])
    async def neko(self, ctx):
        img = get(f'{nekoapi}meow').json()['url']
        embed = discord.Embed(description="Heres a handsome neko ^owo^", color=0xbb00aa)
        embed.set_image(url = img)
        await ctx.channel.send(embed = embed)



def setup(bot):
    bot.add_cog(Interactions(bot))
    bot.add_cog(ToyBox(bot))
