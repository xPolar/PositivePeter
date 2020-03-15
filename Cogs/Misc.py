# Imports
import asyncio
import datetime
import discord
from discord.ext import commands
import Config
import motor.motor_asyncio
import io
import time
import random

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, member : discord.Member = None):
        """
        Send a hug to someone or recieve one from the bot.
        """
        list = ["https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498",
                "https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
                "https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716",
                "https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
                "https://media1.tenor.com/images/2e155cdda36fc8f806931cd019e9a518/tenor.gif?itemid=15668356",
                "https://media1.tenor.com/images/5845f40e535e00e753c7931dd77e4896/tenor.gif?itemid=9920978",
                "https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705",
                "https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif?itemid=10522729",
                "https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788",
                "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
                "https://media1.tenor.com/images/34a1d8c67e7b373de17bbfa5b8d35fc0/tenor.gif?itemid=8995974",
                "https://media1.tenor.com/images/18474dc6afa97cef50ad53cf84e37d08/tenor.gif?itemid=12375072",
                "https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935",
                "https://media1.tenor.com/images/40aed63f5bc795ed7a980d0ad5c387f2/tenor.gif?itemid=11098589",
                "https://media1.tenor.com/images/460c80d4423b0ba75ed9592b05599592/tenor.gif?itemid=5044460",
                "https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/tenor.gif?itemid=15249774",
                "https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif?itemid=7552093",
                "https://media1.tenor.com/images/44b4b9d5e6b4d806b6bcde2fd28a75ff/tenor.gif?itemid=9383138",
                "https://media1.tenor.com/images/af76e9a0652575b414251b6490509a36/tenor.gif?itemid=5640885",
                "https://media1.tenor.com/images/45b1dd9eaace572a65a305807cfaec9f/tenor.gif?itemid=6238016",
                "https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif?itemid=3532079",
                "https://media1.tenor.com/images/d3dca2dec335e5707e668b2f9813fde5/tenor.gif?itemid=12668677",
                "https://media1.tenor.com/images/54e97e0cdeefea2ee6fb2e76d141f448/tenor.gif?itemid=11378437",
                "https://media1.tenor.com/images/aeb42019b0409b98aed663f35b613828/tenor.gif?itemid=14108949",
                "https://media1.tenor.com/images/1d91e026ddbb19e7b00bd06b1032ef69/tenor.gif?itemid=15546819",
                "https://media1.tenor.com/images/d6510db0a868cfbff697d7279aa89b61/tenor.gif?itemid=10989534",
                "https://media1.tenor.com/images/112c2abcf585b37e6c6950ebc3ab4168/tenor.gif?itemid=5960669",
                "https://media1.tenor.com/images/684efd91473dcfab34cb78bf16d211cf/tenor.gif?itemid=14495459",
                "https://media.giphy.com/media/qscdhWs5o3yb6/giphy.gif",
                "https://media.giphy.com/media/rSNAVVANV5XhK/giphy.gif",
                "https://thumbs.gfycat.com/JubilantImaginativeCuttlefish-max-1mb.gif",
                "https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
                "https://media.giphy.com/media/C4gbG94zAjyYE/giphy.gif",
                "https://thumbs.gfycat.com/AffectionateWelldocumentedKitfox-small.gif",
                "https://i.pinimg.com/originals/02/7e/0a/027e0ab608f8b84a25b2d2b1d223edec.gif",
                "https://78.media.tumblr.com/f95126745e7f608d3718adae179fad6e/tumblr_o6yw691YXE1vptudso1_500.gif",
                "https://i.pinimg.com/originals/4b/8f/5c/4b8f5ca7bf41461a19e3b4d1e64c1eb5.gif",
                "https://media1.tenor.com/images/6ac90d7bd8c1c3c61e6a317e4abf260e/tenor.gif?itemid=12668472",
                "https://media1.tenor.com/images/11b756289eec236b3cd8522986bc23dd/tenor.gif?itemid=10592083"]
        if member == None:
            embed = discord.Embed(
                title = "Hug",
                color = Config.MAINCOLOR
            )
            embed.set_image(url = random.choice(list))
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(
                title = "Hug",
                description = f"{ctx.author.display_name} has hugged {member.display_name}!",
                color = Config.MAINCOLOR
            )
            embed.set_image(url = random.choice(list))
            await ctx.send(embed = embed)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title = "Hug Error",
                description = f"Please provide a valid member!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)

    @commands.command(aliases = ["latency"])
    async def ping(self, ctx):
        """
        Show the bot's current latency.
        """
        embed = discord.Embed(
            title = "Ping",
            description = "Pinging...",
            color = Config.MAINCOLOR
        )
        t1 = time.perf_counter()
        msg = await ctx.send(embed = embed)
        t2 = time.perf_counter()
        embed = discord.Embed(
            title = "🏓 Pong!",
            description = f"API latency is {round((t2 - t1) * 1000)}ms\nLatency is {round(self.bot.latency * 1000, 2)}ms",
            color = Config.MAINCOLOR
        )
        await msg.edit(embed = embed)

    @commands.command()
    async def triggers(self, ctx):
        """
        View all of the words that triggers the bot.
        """
        embed = discord.Embed(
            title = "Triggers",
            description = f"**Suicidal Triggers**\nI want to die\nkill myself\nI want to disappear\ncan't wait to die\nI don't want to be alive\nWhy am I alive\nWhy am I not dead\nWhy can't I die\nI hate being alive\nwish I was dead\nkms\nI have dreams of suicide\nwish I wasn't alive\nwih I didn't have to interact with people anymore\nI have trouble getting out of bed in the morning\nI'm going to jump off a building\nslit my wrists\nI'm going to hurt myself\nhang myself\nI'm suicidal\nplease kill me\nkill me please\nI don't want to live\nshoot myself\ncut myself\nI don't want to live anymore\nI kinda want to die\n**Compliment Triggers**\nI suck\nhate myself\nI'm sad\nI'm worthless\nI'm ass\nI'm trash\nI'm dumb\nI'm an idiot\nI'm ugly\nI'm shit",
            color = Config.MAINCOLOR
        )
        await ctx.send(embed = embed)

    @commands.command()
    async def changelog(self, ctx):
        """
        View all the updates that have been made to the bot.
        """
        if ctx.guild is None:
            prefix = f"{Config.PREFIX}"
        else:
            prefix = await Config.CLUSTER["servers"]["prefixes"].find_one({"_id": ctx.guild.id})
            if prefix == None:
                prefix = f"{Config.PREFIX}"
            else:
                prefix =  prefix["prefix"]
        emojilist = ["⏮️",
                     "◀️",
                     "⏹️",
                     "▶️",
                     "⏭️"
                     ]
        v1 = discord.Embed(
            title = "Update 1.0",
            description = "Bot has been released for private testing.",
            timestamp = datetime.datetime(2019, 11, 29, 22, 30),
            color = Config.MAINCOLOR
        )
        v2 = discord.Embed(
            title = "Update 1.0.1",
            description = f"New update system `{prefix}update`.",
            timestamp = datetime.datetime(2019, 11, 29, 7, 22),
            color = Config.MAINCOLOR
        )
        v3 = discord.Embed(
            title = "Update 1.0.2",
            description = "Added triggers for negative things, now it'll compliment you. Triggers are: `I hate myself` `I suck` `I'm sad` `Im sad`.",
            timestamp = datetime.datetime(2019, 11, 29, 7, 33),
            color = Config.MAINCOLOR
        )
        v4 = discord.Embed(
            title = "Update 1.0.3",
            description = f"Database intergration has been added (Custom prefixes), several new commands including `{prefix}help`, `{prefix}ping` `{prefix}invite` `{prefix}prefix`.",
            timestamp = datetime.datetime(2019, 11, 30, 8, 39),
            color = Config.MAINCOLOR
        )
        v5 = discord.Embed(
            title = "Update 1.0.4",
            description = "Updated the OUATH2 link from being admin to only the required permissions.\nAlso fixed bug with the update system.",
            timestamp = datetime.datetime(2019, 11, 30, 21, 20),
            color = Config.MAINCOLOR
        )
        v6 = discord.Embed(
            title = "Update 1.0.5",
            description = "Added a lot more triggers for negative and suicidal things, find a list of all triggers [here](https://mystb.in/raw/ovizuzuxag). Bot will now also detect if you use `-` or `_` instead of spaces as well as a more advanced detection system.",
            timestamp = datetime.datetime(2019, 11, 30, 22, 31),
            color = Config.MAINCOLOR
        )
        v7 = discord.Embed(
            title = "Update 1.0.6",
            description = f"Fixed the OUATH2 link so the `{prefix}changelog` command works better. Also added a `{prefix}suggesttrigger` command so you guys can help with the bot.",
            timestamp = datetime.datetime(2019, 12, 1, 9, 15),
            color = Config.MAINCOLOR
        )
        v8 = discord.Embed(
            title = "Update 1.0.7",
            description = f"Fixed a bug with `{prefix}suggettrigger`, if you have previously suggested a trigger please resuggest it!",
            timestamp = datetime.datetime(2019, 12, 1, 20, 55),
            color = Config.MAINCOLOR
        )
        v9 = discord.Embed(
            title = "Update 1.1.0",
            description = f"Added a system to connect with volunteers and talk to real people.\nUpdated the `{prefix}invite` command.\nAdded a few more triggers.\nAlso a huge thank you to everyone who has supported this bot. It's crazy to see how this bot blew up in less a week we have reached four hundred servers!",
            timestamp = datetime.datetime(2019, 12, 4, 1, 0),
            color = Config.MAINCOLOR
        )
        v10 = discord.Embed(
            title = "Update 1.2.0",
            description = f"**Added**\nOptimization\nTargetable hugs with the `{prefix}hug` command\nCustom settings on a per server basis for settings such as disabling compliments and setting custom hotlines.\n",
            timestamp = datetime.datetime(2020, 1, 13, 23, 58),
            color = Config.MAINCOLOR
        )
        message = await ctx.send(embed = v10)
        async def pagination(self, ctx, page):
            if page <= 0:
                await pagination(self, ctx, 10)
            else:
                try:
                    await message.clear_reactions()
                except:
                    for emoji in emojilist:
                        await message.remove_reaction(emoji, self.bot.user)
                for emoji in emojilist:
                    if page == 10:
                        if emoji == "◀️" or emoji == "⏮️":
                            pass
                        else:
                            await message.add_reaction(emoji)
                    elif page == 1:
                        if emoji == "▶️" or emoji == "⏭️":
                            pass
                        else:
                            await message.add_reaction(emoji)
                    else:
                        await message.add_reaction(emoji)
                def check(r, u):
                    if r.emoji in emojilist and u.id == ctx.author.id and r.message.id == message.id:
                        return True
                try:
                    waited_for = await self.bot.wait_for("reaction_add", timeout = 120, check = check)
                except asyncio.TimeoutError:
                    for emoji in emojilist:
                        await message.remove_reaction(emoji, self.bot.user)
                else:
                    reaction = waited_for[0]
                    if reaction.emoji == "⏮️":
                        page = 10
                    elif reaction.emoji == "◀️":
                        page += 1
                    elif reaction.emoji == "⏹️":
                        await message.delete()
                    elif reaction.emoji == "▶️":
                        page -=1
                    elif reaction.emoji == "⏭️":
                        page = 1
                    if page == 1:
                        if message.embeds[0].title == "Update 1.0":
                            pass
                        else:
                            await message.edit(embed = v1)
                            await pagination(self, ctx, 1)
                    elif page == 2:
                        await message.edit(embed = v2)
                        await pagination(self, ctx, 2)
                    elif page == 3:
                        await message.edit(embed = v3)
                        await pagination(self, ctx, 3)
                    elif page == 4:
                        await message.edit(embed = v4)
                        await pagination(self, ctx, 4)
                    elif page == 5:
                        await message.edit(embed = v5)
                        await pagination(self, ctx, 5)
                    elif page == 6:
                        await message.edit(embed = v6)
                        await pagination(self, ctx, 6)
                    elif page == 7:
                        await message.edit(embed = v7)
                        await pagination(self, ctx, 7)
                    elif page == 8:
                        await message.edit(embed = v8)
                        await pagination(self, ctx, 8)
                    elif page == 9:
                        await message.edit(embed = v9)
                    elif page == 10:
                        if message.embeds[0].title == "Update 1.2.0":
                            pass
                        else:
                         await message.edit(embed = v10)
                        await pagination(self, ctx, 10)
        await pagination(self, ctx, 10)

    @commands.group()
    @commands.has_permissions(manage_guild = True)
    async def config(self, ctx):
        """
        Edit the bot's configuration settings.
        """
        if ctx.guild is None:
            prefix = f"{Config.PREFIX}"
        else:
            prefix = await Config.CLUSTER["servers"]["prefixes"].find_one({"_id": ctx.guild.id})
            if prefix == None:
                prefix = f"{Config.PREFIX}"
            else:
                prefix =  prefix["prefix"]
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                title = "Configuration",
                description = f"To edit a configutation please do `{prefix}config (Setting) (Value)`.",
                color = Config.MAINCOLOR
            )
            embed.add_field(name = "Responses", value = "`compliment` - **Disable or enable the compliment responses**\n`hotline` - **Set the custom hotline in the suicidal response message**", inline = False)
            embed.add_field(name = "Server", value = "`prefix` - **Set a server's custom prefix**", inline = False)
            await ctx.send(embed = embed)

    @config.command()
    async def compliment(self, ctx, value : bool = None):
        """
        Disable or enable the compliment responses.
        """
        if bool == None:
            embed = discord.Embed(
                title = "Config Error",
                description = "Please provide a valid value!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            await Config.CLUSTER["servers"]["configs"].update_one({"_id": ctx.guild.id}, {"$set": {"_id": ctx.guild.id, "compliment": value}}, upsert = True)
            embed = discord.Embed(
                title = "Config",
                description = f"You have the config variable for `compliment` to `{value}`.",
                color = Config.MAINCOLOR
            )
            await ctx.send(embed = embed)

    @config.command()
    async def hotline(self, ctx, *, value = None):
        """
        Set the custom hotline in the suicidal response message.
        """
        if value == None:
            embed = discord.Embed(
                title = "Config Error",
                description = "Please provide a valid value!",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            await Config.CLUSTER["servers"]["configs"].update_one({"_id": ctx.guild.id}, {"$set": {"_id": ctx.guild.id, "hotline": value}}, upsert = True)
            embed = discord.Embed(
                title = "Config",
                description = f"You have set the config veriable for `hotline` to `{value}`.",
                color = Config.MAINCOLOR
            )
            await ctx.send(embed = embed)

    @config.command()
    async def prefix(self, ctx, *, value = None):
        """
        Set a server's custom prefix.
        """
        if value == None:
            embed = discord.Embed(
                title = "Prefix Error",
                description = "Please specify a prefix",
                color = Config.ERRORCOLOR
            )
            await ctx.send(embed = embed)
        else:
            if value.lower() == "reset":
                await Config.CLUSTER["servers"]["prefixes"].delete_one({"_id": ctx.guild.id})
                embed = discord.Embed(
                    title = "Prefix",
                    description = f"You have reset {ctx.guild.name}'s prefix.",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    title = "Prefix",
                    description = f"You have set {ctx.guild.name}'s prefix to `{value}`",
                    color = Config.MAINCOLOR
                )
                await Config.CLUSTER["servers"]["prefixes"].update_one({"_id": ctx.guild.id}, {"$set": {"prefix": value}}, upsert = True)
                await ctx.send(embed = embed)

    @commands.command(aliases = ["support", "vote"])
    async def invite(self, ctx):
        """
        View all of the bot's relevant links.
        """
        embed = discord.Embed(
            description = f"[`Support Server`](https://discord.gg/VwMWj2B)\n[`Bot Invite Link`](https://discordapp.com/api/oauth2/authorize?client_id=649535694145847301&permissions=26688&scope=bot)\n[`Vote Link`](https://top.gg/bot/649535694145847301/vote)",
            color = Config.MAINCOLOR
        )
        embed.set_author(name = "Invite Links", icon_url = self.bot.user.avatar_url)
        embed.set_footer(text = f"I'm currently in {len(self.bot.guilds)} servers!")
        await ctx.send(embed = embed)

    @commands.command()
    async def suggesttrigger(self, ctx, *, trigger = None):
        """
        Suggest a trigger to be added to the detection system.
        """
        blocked = await Config.CLUSTER["users"]["blocked"].find_one({"_id": ctx.author.id})
        if blocked != None:
            embed = discord.Embed(
                title = "Trigger Suggestion Error",
                description = "You have been blocked from making suggestions.",
                color = Config.ERRORCOLOR
            )
            embed.add_field(name = "Reason for being blocked", value = blocked["reason"])
            await ctx.send(embed = embed)
        else:
            if trigger == None:
                embed = discord.Embed(
                    title = "Trigger Suggestion Error",
                    description = "Please provide a trigger to suggest!",
                    color = Config.ERRORCOLOR
                )
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(
                    title = "Trigger Suggestion",
                    description = trigger,
                    color = Config.MAINCOLOR
                )
                embed.set_footer(text = f"Suggested by {ctx.author.name}#{ctx.author.discriminator} ID - {ctx.author.id}")
                if ctx.message.attachments != []:
                    embed.set_image(url = ctx.message.attachments[0].url)
                channel = self.bot.get_channel(Config.TRIGGER_SUGGEST_LOG)
                msg = await channel.send(embed = embed)
                await msg.add_reaction("✅")
                await msg.add_reaction("❌")
                embed = discord.Embed(
                    title = "Trigger Suggestion",
                    description = "Your suggestion has been inputted to my developer!",
                    color = Config.MAINCOLOR
                )
                await ctx.send(embed = embed)
                
def setup(bot):
    bot.add_cog(Misc(bot))
