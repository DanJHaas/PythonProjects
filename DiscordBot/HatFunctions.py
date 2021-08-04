from dataclasses import dataclass
import io
import PIL
import requests
from PIL import Image
import json


# convert user id into image for use
def usertoavatar(user, imgx=1024, imgy=1024) -> Image:
    im = Image.open(
        io.BytesIO(
            requests.get(
                url=user.avatar_url_as(format="png", static_format="png"),
                params={"user": "cum"},
            ).content
        )
    )
    resize = im.resize((imgx, imgy))
    return resize


# i dont know if this works or not
def coordtolocation(lat, lon):
    # https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>$format=json
    URL = "https://nominatim.openstreetmap.org/reverse?"
    PARA = {"lat": lat, "lon": lon, "format": "json"}
    r = requests.get(url=URL, params=PARA)
    unga = r.text
    obj = json.loads(str(unga))
    return r.url


# varied use cases but splits list into nice discord format
def splitlist(input) -> str:
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


# returns weather data information about that location
# not very acurate but i cant do much about that
def GetWeather(city) -> json:
    URL = "http://api.openweathermap.org/data/2.5/weather"
    location = city
    apikey = "5302a0e28047fdba190337922230a083"
    untits = "metric"
    PARAMS = {"q": location, "appid": apikey, "units": untits}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    obj = json.loads(str(data).replace("'", '"'))
    return obj


def make_image(user) -> Image:
    im = Image.new("RGBA", (1224, 1224), (0, 0, 0, 0))
    background = Image.open("border.png")
    profileoff = (100, 100)
    masking = Image.open("mask.png")
    profile = usertoavatar(user)
    im.paste(profile, box=profileoff, mask=masking)
    im.paste(background, mask=background)
    return im
