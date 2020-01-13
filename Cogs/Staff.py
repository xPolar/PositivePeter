# Imports
import asyncio
import datetime
import discord
from discord.ext import commands
import Config
import motor.motor_asyncio

class Staff(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(651230314039083008, 651230313116073990)
    async def blacklist(self, ctx, user : discord.User = None, *, reason = "No reason provided"):
        """
        Blacklist a user from being able to suggest detections.
        """
        if user == None:
            embed = discord.Embed(
                title = "Blacklist Error",
                description = "Please provide a user to blacklist!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            await Config.CLUSTER["users"]["blocked"].update_one({"_id": user.id}, {"$set": {"_id": user.id, "reason": reason}}, upsert = True)
            embed = discord.Embed(
                title = "Blacklist",
                description = f"The user `{user.name}#{user.discriminator}` has been blacklisted by `{ctx.author.display_name}#{ctx.author.discriminator}`for: {reason}!",
                color = Config.MAINCOLOR
            )
            await ctx.send(embed = embed)
            log_channel = self.bot.get_channel(651635427035447316)
            await log_channel.send(embed = embed)

    @commands.command()
    @commands.has_any_role(651230314039083008, 651230313116073990)
    async def whitelist(self, ctx, user : discord.User = None, *, reason = "No reason provided"):
        if user == None:
            embed = discord.Embed(
                title = "Whitelist Error",
                description = "Please provide a user to whitelist!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            await Config.CLUSTER["users"]["blocked"].find_one({"_id": user.id})
            if blocked == None:
                embed = discord.Embed(
                    title = "Whitelist Error",
                    description = f"{user.name}#{user.discriminator} is not blacklisted!",
                    color = Config.ERRORCOLOR
                )
                await ctx.send(embed = embed)
            else:
                await Config.CLUSTER["users"]["blocked"].delete_one({"_id": user.id})
                embed = discord.Embed(
                    title = "Whitelist",
                    description = f"The user `{user.name}#{user.discriminator}` has been whitelisted by `{ctx.author.display_name}#{ctx.author.discriminator}`for: {reason}!",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)
                log_channel = self.bot.get_channel(651635427035447316)
                await log_channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Staff(bot))
