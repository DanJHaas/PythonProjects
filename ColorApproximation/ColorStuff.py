import json, requests
import sys
import os
from PIL import Image

def resource_path(relative_path):
    try: 
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

username = input("Username: ")
scale = input("Scale (1, 2 | default: 1): ")

try:
    scale = int(scale)
except Exception:
    print("No Letters Allowed")

if isinstance(scale, int):
    if scale < 2:
        scale = 1
        print("Default Scale has been selected")
    elif scale >= 2:
        print("Scale 2 was selected")
else:
    scale = 1
    print("Default Scale has been selected")

if os.path.exists(resource_path(os.path.dirname(os.path.abspath(__file__)))+"\\command.txt"):
        os.remove(resource_path(os.path.dirname(os.path.abspath(__file__)))+"\\command.txt")

def convImg():
    ply = Image.open(resource_path(os.path.dirname(os.path.abspath(__file__)))+'\\{0}.png'.format(username))
    colors={}
    colorvaluesnames = ["red","orange","yellow","lime","green","brown","blue","light_blue","cyan","purple","magenta","pink","black","gray","light_gray","white"]
    colorvaluesnumber = [(153, 51, 51), (216, 127, 51), (229, 229, 51), (127, 204, 25), (102, 127, 51), (102, 76, 51), (51, 76, 178), (102, 153, 216), (76, 127, 153), (127, 63, 178), (178, 76, 216), (242, 127, 165), (25, 25, 25), (76, 76, 76), (153, 153, 153), (255, 255, 255)]
    i=0
    for pixel in colorvaluesnames:
        colors["minecraft:"+colorvaluesnames[i]+"_stained_glass_pane"] = colorvaluesnumber[i]
        i=i+1

    with open(resource_path(os.path.dirname(os.path.abspath(__file__)))+"\\command.txt","w") as file1:
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
    os.remove(resource_path(os.path.dirname(os.path.abspath(__file__)))+'\\{0}.png'.format(username))   

if username != "":
    playerurl = "https://api.mojang.com/users/profiles/minecraft/{0}".format(username)  
    r = requests.get(url= playerurl)
    r2 = r.text
    if r2 != "":
        print("Found User {0}".format(username))
        jsondata = json.loads(str(r2))
        uuid = str(jsondata["id"])
        imageurl = "https://crafatar.com/avatars/{0}?size={1}".format(uuid,scale*8)
        img_data = requests.get(imageurl).content
        with open(resource_path(os.path.dirname(os.path.abspath(__file__)))+'\\{0}.png'.format(username), 'wb') as handler:
            handler.write(img_data)

        convImg()
else:
    print("No Username Was Entered")

