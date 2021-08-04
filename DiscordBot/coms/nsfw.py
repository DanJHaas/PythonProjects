import discord
from discord.ext import commands

# after imports \/
import urllib
import requests
import time

# command types [Funny, Tools]
class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # e621, lots of string and url formatting, Uri is annoying and should be tossed into hell
    @commands.command()
    async def e621(ctx, *args):
        if ctx.channel.is_nsfw():
            URL = "https://e621.net/posts.json?"
            limit = "1"
            if args != None:
                await ctx.send(
                    "```"
                    + "Tags: "
                    + str(args).replace("(", "").replace(")", "").replace("'", "")
                    + "```"
                )
                tags = (
                    str(args)
                    .replace(",", "+")
                    .replace("(", "")
                    .replace(")", "")
                    .replace("'", "")[:-1]
                    + "+order:random"
                )
            else:
                tags = "order:random"

            PARAMS = {"limit": limit, "tags": tags}
            qry = urllib.parse.urlencode(PARAMS).replace("%3A", ":").replace("%2B", "+")
            HEADERS = {"User-Agent": "cum", "From": "googaa@fuckyou.com"}
            s = requests.Session()
            req = requests.Request(
                method="GET", url=URL, params=PARAMS, headers=HEADERS
            )
            prep = req.prepare()
            prep.url = URL + qry
            link = s.send(prep)
            r = link.json()
            if r["posts"] != []:
                for i in range(int(limit)):
                    await ctx.send(
                        "```" + "Artist: " + r["posts"][i]["tags"]["artist"][0] + "```"
                    )
                    await ctx.send(r["posts"][i]["file"]["url"])
                    time.sleep(1)
            else:
                await ctx.send("invalid tags please try again")
        else:
            await ctx.send("This is a Non-Nsfw chat")


def setup(bot):
    bot.add_cog(Funny(bot))
