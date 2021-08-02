import discord
from discord.ext import commands

# after imports \/
import io
import HatFunctions
from PIL import Image

# command types [Funny, Tools]
class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chad(self, ctx, *user: discord.User):

        users = []
        if len(user) == 2:
            for i in user:
                u = await self.bot.fetch_user(i.id)
                users.append(HatFunctions.usertoavatar(u, 128, 128))

            backimage = Image.open("cover8.png", "r").convert("RGBA")
            x1, y1 = users[0].size
            x2, y2 = users[1].size
            offx1 = 335
            offy1 = 163
            offx2 = 1022
            offy2 = 213
            backimage.paste(
                users[0], box=(0 + offx1, 0 + offy1, x1 + offx1, y1 + offy1)
            )
            backimage.paste(
                users[1], box=(0 + offx2, 0 + offy2, x2 + offx2, y2 + offy2)
            )
            # backimage.show()
            # await ctx.send(file=discord.File(backimage.tobytes()))
            with io.BytesIO() as image_binary:
                backimage.save(image_binary, "PNG")
                image_binary.seek(0)
                await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))

        else:
            await ctx.send(f"{len(user)} users were passed 2 expected")

    @chad.error
    async def clear_error(ctx, error):
        await ctx.send("no")


def setup(bot):
    bot.add_cog(Funny(bot))
