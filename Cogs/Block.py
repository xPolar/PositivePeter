# Imports
import asyncio

import discord
import motor.motor_asyncio
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    async def cog_check(self, ctx):
        return ctx.author.id in Config.OWNERIDS
    
    @commands.command(aliases = ["blacklist"])
    async def block(self, ctx, id : int = None, *, reason = None):
        if id == None:
            embed = discord.Embed(
                title = "Error",
                description = "Please provide an ID to block!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            if reason == None:
                reason = "No reason specified"
            embed = discord.Embed(
                title = "Blocked",
                description = f"You have blocked `{id}` from making suggestions for: {reason}!",
                color = Config.MAINCOLOR
            )
            await Config.CLUSTER["users"]["blocked"].update_one({"_id": id}, {"$set": {"reason": reason}}, upsert = True)
            await ctx.send(embed = embed)
            channel = self.bot.get_channel(Config.BLOCK_LOG)
            embed = discord.Embed(
                title = "User Blocked",
                description = f"The ID `{id}` was blocked by `{ctx.author}` for: {reason}",
                color = Config.MAINCOLOR
            )
            embed.set_footer(text = f"Blocker ID: {ctx.author.id}")
            await channel.send(embed = embed)
    
    @commands.command(asliases = ["whitelist"])
    async def unblock(self, ctx, id : int = None):
        if id == None:
            embed = discord.Embed(
                title = "Error",
                description = "Please provide an ID to unblock!",
                color = Config.ERRORCOLOR
            )
        else:
            embed = discord.Embed(
                title = "Unblocked",
                description = f"You habe unblocked `{id}` from making suggestions!",
                color = Config.MAINCOLOR
            )
            await Config.CLUSTER["users"]["blocked"].delete_one({"_id": id})
            await ctx.send(embed = embed)
            channel = self.bot.get_channel(Config.BLOCK_LOG)
            embed = discord.Embed(
                title = "User Unblocked",
                description = f"The ID `{id}` was unblocked by `{ctx.author}`.",
                color = Config.MAINCOLOR
            )
            embed.set_footer(text = f"Unblocker ID: {ctx.author.id}")
            await channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))
