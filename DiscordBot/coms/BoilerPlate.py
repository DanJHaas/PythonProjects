import discord
from discord.ext import commands

# after imports \/

# command types [Funny, Tools]
class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Funny(bot))
