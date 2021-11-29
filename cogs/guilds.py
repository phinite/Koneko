import discord.py
from discord.ext import commands
import json

database = 'db.json'

class GuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.event()
    async def on_guild_join(self, guild_x):
        db = db_read(database)
        for guild in db['guilds']:
            if guild['id'] == guild_x.id:
                return
        df = db_read("default.json")
        df = df['guild'] = int(guild_x.id)
        db['guilds'].append(df)
        db_write(database, db)

    def db_write(db, guild_dict):
        with open(db, "w") as d:
            json.dumps(guild_dict, d)

    def db_read(db):
        with open(db,"r") as d:
            return json.loads(d.read())

def setup(bot):
    bot.add_extension(GuildJoin(bot))
