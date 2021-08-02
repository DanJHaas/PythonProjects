import discord
from discord.ext import commands

# after imports \/

# command types [Funny, Tools]
class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # https://github.com/HattyH124/PythonProjects
    @commands.command()
    async def github(self, ctx):
        await ctx.send("https://github.com/HattyH124/PythonProjects")


def setup(bot):
    bot.add_cog(Tools(bot))
