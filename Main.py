# Imports
import asyncio
import datetime
import discord
from discord.ext import commands
import Config
import motor.motor_asyncio
import random
import logging

# Logging system setup
logging.basicConfig(level = logging.INFO, format="Positive Peter | [%(levelname)s] | %(message)s")

# Server side prefix thing
async def get_prefix(bot, message):
    # If the command wasn't used in a server it returns the default prefix
    if message.guild is None:
        return commands.when_mentioned_or(Config.PREFIX)(bot, message)
    else:
        # Gets all the prefixes from the databse
        prefix = await Config.CLUSTER["servers"]["prefixes"].find_one({"_id": message.guild.id})
        # If it can't find a prefix for the server the command was used in it returns the default prefix
        if prefix == None:
            return commands.when_mentioned_or(Config.PREFIX)(bot, message)
        else:
            # Returns custom prefix if it does exist
            return prefix["prefix"]

# Set prefix and set case insensitive to true so a command will work if miscapitlized
bot = commands.Bot(command_prefix = get_prefix, case_insensitive = True)

# Remove default help command
bot.remove_command('help')

# Cogs
cogs = ["Prevention",
        "Volunteer",
        "Misc",
        "Other"]

# Starts all cogs
for cog in cogs:
    bot.load_extension("Cogs." + cog)

# Check to see if the user invoking the command is in the OWNERIDS Config
def owner(ctx):
    return int(ctx.author.id) in Config.OWNERIDS

# Restarts and reloads all cogs
@bot.command()
@commands.check(owner)
async def restart(ctx):
    """
    Restart the bot.
    """
    restarting = discord.Embed(
        title = "Restarting...",
        color = Config.MAINCOLOR
    )
    msg = await ctx.send(embed = restarting)
    # Gets every cog from the cog list and restarts it
    for cog in cogs:
        bot.reload_extension("Cogs." + cog)
        restarting.add_field(name = f"{cog}", value = "🔁 Restarted!")
        await msg.edit(embed = restarting)
    logging.info(f"Bot has been restarted succesfully in {len(bot.guilds)} server(s) with {len(bot.users)} users by {ctx.author.name}#{ctx.author.discriminator} (ID - {ctx.author.id})!")
    await asyncio.sleep(3)
    await msg.delete()
    if ctx.guild != None:
        try:
            await ctx.message.delete()
        except:
            pass

# Command error
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.BadArgument):
        pass
    else:
        raise error

# On ready
@bot.event
async def on_ready():
    logging.info(f"Bot has been started succesfully in {len(bot.guilds)} server(s) with {len(bot.users)} users!")

    # Loop for status
    loop = True
    while loop == True:
        statuses = [f"{Config.PREFIX}help | 1-800-273-8255",
                    f"{Config.PREFIX}help | Preventing Suicides"]
        await bot.change_presence(activity = discord.Game(random.choice(statuses)))
        await asyncio.sleep(600)

# Log whenever someone invites the bot to their server
@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(
        title = "Joined a server!",
        timestamp = datetime.datetime.utcnow(),
        color = Config.MAINCOLOR
    )
    embed.add_field(name = "Guild Name", value = guild.name)
    embed.add_field(name = "Guild Members", value = len(guild.members))
    embed.add_field(name = "Guild ID", value = guild.id)
    embed.add_field(name = "Guild Owner", value = f"{guild.owner.name}#{guild.owner.discriminator}")
    embed.add_field(name = "Guild Owner ID", value = guild.owner.id)
    embed.set_footer(text = f"I am now in {len(bot.guilds)} servers")
    channel = bot.get_channel(Config.JOIN_LOG)
    await channel.send(embed = embed)

# Starts bot
bot.run(Config.TOKEN)
