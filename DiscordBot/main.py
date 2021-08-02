import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    intents=intents,
    command_prefix="~",
    activity=discord.Game("~help | fixing up some things..."),
)


@bot.event
async def on_command_error(ctx, error):
    pass


@bot.event
async def on_ready():
    print("Were good to go!")


commands = ["test", "sus", "card", "chad", "weather", "space", "advice", "git"]
for i in commands:
    bot.load_extension(f"coms.{i}")
    print(f"Successfully added command: {i}!")


"""
time for counting later
will implement card timings eventualy
"""
# @tasks.loop(seconds=1.0)
# async def hello():
#     epoch_time = int(time.time())
#     print(epoch_time)
# hello.start()


# # e621, lots of string and url formatting, Uri is annoying and should be tossed into hell
# @bot.command()
# async def e621(ctx, *args):
#     if ctx.channel.is_nsfw():
#         URL = "https://e621.net/posts.json?"
#         limit = "1"
#         if args != None:
#             await ctx.send(
#                 "```"
#                 + "Tags: "
#                 + str(args).replace("(", "").replace(")", "").replace("'", "")
#                 + "```"
#             )
#             tags = (
#                 str(args)
#                 .replace(",", "+")
#                 .replace("(", "")
#                 .replace(")", "")
#                 .replace("'", "")[:-1]
#                 + "+order:random"
#             )
#         else:
#             tags = "order:random"

#         PARAMS = {"limit": limit, "tags": tags}
#         qry = urllib.parse.urlencode(PARAMS).replace("%3A", ":").replace("%2B", "+")
#         HEADERS = {"User-Agent": "cum", "From": "googaa@fuckyou.com"}
#         s = requests.Session()
#         req = requests.Request(method="GET", url=URL, params=PARAMS, headers=HEADERS)
#         prep = req.prepare()
#         prep.url = URL + qry
#         link = s.send(prep)
#         r = link.json()
#         if r["posts"] != []:
#             for i in range(int(limit)):
#                 await ctx.send(
#                     "```" + "Artist: " + r["posts"][i]["tags"]["artist"][0] + "```"
#                 )
#                 await ctx.send(r["posts"][i]["file"]["url"])
#                 time.sleep(1)
#         else:
#             await ctx.send("invalid tags please try again")
#     else:
#         await ctx.send("This is a Non-Nsfw chat")


if __name__ == "__main__":
    myfile = open("key1.txt")
    txt = myfile.read()
    bot.run(txt)
    myfile.close()
