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
import time, os, platform
from datetime import datetime
from typing import Union
## Packages that have to be installed through the package manager.
import aiohttp, discord, psutil
from colorama import Fore, Style
from discord.ext import commands
## Packages on this machine.
import Config
from Utilities import embed_color, get_prefix, prefixes, __version__

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["latency"])
    async def ping(self, ctx):
        """Get the latency between our bot and Discord as well as the latency of the host."""

        # Get the time at one point, trigger typing, get the time again then subtract the two values to get the host latency. To get API latency use self.bot.latency, get round trip by adding up the two latencies.
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        embed = discord.Embed(
            title = "🏓 Pong!",
            description = f"Host latency is { round((t2 - t1) * 1000) }ms.\nAPI latency is { int(round(self.bot.latency * 1000, 2)) }ms.\nRound Trip took { int(round((t2 - t1) * 1000) + round(self.bot.latency * 1000, 2)) }ms.",
            color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
        )

        # Print out into the console when the round trip takes over 500 milliseconds.
        if round((t2 - t1) * 1000) + round(self.bot.latency * 1000, 2) > 500:
            print()
            print(f"{Style.BRIGHT}{Fore.RED}[WARNING]{Fore.WHITE} API latency is { round((t2 - t1) * 1000) }ms, host latency is { int(round(self.bot.latency * 1000, 2)) }ms, and round trip took { int(round((t2 - t1) * 1000) + round(self.bot.latency * 1000, 2)) }ms.")
        await ctx.send(embed = embed)
    
    # The three following commands will be listed within the help command however allow them to be singular commands below for easier use.
    @commands.command()
    async def vote(self, ctx):
        f"""Obtain the link to vote for {self.bot.user.name}."""
        embed = discord.Embed(
            title = f"Vote for {self.bot.user.name}",
            url = f"https://top.gg/bot/{self.bot.user.id}/vote",
            color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
        )
        await ctx.send(embed = embed)
    
    @commands.command()
    async def support(self, ctx):
        """Obtain the link to join the bot's support server."""
        embed = discord.Embed(
            title = "Support Server",
            url = "https://discord.gg/VwMWj2B",
            color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
        )
        await ctx.send(embed = embed)

    @commands.command()
    async def invite(self, ctx):
        f"""Invite {self.bot.user.name}."""
        embed = discord.Embed(
            title = f"Invite {self.bot.user.name}",
            url = f"https://discordapp.com/oauth2/authorize?client_id={self.bot.user.id}&permissions=26688&scope=bot",
            color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["info"])
    async def stats(self, ctx):
        """View some detailed statistics about the bot."""
        commands = 0
        for COG in Config.COGS:
            commands += len(set(self.bot.cogs[COG].walk_commands()))
        channels = 0
        roles = 0
        for guild in self.bot.guilds:
            channels += len(guild.channels)
            roles += len(guild.roles)
        process = psutil.Process(os.getpid())
        total_mem = psutil.virtual_memory().total
        current_mem = process.memory_info().rss
        name = f"{self.bot.user.name}'" if self.bot.user.name[-1] == "s" else f"{self.bot.user.name}'s"
        embed = discord.Embed(
            title = f"{name} Statistics",
            timetamp = datetime.utcnow(),
            color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
        )
        embed.add_field(name = "📊 Bot Statistics", value = f"**Servers:** {len(self.bot.guilds)}\n**Users:** {len(self.bot.users)}\n**Channels:** {channels}\n**Roles:** {roles}\n**Shards:** {self.bot.shard_count} `[ID: {(ctx.guild.shard_id if ctx.guild else 0) + 1}]`", inline = False)
        embed.add_field(name = "📋 Bot Information", value = f"**Creator:** [**Polar#6880**](https://discord.com/users/619284841187246090)\n**Bot Version:** {__version__}\n**Lines of Code:** 2790\n**Commands:** {commands}")
        embed.add_field(name = "🖥 Hardware", value = f"**discord.py Version:** v{discord.__version__}\n**Python Version:** {platform.python_version()}\n**Operating System:** {platform.system()} {platform.release()} {platform.version()}\n**Memory Usage:** {(current_mem / total_mem) * 100:.2f}% ({process.memory_info().rss / 1000000:.2f}mb)", inline = False)
        await ctx.send(embed = embed)

    @commands.command()
    async def prefix(self, ctx, new_prefix = None):
        """View or set a prefix within a server."""
        if new_prefix == None or ctx.guild == None:
            embed = discord.Embed(
                description = f"Hey there, my name is { self.bot.user.name if ctx.guild == None else ctx.guild.me.display_name } and my prefix is `{get_prefix(ctx.message)}`",
                color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
            )
        else:
            if ctx.author.guild_permissions.manage_guild == False:
                embed = discord.Embed(
                    title = "Missing Permissions",
                    description = "You're missing the **Manage Server** permission which is required to change a server's prefix!",
                    color = Config.ERRORCOLOR
                )
            else:
                if len(new_prefix) > 5 and new_prefix.lower() != "remove":
                    embed = discord.Embed(
                        title = "Prefix Too Long",
                        description = "Please keep the prefix under five characters long!",
                        color = Config.ERRORCOLOR
                    )
                else:
                    embed = discord.Embed(
                        title = f"Prefix Updated",
                        description = f"My prefix is now `{ new_prefix if new_prefix.lower() != 'remove' else Config.PREFIX }`",
                        color = embed_color(ctx.author)
                    )
                    Config.CLUSTER["servers"]["prefixes"].delete_one({"_id": ctx.guild.id}) if new_prefix.lower() == "remove" else Config.CLUSTER["servers"]["prefixes"].update_one({"_id": ctx.guild.id}, {"$set": {"prefix": new_prefix}}, upsert = True)
                    if new_prefix.lower() == "remove" and ctx.guild.id in prefixes:
                        prefixes.pop(ctx.guild.id)
                    else:
                        prefixes[ctx.guild.id] = new_prefix
        await ctx.send(embed = embed)
    
    @commands.command()
    async def hug(self, ctx, target : Union[discord.Member, discord.User, int, str] = None):
        """Hug someone or receive a hug from the bot."""
        if isinstance(target, int):
            try: # Use self.bot.fetch_user to turn an int into discord.User, if discord.NotFound is raised ask the user to provide a valid user.
                target = await self.bot.fetch_user(target)
            except discord.NotFound:
                target = f"{target}"
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.ksoft.si/meme/random-image", params = {"tag": "hug"}, headers = {"Authorization": f"Bearer {Config.KSOFT_TOKEN}"}) as resp:
                data = await resp.json()
                embed = discord.Embed(
                    title = f"{ f'Have a hug {ctx.author.name}!' if target == None else f'{ctx.author.name} gave {target.name if isinstance(target, (discord.Member, discord.User)) else target} a hug, how cute!' }",
                    color = Config.MAINCOLOR
                )
                embed.set_image(url = data["url"])
                embed.set_footer(text = "Image provided by KSoft.Si")
                await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))