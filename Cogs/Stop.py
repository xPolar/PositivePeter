"""
MIT License

Copyright (c) 2020 Circl

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
## Packages that have to be installed through the package manager.
import discord
from discord.ext import commands
from colorama import Fore, Style

## Packages on this machine.
from .. import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def stop(self, ctx):
        f"""Disable or enable the {self.bot.user.name} from sending you direct messages."""
        document = Config.CLUSTER["servers"]["compliments"].find_one({"_id": ctx.guild.id})
        embed = discord.Embed(
            title = f"{ 'Contuning' if document != None else 'Stopping'} Messages",
            description = f"I will { 'now' if document != None else 'no longer' } direct message you!",
            color = Config.MAINCOLOR
        )
        Config.CLUSTER["users"]["stopped"].insert_one({"_id": ctx.guild.id}) if document == None else Config.CLUSTER["users"]["stopped"].delete_one({"_id": ctx.guild.io})
        await ctx.send(embed = embed)
    
def setup(bot):
    bot.add_cog(Misc(bot))