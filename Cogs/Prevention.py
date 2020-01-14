# Imports
import asyncio
import datetime
import discord
from discord.ext import commands
import Config
import motor.motor_asyncio
import random
import logging

class Prevention(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user or message.author.bot == False:
            if message.content == "\n":
                pass
            else:
                hint_entrys1 = ["I want to die",
                               "kill myself",
                               "I want to disappear",
                               "can't wait to die",
                               "I don't want to be alive",
                               "Why am I alive",
                               "Why am I not dead",
                               "Why can't I die",
                               "I hate being alive",
                               "wish I was dead",
                               "kms",
                               "I have dreams of suicide",
                               "wish I wasn't alive",
                               "wish I didn't have to interact with people anymore",
                               "I have trouble getting out of bed in the morning",
                               "I'm going to jump off a building",
                               "slit my wrists",
                               "I'm going to hurt myself",
                               "hang myself",
                               "I'm suicidal",
                               "please kill me",
                               "kill me please"
                               "I don't want to live",
                               "shoot myself",
                               "cut myself",
                               "I don't want to live anymore",
                               "I kinda want to die"]
                hint_entrys2 = {"I suck": random.choice(["Everyone has imperfections, you're great!",
                                           "No you don't you're great!",
                                           "You're amazing!"]),
                               "hate myself": random.choice(["You're awesome don't worry!",
                                                             "You have nothing to hate, you're a great person"]),
                               "I'm sad": random.choice(["Don't be sad, you're great!",
                                                         "You have nothing to be sad about, you're an amazing person!"]),
                               "I'm worthless": random.choice(["No you're not, you're amazing!",
                                                               "You're worth every dollar in the world.",
                                                               "You're priceless!"]),
                               "I'm ass": "No you're amazing",
                               "I'm trash": random.choice(["You're not trash, you're gold!",
                                                           "No you're not, you're amazing!",
                                                           "You're breathtaking!"]),
                               "I'm dumb": random.choice(["You're one of the most intelligent people I know!",
                                                          "You're extremely smart!"]),
                               "I'm an idiot": random.choice(["You're one of the most intelligent people I know!",
                                                              "You're extremely smart!"]),
                               "I'm ugly": random.choice(["You're breathtaking!",
                                                          "No you don't, you look just like Keanu Reaves!"]),
                               "I'm shit": "You're amazing!"}
                two_k = "eu non diam phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim tortor at auctor urna nunc id cursus metus aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci a scelerisque purus semper eget duis at tellus at urna condimentum mattis pellentesque id nibh tortor id aliquet lectus proin nibh nisl condimentum id venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas sed tempus urna et pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna eget est lorem ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas integer eget aliquet nibh praesent tristique magna sit amet purus gravida quis blandit turpis cursus in hac habitasse platea dictumst quisque sagittis purus sit amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus mauris a diam maecenas sed enim ut sem viverra aliquet eget sit amet tellus cras adipiscing enim eu turpis egestas pretium aenean pharetra magna ac placerat vestibulum lectus mauris ultrices eros in cursus turpis massa tincidunt dui ut ornare lectus sit amet est placerat in egestas erat imperdiet sed euismod nisi porta lorem mollis aliquam ut porttitor leo a diam sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit amet risus nullam eget felis eget nunc lobortis mattis aliquam faucibus purus in massa tempor nec feugiat nisl pretium fusce id velit ut tortor pretium viverra suspendisse potenti nullam ac tortor vitae purus faucibus ornare suspendisse sed nisi lacus sed viverra tellus in hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu dictum varius duis at consectetur lorem donec massa sapien faucibus et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed ullamcorper"
                entry2 = two_k
                entry3 = two_k
                entry4 = two_k
                entry5 = two_k
                entry6 = two_k
                entry7 = two_k
                entry8 = two_k
                entry9 = two_k
                if message.guild != None:
                    config = await Config.CLUSTER["servers"]["configs"].find_one({"_id": message.guild.id})
                else:
                    config = None
                for entry in hint_entrys1:
                    if "'" in entry:
                        entry2 = entry.lower().replace("'", "")
                    if "i'm" in entry.lower():
                        entry3 = entry.lower().replace("i'm", "i am")
                    if "don't" in entry.lower():
                        entry4 = entry.lower().replace("don't", "do not")
                    if "want to" in entry.lower():
                        entry5 = entry.lower().replace("want to", "wanna")
                    if "can't" in entry.lower():
                        entry6 = entry.lower().replace("can't", "can not")
                    if " " in entry:
                        entry7 = entry.lower().replace(" ", "-")
                        entry8 = entry.lower().replace(" ", "_")
                    if "kinda" in entry:
                        entry9 = entry.replace("kinda", "kind of")
                    if entry.lower() in message.content.lower() or entry2 in message.content.lower() or entry3 in message.content.lower() or entry4 in message.content.lower() or entry5 in message.content.lower() or entry6 in message.content.lower() or entry7 in message.content.lower() or entry8 in message.content.lower() or entry9 in message.content.lower():
                        await Config.CLUSTER["users"]["detections"].update_one({"_id": message.author.id}, {"$push": {"detections": entry}}, upsert = True)
                        detections = await Config.CLUSTER["users"]["detections"].find_one({"_id": message.author.id})
                        if detections != None:
                            if len(detections["detections"]) >= 5:
                                embed = discord.Embed(
                                    title = "Suicide Prevention",
                                    description = f"Hey there {message.author.name}, based on your previous message I have detected hints of suicidal thoughts. If you are considering suicide please contact your local suicide prevention hotline, to find your hotline please visit [this](https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines) website.",
                                    color = Config.MAINCOLOR
                                )
                                embed.add_field(name = "Contact a volunteer", value = "If you want to talk to a Discord volunteer please react to this message with 🦺 (:safetyvest\:).")
                                if config != None:
                                    if "hotline" in config:
                                        embed.add_field(name = "Server's custom set hotline", value = config["hotline"], inline = False)
                                msg = await message.author.send(embed = embed)
                                await msg.add_reaction("🦺")
                                await Config.CLUSTER["users"]["detections"].delete_one({"_id": message.author.id})
                                break
                    else:
                        continue
                if message.guild == None:
                    value = True
                else:
                    if config == None:
                        value = True
                    else:
                        value = config["compliment"]
                if value == True:
                    for entry in hint_entrys2:
                        if "'" in entry:
                            entry2 = entry.lower().replace("'", "")
                        if "i'm" in entry.lower():
                            entry3 = entry.lower().replace("i'm", "i am")
                        if "don't" in entry.lower():
                            entry4 = entry.lower().replace("don't", "do not")
                        if "want to" in entry.lower():
                            entry5 = entry.lower().replace("want to", "wanna")
                        if "can't" in entry.lower():
                            entry6 = entry.lower().replace("can't", "can not")
                        if " " in entry:
                            entry7 = entry.lower().replace(" ", "-")
                            entry8 = entry.lower().replace(" ", "_")
                        if entry.lower() in message.content.lower() or entry2 in message.content.lower() or entry3 in message.content.lower() or entry4 in message.content.lower() or entry5 in message.content.lower() or entry6 in message.content.lower() or entry7 in message.content.lower() or entry8 in message.content.lower():
                            if "I suck dick" in message.content.lower() or "assuming" in message.content.lower() or "sadistic" in message.content.lower():
                                continue
                            else:
                                await message.channel.send(hint_entrys2[entry])
                                break
                        else:
                            continue

def setup(bot):
    bot.add_cog(Prevention(bot))
