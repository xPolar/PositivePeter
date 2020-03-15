# Imports
import asyncio
import random

import discord
import motor.motor_asyncio
from discord.ext import commands

import Config

class Prevention(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            enabled = await Config.CLUSTER["users"]["stopped"].find_one({"_id": message.author.id})
            if enabled == None:
                value = True
            else:
                value = enabled["value"]
            if value == True:
                suicide_triggers = ["I wish I was never born", "I want to die", "KMS", "Kill Myself",
                                    "I'm going to suffocate myself", "I'm going to commit suicide",
                                    "I just want to die", "I'm planning on commiting suicide",
                                    "I took an overdose", "I just want to die", "Time to die I guess",
                                    "Why am I alive", "Kill me", "End me", "I have trouble getting out of bed in the morning",
                                    "Killing myself", "I want to commit suicide", "I deserve to die",
                                    "Would anyone miss me?", "I really want to die", "I want to disappear",
                                    "Can't wait to die", "I don't want to be alive", "I hate being alive",
                                    "Why am I not dead", "Wish I was dead", "I'm going to jump off a building",
                                    "Hurt myself", "Hang myself", "I'm suicidal", "I don't want to live", "Shoot myself",
                                    "Cut myself", "I don't want to live anymore", "I kinda want to die"]
                for trigger in suicide_triggers:
                    trigger1 = trigger.lower()
                    trigger2 = trigger1.replace(" ", "")
                    trigger3 = trigger1.replace("i'm", "im")
                    trigger4 = trigger1.replace("i'm", "i am")
                    trigger5 = trigger1.replace("want to", "wanna")
                    trigger6 = trigger1.replace("can't", "cant")
                    trigger7 = trigger1.replace("can't", "can not")
                    trigger8 = trigger1.replace("don't", "dont")
                    trigger9 = trigger1.replace("don't", "do not")
                    if trigger1 in message.content.lower() or trigger2 in message.content.lower() or trigger3 in message.content.lower() or trigger4 in message.content.lower() or trigger5 in message.content.lower() or trigger6 in message.content.lower() or trigger7 in message.content.lower() or trigger8 in message.content.lower() or trigger9 in message.content.lower():
                        await Config.CLUSTER["users"]["detections"].update_one({"_id": message.guild.id}, {"$inc": {"detections": 1}}, upsert = True)
                        detections = await Config.CLUSTER["users"]["detections"].find_one({"_id": message.guild.id})
                        if detections["detections"] >= 3:
                            embed = discord.Embed(
                                title = "Suicide Prevention",
                                description = f"Hey there {message.author.name}, based on your previous message I have detected hints of suicidal thoughts. If you are considering suicide please contact your local suicide prevention hotline, to find your hotline please visit [this](https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines) website.",
                                color = Config.MAINCOLOR
                            )
                            hotline = await Config.CLUSTER["servers"]["hotlines"].find_one({"_id": message.guild.id})
                            if hotline != None:
                                embed.add_field(name = "**Server Side Hotline**", value = hotline["hotline"])
                            await message.author.send(embed = embed)
                            await Config.CLUSTER["users"]["detections"].delete_one({"_id": message.guild.id})
                        break
                if message.guild != None:
                    enabled = await Config.CLUSTER["servers"]["compliments"].find_one({"_id": message.guild.id})
                    if enabled == None:
                        value = True
                    else:
                        value = enabled["value"]
                    if value == True:
                        compliment_triggers = {"I'm worthless": ["No you're not!", "You're priceless", "You're worth more then diamonds!"],
                                               "I'm not good enough": "You're way more then enough", "Why am I not good enough?": "You're way more then enough",
                                               "I can't do anything right": ["You're doing just fine!", "You're perfect!"], "I suck": ["No you don't you're amazing!",
                                               "Everyone has imperfections, you're great", "You're amazing"], "I'm sad": ["Don't be sad, you're great!"],
                                               "I'm trash": ["You're not trash, you're gold", "No you're not, you're amazing!"], "I'm dumb": ["No you're not!",
                                               "You're one of the smartest people I know!", "You're extremely intilligent!"], "I'm an idiot": ["No you're not!",
                                               "You're one of the smartest people I know!", "You're extremely intilligent!"], "I'm ugly": ["You're breathtaking!",
                                               "No you're not, you're amazing!"]}
                        for trigger in compliment_triggers:
                            trigger1 = trigger.lower()
                            trigger2 = trigger1.replace("'", "")
                            trigger3 = trigger1.replace("i'm", "im")
                            trigger4 = trigger1.replace("i'm", "i am")
                            if trigger1 in message.content.lower() or trigger2 in message.content.lower() or trigger3 in message.content.lower() or trigger4 in message.content.lower():
                                if str(type(compliment_triggers[trigger])) == "<class 'list'>":
                                    await message.channel.send(random.choice(compliment_triggers[trigger]))
                                    break
                                else:
                                    await message.channel.send(compliment_triggers[trigger])
                            
def setup(bot):
    bot.add_cog(Prevention(bot))
