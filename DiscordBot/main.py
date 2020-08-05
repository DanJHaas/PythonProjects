from math import nan
import discord
from discord.ext import commands
from terminaltables import AsciiTable, DoubleTable, SingleTable
from datetime import datetime
import requests
import urllib
import json
import PIL
from geopy.geocoders import Nominatim

bot = commands.Bot(command_prefix="~")
geolocator = Nominatim(user_agent="ungaDiscordBot")
@bot.event
async def on_ready():
    print("Were good to go")

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

def ElectricBoogaloo(lat, lon):
    URL = "https://api.weatherbit.io/v2.0/current"
    apikey = "5da0faaee117402bb3fbcfeab8115847"
    PARAMS = {'lat':lat,'lon':lon,'key':apikey}
    r = requests.get(url = URL, params = PARAMS)
    data = r.text
    obj = json.loads(str(data))
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

#rand facts about space TODO #1
@bot.command()
async def spacefacts(ctx):
    await ctx.send(datetime.utcfromtimestamp(int("1595130776")).strftime('%Y-%m-%d %H:%M:%S'))


#stupid fucking apostrophies holy fuck
#give advice
@bot.command()
async def advice(ctx):
    URL = "https://api.adviceslip.com/advice"
    r = requests.get(url= URL)
    unga = r.text
    obj = json.loads(str(unga))
    await ctx.send(str(obj["slip"]["advice"]).upper())

@bot.command()
async def geocode(ctx, *args):
    if args != "":
        if geolocator.geocode(args) != None:
            location = geolocator.geocode(args)
            await ctx.send((location.latitude, location.longitude))
            await ctx.send(ElectricBoogaloo(location.latitude, location.longitude))
            await ctx.send(location.address)
        else:
            await ctx.send("City does not exsist")
    else:
        await ctx.send("No Arguments found")
    #API: 5da0faaee117402bb3fbcfeab8115847


#e621, lots of string and url formatting, Uri is annoying and should be tossed into hell
#https://e621.net/posts.json?limit=1&tags=transformation+order:random
@bot.command()
async def e621(ctx, *args):
    if ctx.channel.is_nsfw():
        URL = "https://e621.net/posts.json?"
        limit = "1"
        if args != ():
            await ctx.send("```"+"Tags: "+str(args).replace("(","").replace(")","").replace("'","")+"```")
            tags = str(args).replace(",","+").replace("(","").replace(")","").replace("'","")[:-1]+"+order:random"
        else:
            tags = "order:random"

        PARAMS = {'limit':limit,'tags':tags}
        qry = urllib.parse.urlencode(PARAMS).replace("%3A",":").replace("%2B","+")
        HEADERS = {'User-Agent':'HH124','From':'hasshaas1@gmail.com'}
        s = requests.Session()
        req = requests.Request(method='GET', url=URL,params = PARAMS,headers=HEADERS)
        prep = req.prepare()
        prep.url = URL + qry
        link = s.send(prep)
        r = link.json()
        if r["posts"] != []:
            for i in range(int(limit)):
                await ctx.send("```"+"Artist: "+r["posts"][i]["tags"]["artist"][0]+"```")
                await ctx.send(r["posts"][i]["file"]["url"])
        else:
            await ctx.send("invalid tags please try again")
    else:
        await ctx.send("This is a Non-Nsfw chat")

        
myfile = open("key1.txt")
txt = myfile.read()
bot.run(txt)
myfile.close()