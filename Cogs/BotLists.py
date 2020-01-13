# Imports
import asyncio
import datetime
import discord
from discord.ext import commands
import Config
import motor.motor_asyncio
import random
import aiohttp

class BotLists(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.dbltoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0OTUzNTY5NDE0NTg0NzMwMSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTc1NDIzNDk4fQ.kg2Om9Ec2h46De3BE_wxj8b302bkgLVep2MDSK8_owg"
        self.dblurl = "https://discordbots.org/api/bots/649535694145847301/stats"
        self.dblheaders = {"Authorization" : self.dbltoken}
        self.session = aiohttp.ClientSession(loop = self.bot.loop)

    async def update(self):
          guild_count = len(self.bot.guilds)
          payload = json.dumps({
          'server_count': guild_count
          })

          headers = {
              "authorization": "2ea1f1755b26a7b876a03452e9774d1e0389ff914bc4fdd3132b11cbacf60a9baf6b742362009b0e739bb7630050dc8c7cb5615a667fc72ecab73d0a994ba9d1",
              "content-type": "application/json"
          }

          url = f"https://divinediscordbots.com/bots/{self.bot.user.id}/stats"
          async with self.session.post(url, data = payload, headers = headers) as resp:

    @commands.Cog.listener()
    async def on_ready(self):
        payload = {"server_count": len(self.bot.guilds)}
        async with aiohttp.ClientSession() as aioclient:
                await aioclient.post(self.dblurl, data = payload, headers = self.dblheaders)
        await self.update()

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        payload = {"server_count": len(self.bot.guilds)}
        async with aiohttp.ClientSession() as aioclient:
                await aioclient.post(self.dblurl, data = payload, headers = self.dblheaders)
        await self.update()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        payload = {"server_count": len(self.bot.guilds)}
        async with aiohttp.ClientSession() as aioclient:
                await aioclient.post(self.dblurl, data = payload, headers = self.dblheaders)
        await self.update()

def setup(bot):
    bot.add_cog(BotLists(bot))
