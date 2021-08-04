import glob
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


commands = [i[5:-3] for i in glob.glob("coms/*.py", recursive=True)]
for i in commands:
    try:
        bot.load_extension(f"coms.{i}")
        print(f"Successfully added command: {i}!")
    except Exception:
        print(f"Could not add command: {i}")


"""
time for counting later
will implement card timings eventualy
"""
# @tasks.loop(seconds=1.0)
# async def hello():
#     epoch_time = int(time.time())
#     print(epoch_time)
# hello.start()


if __name__ == "__main__":
    myfile = open("key1.txt")
    txt = myfile.read()
    bot.run(txt)
    myfile.close()
