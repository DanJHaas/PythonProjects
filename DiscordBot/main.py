import discord
from discord.ext import commands
import PIL

bot = commands.Bot(command_prefix="~")

@bot.event
async def on_ready():
    print("Were good to go")

@bot.command()
async def unga(ctx):
    await ctx.send(file=discord.File(r"C:\Users\bluee\Desktop\DeepFake\DeepFaceLab_CUDA\workspace\result.mp4"))

@bot.command()
async def flip(ctx):
    await 

#weather Api : 5302a0e28047fdba190337922230a083

#http://api.openweathermap.org/data/2.5/weather?q=New_York&appid=5302a0e28047fdba190337922230a083
bot.run('MjMwMDk5MzUyNTMyNjgwNzA0.XxJqLA.PSoUuLEMtUFVSXYmUEUfLN4gXSI')