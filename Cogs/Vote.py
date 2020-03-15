# Imports
import asyncio

import discord
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(
            title = "Vote",
            url = "https://top.gg/bot/649535694145847301/vote",
            color = Config.MAINCOLOR
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))