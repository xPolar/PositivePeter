# Imports
import asyncio

import discord
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    async def get_prefix(self, ctx):
        if ctx.message.guild == None:
            return Config.PREFIX
        else:
            prefixes = await Config.CLUSTER["servers"]["prefixes"].find_one({"_id": ctx.message.guild.id})
            if prefixes == None:
                return Config.PREFIX
            else:
                return prefixes["prefix"]

    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand == None:
            embed = discord.Embed(
                title = "Help",
                color = Config.MAINCOLOR
            )
            prefix = await self.get_prefix(ctx)
            embed.add_field(name = f"**{prefix}help [Command]**", value = "View this menu or information about a command.", inline = False)
            embed.add_field(name = f"**{prefix}invite**", value = "Get a link to invite me.", inline = False)
            embed.add_field(name = f"**{prefix}support**", value = "Get a link to the support server.", inline = False)
            embed.add_field(name = f"**{prefix}vote**", value = "Get a link to vote for the bot.", inline = False)
            embed.add_field(name = f"**{prefix}ping**", value = "View the bot's latency.", inline = False)
            embed.add_field(name = f"**{prefix}stop**", value = "Have the bot stop responding to you.", inline = False)
            embed.add_field(name = f"**{prefix}suggest <Suggestion>**", value = "Suggest a trigger for the Positive Peter community to review.", inline = False)
            if ctx.guild != None:
                if ctx.author.guild_permissions.manage_guild == True:
                    embed.add_field(name = f"**{prefix}config <Configuration> <Value>**", value = "Edit a server side configuration value.", inline = False)
                    embed.add_field(name = f"**{prefix}prefix <New Prefix>**", value = "Edit the server side prefix.", inline = False)
            if ctx.author.id in Config.OWNERIDS:
                embed.add_field(name = f"**{prefix}restart [Cog]**", value = "Restart the entire bot or a singular cog.", inline = False)
                embed.add_field(name = f"**{prefix}block**", value = "Block a user from sending suggestions.", inline = False)
                embed.add_field(name = f"**{prefix}unblock**", value = "Unblock a user from sending suggestions.", inline = False)
            embed.add_field(name = "\u200b", value = "**[Invite](https://discordapp.com/oauth2/authorize?client_id=649535694145847301&permissions=26688&scope=bot)\n[Vote](https://top.gg/bot/649535694145847301/vote)\n[Support](https://discord.gg/VwMWj2B)**", inline = False)
            await ctx.send(embed = embed)
    
    @help.command(aliases = ["help"])
    async def _help(self, ctx):
        prefix = await self.get_prefix(ctx)
        embed = discord.Embed(
            title = f"Help [Command]",
            description = "View this menu or information about a command.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        embed.add_field(name = "**Example Usage**", value = f"`{prefix}help suggest`")
        await ctx.send(embed = embed)
    
    @help.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "Invite",
            description = "Get a link to invite me.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        await ctx.send(embed = embed)
    
    @help.command()
    async def support(self, ctx):
        embed = discord.Embed(
            title = "Support",
            description = "Get a link to the support server.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        await ctx.send(embed = embed)
    
    @help.command()
    async def vote(self, ctx):
        embed = discord.Embed(
            title = "Vote",
            description = "Get a link to vote for the bot.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        await ctx.send(embed = embed)
    
    @help.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title = "Ping",
            description = "View the bot's latency.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        await ctx.send(embed = embed)

    @help.command()
    async def stop(self, ctx):
        embed = discord.Embed(
            title = "Stop",
            description = "Have the bot stop responding to you.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        await ctx.send(embed = embed)

    @help.command()
    async def suggest(self, ctx):
        embed = discord.Embed(
            title = "Suggest <Suggestion>",
            description = "Suggest a trigger for the Positive Peter community to review.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        prefix = await self.get_prefix(ctx)
        embed.add_field(name = "**Example Usage**", value = f"`{prefix}suggest I want to die`")
        await ctx.send(embed = embed)

    @help.command()
    @commands.has_permissions(manage_guild = True)
    async def config(self, ctx):
        embed = discord.Embed(
            title = "Config <Configuration> <Value / Reset>",
            description = "Edit a server side configuration value.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        prefix = await self.get_prefix(ctx)
        embed.add_field(name = "**Example Usage**", value = f"`{prefix}config hotline 123-456-7890`")
        await ctx.send(embed = embed)
    
    @help.command()
    @commands.has_permissions(manage_guild = True)
    async def prefix(self, ctx):
        embed = discord.Embed(
            title = "Prefix <New Prefix / Reset>",
            description = "Edit a server side configuration value.",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Help")
        prefix = await self.get_prefix(ctx)
        embed.add_field(name = "**Example Usage**", value = f"`{prefix}prefix !`")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))