# Imports
import asyncio

import discord
from discord.ext import commands

import Config

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, suggestion = None):
        """
        Suggest a trigger to be voted on by the [Positive Peter Support Discord](https://discord.gg/VwMWj2B).
        """
        blocked = await Config.CLUSTER["users"]["blocked"].find_one({"_id": ctx.author.id})
        if blocked != None:
            embed = discord.Embed(
                title = "Blocked",
                description = f"You're blocked from making suggestions for: {blocked['reason']}",
                color = Config.MAINCOLOR
            )
            await ctx.send(embed = embed)
        else:
            if suggestion == None:
                embed = discord.Embed(
                    title = "Error",
                    description = "Please provide a suggestion!",
                    color = Config.ERRORCOLOR
                )
                await ctx.send(embed = embed)
            else:
                if suggestion.startswith("[") == True:
                    suggestion = suggestion[1]
                if suggestion.endswith("]") == True:
                    suggestion = suggestion[:-1]
                embed = discord.Embed(
                    title = "Trigger Suggestion",
                    description = suggestion,
                    color = Config.MAINCOLOR
                )
                embed.set_footer(text = f"Suggested by {ctx.author}. ID: {ctx.author.id}")
                channel = self.bot.get_channel(Config.TRIGGER_SUGGEST_LOG)
                msg = await channel.send(embed = embed)
                await msg.add_reaction("✅")
                await msg.add_reaction("❌")
                embed = discord.Embed(
                    title = "Trigger Suggested",
                    description = "I have suggested your trigger to the Positive Peter community!",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Misc(bot))
