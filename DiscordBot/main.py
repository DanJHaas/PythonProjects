from math import nan
import discord
from discord.ext import commands
from requests.api import request
from terminaltables import AsciiTable, DoubleTable, SingleTable
from datetime import datetime
import requests
import urllib.request
import json
from PIL import Image
import time
import random
import io
from geopy.geocoders import Nominatim

bot = commands.Bot(
    command_prefix="~",
    activity=discord.Game("~help | fixing up some things..."),
)
geolocator = Nominatim(user_agent="ungaDiscordBot")


@bot.event
async def on_ready():
    print("Were good to go")


def coordtolocation(lat, lon):
    # https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>$format=json
    URL = "https://nominatim.openstreetmap.org/reverse?"
    PARA = {"lat": lat, "lon": lon, "format": "json"}
    r = requests.get(url=URL, params=PARA)
    unga = r.text
    obj = json.loads(str(unga))
    return r.url


def splitlist(input):
    value = ""
    try:
        if type(input) == dict:
            for i in input:
                value += """```ini\n[{0}]: {1}\n```""".format(i, input[i])
        elif type(input) == list:
            for i in input:
                value += "{0}\n".format(i)
    except Exception as error:
        value = error
    return value


def GetWeather(city):
    URL = "http://api.openweathermap.org/data/2.5/weather"
    location = city
    apikey = "5302a0e28047fdba190337922230a083"
    untits = "metric"
    PARAMS = {"q": location, "appid": apikey, "units": untits}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    obj = json.loads(str(data).replace("'", '"'))
    return obj


def grepWeather(lat, lon):
    myfile1 = open("DiscordBot\key2.txt")
    txt1 = myfile1.read()
    URL = "https://api.weatherbit.io/v2.0/current"
    apikey = txt1
    PARAMS = {"lat": lat, "lon": lon, "key": apikey}
    r = requests.get(url=URL, params=PARAMS)
    data = r.text
    obj = json.loads(str(data))
    myfile1.close()
    return obj


@bot.command()
async def chad(ctx, *user: discord.User):
    # u = await bot.fetch_user(user.id)
    # await ctx.send(u.avatar_url)
    users = []
    if len(user) == 2:
        for i in user:
            u = await bot.fetch_user(i.id)
            PARAMS = {"user": "cum"}
            r = requests.get(url=u.avatar_url, params=PARAMS)
            im = Image.open(io.BytesIO(r.content)).convert("RGBA")
            reim = im.resize((128, 128))
            users.append(reim)

        backimage = Image.open("DiscordBot/cover8.png", "r").convert("RGBA")
        x1, y1 = users[0].size
        x2, y2 = users[1].size
        offx1 = 335
        offy1 = 163
        offx2 = 1022
        offy2 = 213
        backimage.paste(users[0], box=(0 + offx1, 0 + offy1, x1 + offx1, y1 + offy1))
        backimage.paste(users[1], box=(0 + offx2, 0 + offy2, x2 + offx2, y2 + offy2))
        # backimage.show()
        # await ctx.send(file=discord.File(backimage.tobytes()))
        with io.BytesIO() as image_binary:
            backimage.save(image_binary, "PNG")
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))

    else:
        await ctx.send(f"{len(user)} users were passed 2 expected")


@bot.command()
async def weather(ctx, *args):
    location = str(args).replace("(", "").replace(")", "").replace("'", "")
    location = str(location[:-1])
    obj = json.loads(str(GetWeather(location)).replace("'", '"'))
    if str(obj["cod"]) == "200":
        # await ctx.send(obj)
        Weather_data = [
            [
                "Location",
                "Wind info",
                "Sky Conditions",
                "Temperature (Celcius)",
                "Barometer",
            ],
            [
                "Latitude: " + str(obj["coord"]["lat"]) + "°",
                "Wind Speed: " + str(obj["wind"]["speed"]) + " km/h",
                "Sky condition: " + str(obj["weather"][0]["main"]),
                "Current Temp: " + str(obj["main"]["temp"]) + "°",
                "Pressure: " + str(obj["main"]["pressure"]) + " mbar",
            ],
            [
                "Longitude: " + str(obj["coord"]["lon"]) + "°",
                "Wind angle: " + str(obj["wind"]["deg"]) + "°",
                "Cloud type: " + str(obj["weather"][0]["description"]),
                "Feels like: " + str(obj["main"]["feels_like"]) + "°",
                "Humidity: " + str(obj["main"]["humidity"]) + "%",
            ],
            [
                "City: " + obj["name"],
                "",
                "",
                "Min Temp: " + str(obj["main"]["temp_min"]) + "°",
                "Visibility: " + str(obj["visibility"] / 100) + "%",
            ],
            [
                "Country: " + obj["sys"]["country"],
                "",
                "",
                "Max Temp: " + str(obj["main"]["temp_max"]) + "°",
                "",
            ],
        ]
        tableWeather = SingleTable(Weather_data)
        await ctx.send("```" + tableWeather.table + "```")
    else:
        await ctx.send("could not process location please try again")


# rand facts about space TODO #1
# https://api.wheretheiss.at/v1/satellites/25544
@bot.command()
async def spacefacts(ctx):

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
    embedVar.add_field(name="General Info", value=splitlist(text1), inline=False)
    # embedVar.add_field(name="Field2", value="https://i.nhentai.net/galleries/1914664/1.jpg", inline=False)
    # embedVar.set_image(url="image url")
    await ctx.channel.send(embed=embedVar)

    # await ctx.send(epochTime)


# @bot.command()
# async def fonts(ctx):
#     await ctx.send("cum")


# stupid fucking apostrophies holy fuck
# give advice
@bot.command()
async def advice(ctx):
    URL = "https://api.adviceslip.com/advice"
    r = requests.get(url=URL)
    unga = r.text
    obj = json.loads(str(unga))
    await ctx.send(str(obj["slip"]["advice"]).upper())


# @bot.command()
# async def cum(ctx, *args):
#     await ctx.send(args[0])

# https://github.com/HattyH124/PythonProjects
@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/HattyH124/PythonProjects")


@bot.command()
async def geocode(ctx, *args):
    if args != "":
        if geolocator.geocode(args) != None:
            location = geolocator.geocode(args)
            w = grepWeather(location.latitude, location.longitude)
            Weather_data = [
                [
                    "Location",
                    "Wind info",
                    "Sky Conditions",
                    "Temperature (Celcius)",
                    "Barometer",
                ],
                [
                    "Latitude: " + str(w["data"][0]["lat"]) + "°",
                    "Wind Speed: " + str(w["data"][0]["wind_spd"]) + " km/h",
                    "Cloud Cover: " + str(w["data"][0]["clouds"]) + "%",
                    "Temp: " + str(w["data"][0]["temp"]) + "°",
                    "Pressure: " + str(w["data"][0]["pres"]) + " mbar",
                ],
                [
                    "Longitude: " + str(w["data"][0]["lon"]) + "°",
                    "Wind angle: " + str(w["data"][0]["wind_dir"]) + "°",
                    "UV index: " + str(w["data"][0]["uv"]),
                    "Apparent Temp: " + str(w["data"][0]["app_temp"]) + "°",
                    "Humidity: " + str(w["data"][0]["rh"]) + "%",
                ],
                [
                    "City: " + str(w["data"][0]["city_name"]),
                    "",
                    "Solar Radiation: " + str(w["data"][0]["solar_rad"]) + " W/m^2",
                    "",
                    "Visibility: " + str(w["data"][0]["vis"]) + " Meters",
                ],
                [
                    "Country: " + str(w["data"][0]["country_code"]),
                    "",
                    "Time: " + str(w["data"][0]["pod"]),
                    "",
                    "Dew Point: " + str(w["data"][0]["dewpt"]) + "°",
                ],
            ]
            tableWeather = SingleTable(Weather_data)
            await ctx.send("```" + tableWeather.table + "```")
        else:
            await ctx.send("City does not exsist")
    else:
        await ctx.send("No Arguments found")


# e621, lots of string and url formatting, Uri is annoying and should be tossed into hell
# https://e621.net/posts.json?limit=1&tags=transformation+order:random
@bot.command()
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
        HEADERS = {"User-Agent": "HH124", "From": "hasshaas1@gmail.com"}
        s = requests.Session()
        req = requests.Request(method="GET", url=URL, params=PARAMS, headers=HEADERS)
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


myfile = open("DiscordBot\key1.txt")
txt = myfile.read()
bot.run(txt)
myfile.close()
