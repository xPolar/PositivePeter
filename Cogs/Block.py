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
from colorama import Fore, Style
from discord.ext import commands
## Packages on this machine.
import Config
from Utilities import embed_color

class Block(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    async def cog_check(self, ctx):
        return ctx.author.id in Config.OWNERIDS
    
    @commands.command(aliases = ["blacklist"])
    async def block(self, ctx, user : Union[discord.Member, discord.User, int] = None, reason = None):
        """Block a user from creating suggestions."""
        if user == None:
            embed = discord.Embed(
                title = "Empty Argument",
                description = "Please provide a user to block!",
                color = Config.ERRORCOLOR
            )
        else:
            if isinstance(user, int):
                try: # Use self.bot.fetch_user to turn an int into discord.User, if discord.NotFound is raised ask the user to provide a valid user.
                    user = await self.bot.fetch_user(user)
                except discord.NotFound:
                    embed = discord.Embed(
                        title = "Invalid Argument",
                        description = "Please provide a valid user!",
                        color = Config.ERRORCOLOR
                    )
                    return await ctx.send(embed = embed)
            embed = discord.Embed(
                title = "Blocked",
                description = f"You have blocked `{user}` from making suggestions{ f' for: {reason}' if reason != None else '!' }",
                color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
            )
            Config.CLUSTER["users"]["blocked"].update_one({"_id": user.id}, {"$set": {"reason": "No reason specified." if reason == None else reason}}, upsert = True)
            print(f"{Style.BRIGHT}{Fore.RED}[USER-BLOCKED]{Fore.WHITE} {Fore.YELLOW}{user.id}{Fore.WHITE} has been blocked by {Fore.YELLOW}{ctx.author.name}{Fore.WHITE}{ f'for: {reason}' if reason != None else '!' }{Fore.RESET}")
        await ctx.send(embed = embed)
    
    @block.error
    async def block_error(self, ctx, error):
        """Block command error handler.

        Args:
            ctx (discord.Context): discord.py's context object.
            error (Exception): The exception that was raised.
        """
        if isinstance(error, commands.BadUnionArgument):
            embed = discord.Embed(
                title = "Invalid Argument",
                description = "Please provide a valid user to block!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
    
    @commands.command(aliases = ["whitelist"])
    async def unblock(self, ctx, user : Union[discord.Member, discord.User, int] = None):
        """Unblock a user from creating suggestions."""
        if user == None:
            embed = discord.Embed(
                title = "Empty Argument",
                description = "Please provide a user to block!",
                color = Config.ERRORCOLOR
            )
        else:
            if isinstance(user, int):
                try: # Use self.bot.fetch_user to turn an int into discord.User, if discord.NotFound is raised ask the user to provide a valid user.
                    user = await self.bot.fetch_user(user)
                except discord.NotFound:
                    embed = discord.Embed(
                        title = "Invalid Argument",
                        description = "Please provide a valid user!",
                        color = Config.ERRORCOLOR
                    )
                    return await ctx.send(embed = embed)
            embed = discord.Embed(
                title = "Unblocked",
                description = f"You have unblocked `{user}` from making suggestions!",
                color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
            )
            Config.CLUSTER["users"]["blocked"].delete_one({"_id": user.id})
            print(f"{Style.BRIGHT}{Fore.CYAN}[USER-UNBLOCKED]{Fore.WHITE} {Fore.YELLOW}{user.id}{Fore.WHITE} has been unblocked by {Fore.YELLOW}{ctx.author.name}{Fore.WHITE}!{Fore.RESET}")
        await ctx.send(embed = embed)
        
    @unblock.error
    async def unblock_error(self, ctx, error):
        """Unblock command error handler.

        Args:
            ctx (discord.Context): discord.py's context object.
            error (Exception): The exception that was raised.
        """
        if isinstance(error, commands.BadUnionArgument):
            embed = discord.Embed(
                title = "Invalid Argument",
                description = "Please provide a valid user to unblock!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Block(bot))
