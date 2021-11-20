import discord
from discord.ext import commands


class Administration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name = 'purge')
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, limit: int = None):
        limit = 100 if limit is None else int(limit)
        await ctx.channel.purge(limit = limit)
        print(f"purged {limit} in {ctx.guild.name}")


    @commands.command(name = 'ban')
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, who: discord.User = None, *, reason = None):
        if who is None:
            await ctx.channel.send("Must specify who to ban")
            return
        await who.ban(reason = reason)
        await ctx.channel.send(f"{who.mention} was banned for \"{reason}\"")
    

    @commands.command(name = 'kick')
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, who: discord.User = None, *, reason = None):
        if who is None:
            await ctx.channel.send("Must specify who to ban")
            return
        await who.kick(reason = reason)
        await ctx.channel.send(f"{who.mention} was kicked for \"{reason}\"")


def setup(bot):
    bot.add_cog(Administration(bot))
