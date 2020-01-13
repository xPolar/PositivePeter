# Imports
import asyncio
import datetime
import discord
from discord.ext import commands
import Config
import motor.motor_asyncio
import googletrans
from googletrans import Translator
import random
translator = Translator()

class Prevention(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            if message.content == "\n":
                pass
            else:
                translate = translator.translate(text = message.content)
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
                entry2 = "\n"
                entry3 = "\n"
                entry4 = "\n"
                entry5 = "\n"
                entry6 = "\n"
                entry7 = "\n"
                entry8 = "\n"
                entry9 = "\n"
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
                    if entry.lower() in translate.text.lower() or entry2 in translate.text.lower() or entry3 in translate.text.lower() or entry4 in translate.text.lower() or entry5 in translate.text.lower() or entry6 in translate.text.lower() or entry7 in translate.text.lower() or entry8 in translate.text.lower() or entry9 in translate.text.lower():
                        await Config.CLUSTER["users"]["detections"].update_one({"_id": message.author.id}, {"$push": {"detections": entry}}, upsert = True)
                        detections = await Config.CLUSTER["users"]["detections"].find_one({"_id": message.author.id})
                        if detections != None:
                            if len(detections["detections"]) >= 5:
                                embed = discord.Embed(
                                    title = translator.translate("Suicie Prevention", dest = translate.src).text,
                                    description = translator.translate(f"Hey there {message.author.name}, based on your previous message I have detected hints of suicidal thoughts. If you are considering suicide please contact your local suicide prevention hotline, to find your hotline please visit [this]", dest = translate.src).text + "(https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines) " + translator.translate("website.", dest = translate.src).text,
                                    color = Config.MAINCOLOR
                                )
                                embed.add_field(name = translator.translate("Contact a volunteer", dest = translate.src).text, value = translator.translate("If you want to talk to a Discord volunteer please react to this message with", dest = translate.src).text + " 🦺 (:safetyvest\:).")
                                if config != None:
                                    if "hotline" in config:
                                        embed.add_field(name = translator.translate("Server's custom set hotline", dest = translate.src).text, value = translator.translate(config["hotline"], dest = translate.src).text, inline = False)
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
                        if entry.lower() in translate.text.lower() or entry2 in translate.text.lower() or entry3 in translate.text.lower() or entry4 in translate.text.lower() or entry5 in translate.text.lower() or entry6 in translate.text.lower() or entry7 in translate.text.lower() or entry8 in translate.text.lower():
                            if "I suck dick" in translate.text.lower() or "assuming" in translate.text.lower() or "sadistic" in translate.text.lower():
                                continue
                            else:
                                await message.channel.send(translator.translate(hint_entrys2[entry], dest = translate.src).text)
                                break
                        else:
                            continue

def setup(bot):
    bot.add_cog(Prevention(bot))
