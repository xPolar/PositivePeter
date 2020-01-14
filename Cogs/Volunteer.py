# Imports
import asyncio
import datetime
import discord
from discord.ext import commands
import Config
import motor.motor_asyncio

class Volunteer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user != self.bot.user:
            if reaction.emoji == "🦺":
                if "🦺" in reaction.message.embeds[0].fields[0].value and reaction.message.author == self.bot.user:
                    thread = await Config.CLUSTER["user"]["threads"].find_one({"_id": user.id})
                    if thread == None:
                        embed = discord.Embed(
                            title = f"New Thread",
                            description = f"`{user.name}#{user.discriminator}` has requested to talk to a volunteer!",
                            timestamp = datetime.datetime.utcnow(),
                            color = Config.MAINCOLOR
                        )
                        embed.set_footer(text = f"User ID: {user.id}")
                        channel = self.bot.get_channel(Config.THREAD_CHANNEL)
                        msg = await channel.send(embed = embed)
                        await Config.CLUSTER["user"]["threads"].insert_one({"_id": user.id, "msg_id": msg.id})
                        embed = discord.Embed(
                            title = "Thread Created",
                            description = "A thread has been created for you, please wait for the next avaliale volunteer.",
                            color = Config.MAINCOLOR
                        )
                        await user.send(embed = embed)

    @commands.command()
    @commands.has_any_role(Config.VOLUNTEER_ROLE)
    async def claim(self, ctx, user : discord.User = None):
        """
        Claim a thread.
        """
        if user == None:
            embed = discord.Embed(
                title = "Claim Error",
                description = "Please provide a valid ID!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            thread = await Config.CLUSTER["user"]["threads"].find_one({"_id": user.id})
            if thread == None:
                embed = discord.Embed(
                    title = f"Claim Error",
                    description = f"`{user.name}#{user.discriminator}` doesn't currently have a thread open!",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)
            else:
                channel = self.bot.get_channel(Config.THREAD_CHANNEL)
                msg = await channel.fetch_message(thread["msg_id"])
                embed = discord.Embed(
                    title = "Claimed Thread",
                    description = f"{ctx.author.mention} has claimed this thread, if you would like to help them please send them a direct message.",
                    timestamp = datetime.datetime.utcnow(),
                    color = Config.MAINCOLOR
                )
                embed.set_footer(text = f"This thread was created for {user.name}#{user.discriminator}. User ID: {user.id}")
                thread = await Config.CLUSTER["user"]["threads"].update_one({"_id": user.id}, {"$set": {"claimed_by": ctx.author.id}})
                await msg.edit(embed = embed)
                embed = discord.Embed(
                    title = "You're thread has been claimed!",
                    description = f"`{ctx.author.name}#{ctx.author.discriminator}` has claimed your thread, they will send you a friend request soon. Please make sure you have your friend requests enabled. If you don't know how to do this please follow [this](https://support.discordapp.com/hc/en-us/articles/217916488-Blocking-Privacy-Settings-) guide.",
                    color = Config.MAINCOLOR
                )
                await user.send(embed = embed)

    @claim.error
    async def claim_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title = "Claim Error",
                description = f"Please provide a valid ID!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_any_role(Config.VOLUNTEER_ROLE)
    async def close(self, ctx, user : int):
        """
        Close a thread.
        """
        if user == None:
            embed = discord.Embed(
                title = "Close Error",
                description = "Please provide a valid ID!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            thread = await Config.CLUSTER["user"]["threads"].find_one({"_id": user})
            if thread == None:
                embed = discord.Embed(
                    title = f"Close Error",
                    description = f"This user doesn't currently have a thread open!",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)
            else:
                await Config.CLUSTER["user"]["threads"].delete_one({"_id": user})
                channel = self.bot.get_channel(Config.THREAD_CHANNEL)
                msg = await channel.fetch_message(thread["msg_id"])
                embed = discord.Embed(
                    title = "Closed Thread",
                    description = f"{ctx.author.mention} has closed this thread.",
                    timestamp = datetime.datetime.utcnow(),
                    color = Config.MAINCOLOR
                )
                embed.set_footer(text = f"User ID: {user}")
                await msg.edit(embed = embed)

    @close.error
    async def close_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title = "Close Error",
                description = f"Please provide a valid ID!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Volunteer(bot))
