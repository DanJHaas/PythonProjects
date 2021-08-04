import discord
from discord.ext import commands

# after imports \/
import json
import requests
import HatFunctions
from datetime import datetime

# command types [Funny, Tools]
class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # rand facts about space TODO #1
    # https://api.wheretheiss.at/v1/satellites/25544
    @commands.command()
    async def spacefacts(self, ctx):

        URL = "https://api.wheretheiss.at/v1/satellites/25544"
        r = requests.get(url=URL)
        unga = r.text
        obj = json.loads(str(unga))

        epochTime = datetime.utcfromtimestamp(int(obj["timestamp"])).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        text1 = {
            "Timestamp": epochTime,
            "Longitude": obj["longitude"],
            "Latitude": obj["latitude"],
            "Altitude (km)": obj["altitude"],
            "Velocity (km/h)": obj["velocity"],
            "Visibility": obj["visibility"],
        }
        embedVar = discord.Embed(
            title=str(obj["name"]).upper(),
            description="Satatlite ID: {0}".format(obj["id"]),
            color=0x00FF00,
        )
        embedVar.add_field(
            name="General Info", value=HatFunctions.splitlist(text1), inline=False
        )
        await ctx.send(embed=embedVar)


def setup(bot):
    bot.add_cog(Tools(bot))
