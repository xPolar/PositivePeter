import asyncio
import datetime
import logging
import random

import discord
import motor.motor_asyncio
from discord.ext import commands

import Config

logging.basicConfig(level = "INFO", format = "Positive Peter |  [%(levelname)s] | %(message)s")
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

async def get_prefix(bot, message):
    if message.guild == None:
        return commands.when_mentioned_or(Config.PREFIX)(bot, message)
    else:
        prefixes = await Config.CLUSTER["servers"]["prefixes"].find_one({"_id": message.guild.id})
        if prefixes == None:
            return commands.when_mentioned_or(Config.PREFIX)(bot, message)
        else:
            return prefixes["prefix"]

bot = commands.Bot(command_prefix = get_prefix, case_insensitive = True)

bot.remove_command("help")

COGS = ["Block", "Configuration", "Ping", "Prefix", "Prevention", "Stop", "Suggest", "Vote", "Invite", "Support", "BotLists", "Help"]

for Cog in COGS:
    bot.load_extension(f"Cogs.{Cog}")
    logging.info(f"Cog: {Cog} has started.")

def owner(ctx):
    return ctx.author.id in Config.OWNER_IDS

@bot.command()
async def restart(ctx, cog = None):
    """
    Restart the bot.
    """
    if cog != None:
        cog = cog.lower().title()
        bot.reload_extension(f"Cogs.{cog}")
        logging.info(f"Cog: {cog} has been restarted.")
        embed = discord.Embed(
                title = f"Restarted {cog}",
                description = f"I have restarted cog: {cog}!",
                color = Config.MAINCOLOR
        )
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(
                title = "Restarting",
                color = Config.MAINCOLOR
        )
        msg = await ctx.send(embed = embed)
        for Cog in COGS:
            bot.reload_extension(f"Cogs.{Cog}")
            logging.info(f"Cog: {Cog} has been restarted.")
            embed.add_field(name = Cog, value = "🔄 Restarted")
            await msg.edit(embed = embed)
        logging.info(f"Bot has restarted successfully in {len(bot.guilds)} server(s) with {len(bot.users)} users!")
        await asyncio.sleep(3)
        await msg.delete()
        if ctx.guild != None:
            try:
                await ctx.message.delete()
            except:
                pass

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.BadArgument):
        return
    else:
        raise error
        try:
            embed = discord.Embed(
                    title = "Error",
                    description = f"**```\n{error}\n```**",
                    color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        except:
            pass

@bot.event
async def on_ready():
    logging.info(f"Bot has started successfully in {len(bot.guilds)} server(s) with {len(bot.users)} users!")
    while True:
        statueses = [f"{Config.PREFIX}help | 1-800-273-8255",
                     f"{Config.PREFIX}help | {Config.PREFIX}vote"]
        await bot.change_presence(activity = discord.Game(random.choice(statueses)))
        await asyncio.sleep(600)

bot.run(Config.TOKEN)
