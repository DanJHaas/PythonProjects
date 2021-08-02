import discord
from discord.ext import commands


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def picture(self, ctx, *user: discord.User):
        for i in user:
            u = await self.bot.fetch_user(i.id)
            await ctx.send(u.avatar_url)

    @picture.error
    async def clear_error(self, ctx, error):
        await ctx.send("no")


def setup(bot):
    bot.add_cog(Tools(bot))
