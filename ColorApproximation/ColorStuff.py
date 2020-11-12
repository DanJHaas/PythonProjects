import urllib, json, requests
import PIL
import os
from PIL import Image


username = input("Username: ")
playerurl = "https://api.mojang.com/users/profiles/minecraft/{0}".format(username)
palellet = Image.open("ColorApproximation//Palette.png")

if os.path.exists("ColorApproximation//command.txt"):
        os.remove("ColorApproximation//command.txt")

def convImg():
    pal = Image.open('ColorApproximation//{0}.png'.format("Palette"))
    ply = Image.open('ColorApproximation//{0}.png'.format(username))
    colors={}
    colorvalues = ["red","orange","yellow","lime","green","brown","blue","light_blue","cyan","purple","magenta","pink","black","gray","light_gray","white"]
    i=0
    for pixel in pal.getdata():
        colors["minecraft:"+colorvalues[i]+"_stained_glass_pane"] = pixel
        i=i+1

    with open("ColorApproximation//command.txt","w") as file1:
        file1.write("/give @p minecraft:bundle{Items:[")
        for head in ply.getdata():
            tempdev = 1000
            winner =""
            value = False
            r1,g1,b1=head
            for name,color in colors.items():
                r2,g2,b2=color
                dev = abs(r1-r2) + abs(g1-g2) + abs(b1-b2)
                if (value !=False) or (dev < tempdev):
                    winner = name
                    tempdev = dev
            file1.write('{id:"'+winner+'",Count:1b},')
        file1.write("]}")  
    os.remove('ColorApproximation//{0}.png'.format(username))   
                
                
r = requests.get(url= playerurl)
r2 = r.text
if r2 != "":
    print("Found User {0}".format(username))
    jsondata = json.loads(str(r2))
    uuid = str(jsondata["id"])
    imageurl = "https://crafatar.com/avatars/{0}?size=8".format(uuid)
    img_data = requests.get(imageurl).content
    with open('ColorApproximation//{0}.png'.format(username), 'wb') as handler:
        handler.write(img_data)

    convImg()
