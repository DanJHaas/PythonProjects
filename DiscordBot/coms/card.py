import discord
from discord.ext import commands

# after imports \/
import io
import HatFunctions

# command types [Funny, Tools]
class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def card(self, ctx, *users: discord.User):
        images = []
        for i in users:
            u = await self.bot.fetch_user(i.id)
            images.append(HatFunctions.make_image(u))

        for i in images:
            with io.BytesIO() as image_binary:
                i.save(image_binary, "PNG")
                image_binary.seek(0)
                await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))

    @card.error
    async def clear_error(ctx, error):
        await ctx.send("no")


def setup(bot):
    bot.add_cog(Funny(bot))
