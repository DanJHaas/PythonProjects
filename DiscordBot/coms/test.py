import discord
from discord import user
from discord.ext import commands


class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # testing command for ref for future
    @commands.command()
    async def picture(self, ctx, *user: discord.User):
        for i in user:
            u = await self.bot.fetch_user(i.id)
            await ctx.send(u.avatar_url)

    @picture.error
    async def clear_error(self, ctx, error):
        await ctx.send("no")

    @commands.command()
    async def players(self, ctx):
        all_users = []
        for i in ctx.message.guild.members:
            all_users.append(i)
            await ctx.send(f"{i.name=}")


def setup(bot):
    bot.add_cog(Tools(bot))
