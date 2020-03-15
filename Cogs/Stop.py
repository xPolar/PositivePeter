# Imports
import asyncio

import discord
import motor.motor_asyncio
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def stop(self, ctx):
        enabled = await Config.CLUSTER["users"]["stopped"].find_one({"_id": ctx.author.id})
        if enabled == None:
            embed = discord.Embed(
                title = "Stopping Messages",
                description = "From now on I will stop messaging you.",
                color = Config.MAINCOLOR
            )
            value = False
        else:
            if enabled["value"] == True:
                embed = discord.Embed(
                    title = "Stopping Messages",
                    description = "From now on I will stop messaging you.",
                    color = Config.MAINCOLOR
                )
                value = False
            else:
                embed = discord.Embed(
                    title = "Continuing Messages",
                    description = "From now on I will message you.",
                    color = Config.MAINCOLOR
                )
                value = True
        await Config.CLUSTER["users"]["stopped"].update_one({"_id": ctx.author.id}, {"$set": {"value": value}}, upsert = True)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))