# Imports
import asyncio

import discord
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(
            title = "Support",
            url = "https://discord.gg/VwMWj2B",
            color = Config.MAINCOLOR
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))