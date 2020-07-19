import discord
from discord.ext import commands
from terminaltables import AsciiTable, DoubleTable, SingleTable
from datetime import datetime
import requests
import json
import PIL

bot = commands.Bot(command_prefix="~")

@bot.event
async def on_ready():
    print("Were good to go")

@bot.command()
async def unga(ctx):
    await ctx.send(file=discord.File(r"C:\Users\bluee\Desktop\DeepFake\DeepFaceLab_CUDA\workspace\result.mp4"))

table_data = [
    ['Heading1', 'Heading2'],
    ['row1', 'row1'],
    ['row2', 'row2'],
    ['row3', 'row3']
]
table = DoubleTable(table_data)
@bot.command()
async def test(ctx, *args):
    await ctx.send("```"+table.table+"```")



def GetWeather(city):
    URL = "http://api.openweathermap.org/data/2.5/weather"
    location = city
    apikey = "5302a0e28047fdba190337922230a083"
    untits = "metric"
    PARAMS = {'q':location,'appid':apikey,'units':untits}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    obj = json.loads(str(data).replace("\'","\""))
    return obj


@bot.command()
async def weather(ctx, *args):
    location = str(args).replace("(", "").replace(")","").replace("'","")
    location = str(location[:-1])
    obj = json.loads(str(GetWeather(location)).replace("\'","\""))
    if str(obj["cod"]) == "200":
        #await ctx.send(obj)
        Weather_data = [
        ['Location', 'Wind info', "Sky Conditions", "Temperature (Celcius)","Barometer"],
        ["Latitude: "+str(obj["coord"]["lat"])+"°", 'Wind Speed: '+str(obj["wind"]["speed"])+" km/h", "Sky condition: "+str(obj["weather"][0]["main"]),"Current Temp: "+str(obj["main"]["temp"])+"°","Pressure: "+str(obj["main"]["pressure"])+" mbar"],
        ["Longitude: "+str(obj["coord"]["lon"])+"°", 'Wind angle: '+str(obj["wind"]["deg"])+"°", "Cloud type: "+str(obj["weather"][0]["description"]), "Feels like: "+str(obj["main"]["feels_like"])+"°","Humidity: "+str(obj["main"]["humidity"])+"%"],
        ["City: "+obj["name"], "","","Min Temp: "+str(obj["main"]["temp_min"])+"°","Visibility: "+str(obj["visibility"]/100)+"%"],
        ["Country: "+obj["sys"]["country"],"","","","Max Temp: "+str(obj["main"]["temp_max"])+"°"]]
        tableWeather = SingleTable(Weather_data)
        await ctx.send("```"+tableWeather.table+"```")
    else:
        await ctx.send("could not process location please try again")

#rand facts about space
@bot.command()
async def spacefacts(ctx):
    await ctx.send(datetime.utcfromtimestamp(int("1595130776")).strftime('%Y-%m-%d %H:%M:%S'))


#stupid fucking apostrophies holy fuck
def adviceLink():
    URL = "https://api.adviceslip.com/advice"
    r = requests.get(url= URL)
    return r.text

#give advice
@bot.command()
async def advice(ctx):
    obj = json.loads(str(adviceLink()))
    await ctx.send(str(obj["slip"]["advice"]).upper())



myfile = open(r"C:\Users\bluee\Desktop\DeepFake\key.txt")
txt = myfile.read()
bot.run(txt)
myfile.close()