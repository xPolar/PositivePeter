"""
MIT License

Copyright (c) 2020 xPolar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Packages.
## Packages default to Python.
from typing import Union
## Packages that have to be installed through the package manager.
import discord
from discord.ext import commands
## Packages on this machine.
import Config
from Utilities import embed_color, get_prefix

class Configuration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(aliases = ["config"])
    @commands.has_permissions(manage_guild = True)
    async def configuration(self, ctx):
        """Configure the bot in your server to allow for custom hotlines and disable compliments as well as set a custom number of times for the bot to be triggered before sending a DM to the user."""
        if ctx.invoked_subcommand == None:
            prefix = get_prefix(ctx.message)
            embed = discord.Embed(
                title = "Guild Configuration",
                description = f"**`{prefix}hotline` - Set the custom server hotline.\n`{prefix}compliments` - Whether compliments should be sent in {ctx.guild} or not.\n`{prefix}count` - The amount of times the bot has to be triggered to send a DM to a user.**",
                color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
            )
            await ctx.send(embed = embed)
    
    @configuration.error
    async def configuration_error(self, ctx, error):
        """Configuration command error handler.

        Args:
            ctx (discord.Context): discord.py's context object.
            error (Exception): The exception that was raised.
        """
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title = "Missing Permissions",
                description = "You're missing the **Manage Server** permission which is required to use this command!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
    
    @configuration.command()
    async def hotline(self, ctx, *, hotline = None):
        """Set or remove the custom hotline for the server."""
        if hotline == None:
            embed = discord.Embed(
                title = "Empty Argument",
                description = "Please provide a custom server hotline or say `remove` to remove the current hotline!",
                color = Config.ERRORCOLOR
            )
        else:
            if hotline.lower() == "remove":
                embed = discord.Embed(
                    title = "Hotline Removed",
                    description = "I have removed the custom hotline for this server!",
                    color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
                )
                Config.CLUSTER["servers"]["hotlines"].delete_one({"_id": ctx.guild.id})
            else:
                embed = discord.Embed(
                    title = "Hotline Set",
                    description = f"I have set the custom hotline for this server as `{hotline}`!",
                    color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
                )
                Config.CLUSTER["servers"]["hotlines"].update_one({"_id": ctx.guild.id}, {"$set": {"hotline": hotline}}, upsert = True)
        await ctx.send(embed = embed)
    
    @configuration.command()
    async def compliments(self, ctx):
        """Disable or enable compliments from being sent in the server."""
        document = Config.CLUSTER["servers"]["compliments"].find_one({"_id": ctx.guild.id})
        embed = discord.Embed(
            title = f"Compliments { 'Enabled' if document != None else 'Disabled'}",
            description = f"I will { 'now' if document != None else 'no longer' } send compliments in this server!",
            color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
        )
        Config.CLUSTER["servers"]["compliments"].insert_one({"_id": ctx.guild.id}) if document == None else Config.CLUSTER["servers"]["compliments"].delete_one({"_id": ctx.guild.id})
        await ctx.send(embed = embed)
    
    @configuration.command()
    async def count(self, ctx, count : Union[int, str] = None):
        """Set the amount of times the bot has to be triggered to DM a user."""
        if count == None:
            embed = discord.Embed(
                title = "Empty Argument",
                description = "Please provide a number or say `remove` to remove the current count!",
                color = Config.ERRORCOLOR
            )
        else:
            if isinstance(count, int):
                embed = discord.Embed(
                    title = "Count Set",
                    description = f"I have set the count for this server to `{count}`!",
                    color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
                )
                Config.CLUSTER["servers"]["count"].update_one({"_id": ctx.guild.id}, {"$set": {"count": count}}, upsert = True)
            else:
                if count.lower() == "remove":
                    embed = discord.Embed(
                        title = "Count Removed",
                        description = "I have removed the count for this server!",
                        color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
                    )
                    Config.CLUSTER["servers"]["count"].delete_one({"_id": ctx.guild.id})
                else:
                    embed = discord.Embed(
                        title = "Invalid Argument",
                        description = "Please provide a valid number or say `remove` to remove the current count!",
                        color = Config.ERRORCOLOR
                    )
        await ctx.send(embed = embed)

    @count.error
    async def count_error(self, ctx, error):
        """Configuration Count command error handler.

        Args:
            ctx (discord.Context): discord.py's context object.
            error (Exception): The exception that was raised.
        """
        if isinstance(error, commands.BadUnionArgument):
            embed = discord.Embed(
                title = "Invalid Argument",
                description = "Please provide a valid number or say `remove` to remove the current count!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Configuration(bot))