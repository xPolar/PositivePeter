# Imports
import asyncio
import time

import discord
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ["latency"])
    async def ping(self, ctx):
        """
        Show the bot's current latency.
        """
        embed = discord.Embed(
            title = "Ping",
            description = "Pinging...",
            color = Config.MAINCOLOR
        )
        t1 = time.perf_counter()
        msg = await ctx.send(embed = embed)
        t2 = time.perf_counter()
        embed = discord.Embed(
            title = "🏓 Pong!",
            description = f"API latency is {round((t2 - t1) * 1000)}ms\nHost latency is {round(self.bot.latency * 1000, 2)}ms",
            color = Config.MAINCOLOR
        )
        await msg.edit(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))
