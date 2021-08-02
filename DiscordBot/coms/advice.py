import discord
from discord.ext import commands

# after imports \/
import json
import requests

# command types [Funny, Tools]
class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # stupid fucking apostrophies holy fuck
    # give advice
    @commands.command()
    async def advice(self, ctx):
        URL = "https://api.adviceslip.com/advice"
        r = requests.get(url=URL)
        unga = r.text
        obj = json.loads(str(unga))
        await ctx.send(str(obj["slip"]["advice"]).upper())


def setup(bot):
    bot.add_cog(Funny(bot))
