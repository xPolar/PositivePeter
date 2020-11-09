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
## Packages that have to be installed through the package manager.
import discord
from discord.ext import commands
## Packages on this machine.
import Config
from Utilities import embed_color, get_prefix

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    def command_help(self, ctx, name : str, description : str, usage : str, aliases : list = None):
        """Generate a help embed for commands.

        Args:
            ctx (discord.Context): discord.py's context object.
            name (str): The name of the command.
            description (str): The of the command.
            usage (str): How to use the command.
            aliases (str, optional): If there are any aliases to the command. Defaults to None.

        Returns:
            discord.Embed: The generated embed.
        """
        embed = discord.Embed(
            title = name,
            description = description,
            color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR
        )
        embed.set_author(name = "Command Help", icon_url = "https://cdn.discordapp.com/emojis/512367613339369475.png?width=834&height=834")
        embed.description = embed.description + f"\n\nPlease do: `{usage}`"
        if aliases:
            embed.description = embed.description + "\n\nAliases: " + ", ".join([ f'`{alias}`' for alias in aliases ])
        return embed
    
    @commands.group()
    async def help(self, ctx):
        """View the help menu or information on a certain command."""
        if ctx.invoked_subcommand == None:
            prefix = get_prefix(ctx.message)
            embed = discord.Embed(
                color = embed_color(ctx.author) if ctx.guild else Config.MAINCOLOR   
            )
            embed.set_author(name = "Command Help", icon_url = "https://cdn.discordapp.com/emojis/512367613339369475.png?width=834&height=834")
            if ctx.author.id in Config.OWNERIDS:
                embed.add_field(name = "Block", value = f"`{prefix}block <User> [Reason]`\n*Block a user from creating suggestions.*", inline = False)
            if ctx.guild:
                if ctx.author.guild_permissions.manage_guild:
                    embed.add_field(name = "Configuration", value = f"`{prefix}configuration <Option> [Value]`\n*Configure the bot in your server to allow for custom hotlines and disable compliments as well as set a custom number of times for the bot to be triggered before sending a DM to the user.*", inline = False)
            embed.add_field(name = "Help", value = f"`{prefix}help [Command]`\n*View the help menu or information on a certain command.*", inline = False)
            embed.add_field(name = "Hug", value = f"`{prefix}hug [User]`\n*Hug someone or receive a hug from the bot.*", inline = False)
            embed.add_field(name = "Invite", value = f"`{prefix}invite`\n*Invite {self.bot.user.name}.*", inline = False)
            embed.add_field(name = "Ping", value = f"`{prefix}ping`\n*Get the latency between our bot and Discord as well as the latency of the host.*", inline = False)
            embed.add_field(name = "Prefix", value = f"`{prefix}prefix [New Prefix]`\n*View or set a prefix within a server.*", inline = False)
            if ctx.author.id in Config.OWNERIDS:
                embed.add_field(name = "Restart", value = f"`{prefix}restart`\n*Restart the bot's cogs.*", inline = False)
            embed.add_field(name = "Stats", value = f"`{prefix}stats`\n*View some detailed statistics about the bot.*", inline = False)
            embed.add_field(name = "Suggest", value = f"`{prefix}suggest <Suggestion>`\n*Suggest a trigger to the Positive Peter Support Server!*", inline = False)
            embed.add_field(name = "Support", value = f"`{prefix}support`\n*Obtain the link to join the bot's support server.*", inline = False)
            embed.add_field(name = "Unblock", value = f"`{prefix}unblock <User> [Reason]`\n*Unblock a user from creating suggestions.*", inline = False)
            embed.add_field(name = "Vote", value = f"`{prefix}vote`\n*Obtain the link to vote for {self.bot.user.name}.*", inline = False)
            await ctx.send(embed = embed)

    @help.command(aliases = ["blacklist"])
    async def block(self, ctx):
        if ctx.author.id in Config.OWNERIDS:
            await ctx.send(embed = self.command_help(ctx, ctx.invoked_with.lower(), f"{ctx.invoked_with.title()} a user from creating suggestions.", f"{ctx.invoked_with.lower()} <User> [Reason]", ["blacklist" if ctx.invoked_with.lower() == "block" else "block"]))
    
    @help.command(aliases = ["config"])
    @commands.has_permissions(manage_guild = True)
    async def configuration(self, ctx):
        await ctx.send(embed = self.command_help(ctx, ctx.invoked_with.lower(), "Configure the bot in your server to allow for custom hotlines and disable compliments as well as set a custom number of times for the bot to be triggered before sending a DM to the user.", f"{ctx.invoked_with.lower()} <Option> [Value]", ["config" if ctx.invoked_with.lower() == "configuration" else "configuration"]))

    @help.command(name = "help")
    async def _help(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "help", "View the help menu or information on a certain command.", "help [Command]"))
    
    @help.command()
    async def hug(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "hug", f"Hug someone or receive a hug from {self.bot.user.name}.", "hug [User]"))
    
    @help.command()
    async def invite(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "invite", f"Invite {self.bot.user.name}.", "invite"))
    
    @help.command()
    async def ping(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "ping", "Get the latency between our bot and Discord as well as the latency of the host.", "ping"))
    
    @help.command()
    async def prefix(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "prefix", "View or set a prefix within a server.", "prefix [New Prefix]"))
    
    @help.command()
    async def restart(self, ctx):
        if ctx.author.id in Config.OWNERIDS:
            await ctx.send(embed = self.command_help(ctx, "restart", "Restart the bot's cogs.", "restart"))
    
    @help.command()
    async def stats(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "stats", "View some detailed statistics about the bot.", "stats"))
    
    @help.command()
    async def suggest(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "suggest", f"Suggest a trigger to the {self.bot.user.name} support server.", "suggest <Suggestion>"))
    
    @help.command()
    async def support(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "support", "Obtain the link to join the bot's support server.", "support"))
    
    @help.command(aliases = ["whitelist"])
    async def unblock(self, ctx):
        await ctx.send(embed = self.command_help(ctx, ctx.invoked_with.lower(), f"{ctx.invoked_with.title()} a user from making suggestions.", f"{ctx.invoked_with.lower()} <User> [Reason]", ["whitelist" if ctx.invoked_with.lower() == "unblock" else "unblock"]))

    @help.command()
    async def vote(self, ctx):
        await ctx.send(embed = self.command_help(ctx, "vote", f"Obtain the link to vote for {self.bot.user.name}.", "vote"))

def setup(bot):
    bot.add_cog(Help(bot))
