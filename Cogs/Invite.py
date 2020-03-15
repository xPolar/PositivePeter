# Imports
import asyncio

import discord
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Invite",
            url = "https://discordapp.com/oauth2/authorize?client_id=649535694145847301&permissions=26688&scope=bot",
            color = Config.MAINCOLOR
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))