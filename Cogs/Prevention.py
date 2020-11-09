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
from json import load
from random import choice
## Packages that have to be installed through the package manager.
import discord
from discord.ext import commands
## Packages on this machine.
import Config
from Utilities import embed_color

class Prevention(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open(r"PATH/TO/TRIGGERS/JSON") as file: # MAKE SURE TO INCLUDE THE FULL PATH TO THE FILE.
            self.triggers = load(file)

    @commands.Cog.listener()
    async def on_message(self, message):
        """Whenever a message is sent check if a response should be sent.

        Args:
            message (discord.Message): The sent message.
        """
        if message.author.bot == False:
            enabled = Config.CLUSTER["users"]["stopped"].find_one({"_id": message.author.id})
            value = enabled["value"] if enabled else True
            if value:
                for trigger in self.triggers["suicide"]:
                    trigger = trigger.lower()
                    variants = [trigger, trigger.replace("'", ""), trigger.replace("i'm", "im"), trigger.replace("i'm", "i am"), trigger.replace("want to", "wanna"), trigger.replace("can't", "cant"), trigger.replace("can't", "can not"), trigger.replace("don't", "dont"), trigger.replace("don't", "do not")]
                    for variant in variants:
                        if variant in message.content.lower():
                            Config.CLUSTER["users"]["detections"].update_one({"_id": message.author.id}, {"$inc": {"detections": 1}}, upsert = True)
                            detections = Config.CLUSTER["users"]["detections"].find_one({"_id": message.author.id})
                            count = 3
                            if message.guild:
                                count = Config.CLUSTER["servers"]["count"].find_one({"_id": message.guild.id})
                                count = count["count"] if count else 3
                            if detections["detections"] >= count:
                                embed = discord.Embed(
                                    title = "Suicide Prevention",
                                    description = f"Hey there {message.author.name}, based on your previous message I have detected hints of suicidal thoughts. If you are considering suicide please contact your local suicide prevention hotline, to find your hotline please visit [this](https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines) website.",
                                    color = embed_color(message.author) if message.guild else Config.MAINCOLOR
                                )
                                if message.guild:
                                    hotline = Config.CLUSTER["servers"]["hotlines"].find_one({"_id": message.guild.id})
                                    if hotline is not None:
                                        embed.add_field(name = "**Server Side Hotline**", value = hotline["hotline"])
                                try:
                                    await message.author.send(embed = embed)
                                except discord.Forbidden:
                                    pass
                                Config.CLUSTER["users"]["detections"].update_one({"_id": message.author.id}, {"$set": {"detections": 0}})
                            break
                if message.guild:
                    if Config.CLUSTER["servers"]["compliments"].find_one({"_id": message.guild.id}) == None:
                        for trigger in self.triggers["compliment"]:
                            lower_trigger = trigger.lower()
                            variants = [lower_trigger, lower_trigger.replace("'", ""), lower_trigger.replace("i'm", "im"), lower_trigger.replace("i'm", "i am")]
                            for variant in variants:
                                if variant in message.content.lower():
                                    if isinstance(self.triggers["compliment"][trigger], list):
                                        await message.channel.send(choice(self.triggers["compliment"][trigger]))
                                    else:
                                        await message.channel.send(self.triggers["compliment"][trigger])
                                    break

def setup(bot):
    bot.add_cog(Prevention(bot))
