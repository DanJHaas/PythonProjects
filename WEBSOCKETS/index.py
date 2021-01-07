import asyncio
import websockets
import json
import math
from PIL import Image
import random
#ws://72.68.183.77:5000

x,y=0,-1

async def main(websocket, path):
    global x,y
    img = Image.new('RGB', (1000, 1000))
    while(True):
        try:
            
            await websocket.send(">>> CONNECTED TO HAT ONLINE")
            msg = await websocket.recv()
            print("msg")

            # if msg == "break":
            #     y+=1
            #     x=-1

            # if msg == "end":
            #     img.save(f'{random.randint(1,x)}.png')
            #     img.show()

            # if float(msg) > 0:
            #     msg = float(msg)
            #     c = math.floor((int(msg*1000) << 3)/1000)
            #     c=200-c
            #     x+=1
            #     img.putpixel((x,y), (c,c,c))
            #     print(x,y,f"Pixel Value : {c}")
            # else:
            #     x+=1
            #     img.putpixel((x,y), (0,0,0))
            #     #print(x,y)

        except Exception as e: pass#print(e)
    



start_server = websockets.serve(main, "192.168.1.50", 5000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

