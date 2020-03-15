import asyncio

import discord
import motor.motor_asyncio
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    @commands.guild_only()
    async def prefix(self, ctx):
        """
        View or edit your server's prefix.
        """
        if ctx.invoked_subcommand == None:
            prefix = await Config.CLUSTER["servers"]["prefixes"].find_one({"_id": ctx.guild.id})
            if prefix == None:
                prefix = Config.PREFIX
            else:
                prefix = prefix["prefix"]
            embed = discord.Embed(
                title = "Prefix",
                description = f"My prefix for this server is `{prefix}`.",
                color = Config.MAINCOLOR 
            )
            await ctx.send(embed = embed)
    
    @prefix.command()
    @commands.has_permissions(manage_guild = True)
    async def set(self, ctx, new_prefix = None):
        if new_prefix == None:
            embed = discord.Embed(
                title = "Error",
                description = "Please provide a new prefix!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = "Prefix Set",
                description = f"You have set this server's prefix to `{new_prefix}`.",
                color = Config.MAINCOLOR
            )
            prefix = await Config.CLUSTER["servers"]["prefixes"].update_one({"_id": ctx.guild.id}, {"$set": {"prefix": new_prefix}}, upsert = True)
            await ctx.send(embed = embed)

    @prefix.command()
    @commands.has_permissions(manage_guild = True)
    async def reset(self, ctx):
        embed = discord.Embed(
            title = "Prefix Reset",
            description = f"You have reset this server's prefix.",
            color = Config.MAINCOLOR
        )
        await Config.CLUSTER["servers"]["prefixes"].delete_one({"_id": ctx.guild.id})
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))