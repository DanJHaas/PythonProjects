import discord
from discord.ext import commands

# after imports \/
import io
import random
import HatFunctions
from PIL import Image, ImageFont, ImageDraw

# command types [Funny, Tools]
class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # sussy imposter is at it again
    # @ the sussy imposter to throw them out of the ship
    @commands.command()
    async def sus(self, ctx, user: discord.User):
        mentioned_users = [user, ctx.author]
        stored_users = []
        all_users = []
        user_info = []
        # get all users in a list
        for i in ctx.message.guild.members:
            if i not in (user, ctx.author):
                all_users.append(i)
        random.shuffle(all_users)

        # properly sort list to be used later
        for test in range(10):
            if test not in (1, 7):
                try:
                    stored_users.append(all_users[0])
                    all_users.remove(all_users[0])
                except:
                    stored_users.append("blank")
            else:
                stored_users.append(mentioned_users[0])
                mentioned_users.remove(mentioned_users[0])

        # sort list of users into proper formatting
        for i in stored_users:
            if i != "blank":
                u = await self.bot.fetch_user(i.id)
                user_info.append(HatFunctions.usertoavatar(u, 38, 38))
                user_info.append(i.name)
            else:
                blank = Image.new("RGBA", (38, 38), (238, 245, 253))
                user_info.append(blank)
                user_info.append("")

        # duct tape code theres definatly nothing here
        if user_info[19] == "":
            user_info[18] = Image.new("RGBA", (45, 38), (149, 156, 164))

        # 115, 64 starting pos

        # 50 pixels offset down
        # 241 left offset
        # loop for setting proper picture offsets

        # text offsets start(160,69)
        textx = 160
        texty = 64
        offx = 115
        offy = 64
        backimage = Image.open("amogus.png", "r")
        font = ImageFont.truetype("amogus.ttf", 20)
        draw = ImageDraw.Draw(backimage)
        for i in range(20):
            if i % 2 == 0:
                draw.text(
                    (textx, texty),
                    user_info[i + 1],
                    font=font,
                    align="left",
                    fill="black",
                )

                x1, y1 = user_info[i].size
                backimage.paste(
                    user_info[i], box=(0 + offx, 0 + offy, x1 + offx, y1 + offy)
                )
                texty += 50
                offy += 50
                if i == 8:
                    texty = 64
                    offy = 64
                    textx += 241
                    offx += 241

        with io.BytesIO() as image_binary:
            backimage.save(image_binary, "PNG")
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))
        pass

    @sus.error
    async def clear_error(self, ctx, error):
        await ctx.send("no")


def setup(bot):
    bot.add_cog(Funny(bot))
