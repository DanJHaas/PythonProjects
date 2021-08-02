import discord
from discord.ext import commands

# after imports \/
import json
import HatFunctions
from terminaltables import SingleTable

# command types [Funny, Tools]
class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, *args):
        location = str(args).replace("(", "").replace(")", "").replace("'", "")
        location = str(location[:-1])
        obj = json.loads(str(HatFunctions.GetWeather(location)).replace("'", '"'))
        if str(obj["cod"]) == "200":
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


def setup(bot):
    bot.add_cog(Tools(bot))
