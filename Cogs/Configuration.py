# Imports
import asyncio
import time

import discord
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    @commands.has_permissions(manage_guild = True)
    async def config(self, ctx):
        if ctx.invoked_subcommand == None:
            embed = discord.Embed(
                title = "Configuration",
                color = Config.MAINCOLOR
            )
            embed.add_field(name = "**Guild**", value = "`hotline`, `compliments`")
            await ctx.send(embed = embed)
    
    @config.command()
    async def hotline(self, ctx, *, hotline = None):
        if hotline == None:
            embed = discord.Embed(
                title = "Error",
                description = "Please provide a hotline!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            if hotline.lower() == "reset":
                embed = discord.Embed(
                    title = "Hotline Reset",
                    description = "A server side hotline will not be displayed in suicidal messages anymore!",
                    color = Config.MAINCOLOR
                )
                await Config.CLUSTER["servers"]["hotlines"].delete_one({"_id": ctx.guild.id})
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    title = "Hotline Set",
                    description = f"I have set the hotline for {ctx.guild.name} as `{hotline}`!",
                    color = Config.MAINCOLOR
                )
                await Config.CLUSTER["servers"]["hotlines"].update_one({"_id": ctx.guild.id}, {"$set": {"hotline": hotline}}, upsert = True)
                await ctx.send(embed = embed)
    
    @config.command()
    async def compliments(self, ctx, value : bool = None):
        if value == None:
            embed = discord.Embed(
                title = "Error",
                description = "Please provide a value!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            if value == True:
                embed = discord.Embed(
                    title = "Compliments Enabled",
                    description = f"I have set compliments to `{value}` for {ctx.guild.name}!",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    title = "Compliments Disabled",
                    description = f"I have set compliments to `{value}` for {ctx.guild.name}!",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)
            await Config.CLUSTER["servers"]["compliments"].update_one({"_id": ctx.guild.id}, {"$set": {"value": value}}, upsert = True)

def setup(bot):
    bot.add_cog(Misc(bot))