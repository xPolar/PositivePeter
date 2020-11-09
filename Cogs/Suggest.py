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
from datetime import datetime
## Packages that have to be installed through the package manager.
import aiohttp, discord
from discord.ext import commands
## Packages on this machine.
import Config
from Utilities import embed_color

class Suggest(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def suggest(self, ctx, *, suggestion = None):
        """Suggest a trigger to the Positive Peter Support Server!"""
        blocked = Config.CLUSTER["users"]["blocked"].find_one({"_id": ctx.author.id})
        if blocked != None:
            embed = discord.Embed(
                title = "Blocked",
                description = f"You're blocked from making trigger suggestions{ ' for: ' + blocked['reason'] if blocked['reason'] != 'No reason specified.' else '!' }",
                color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
            )
        else:
            if suggestion == None:
                embed = discord.Embed(
                    title = "Empty Argument",
                    description = "Please provide a suggestion!",
                    color = Config.ERRORCOLOR
                )
            else:
                suggestion = suggestion[1:] if suggestion.startswith("[") else suggestion
                suggestion = suggestion[:-1] if suggestion.endswith("]") else suggestion
                embed = discord.Embed(
                    title = "Trigger Suggestion",
                    description = suggestion,
                    timestamp = datetime.utcnow(),
                    color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
                )
                embed.set_footer(text = f"Suggested by: {ctx.author} - ID: {ctx.author.id}")
                async with aiohttp.ClientSession() as session:
                    webhook = discord.Webhook.from_url(Config.T_WEBHOOK, adapter = discord.AsyncWebhookAdapter(session))
                    await webhook.send(embed = embed, username = "Trigger Suggestion")
                embed = discord.Embed(
                    title = "Trigger Suggested",
                    description = "I have suggested your trigger to the Positive Peter Support Server!",
                    color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
                )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Suggest(bot))
