import discord
from discord.ext import commands 
import asyncio
import sys
import json
import os
import psutil
import time
import aiohttp
from datetime import datetime

client = commands.Bot(command_prefix='nl!')

botcolor = 0x000ffc

client.remove_command('help')

aiosession = aiohttp.ClientSession(loop=client.loop)
process = psutil.Process(os.getpid())
memory = process.memory_info().rss / float(2 ** 20)

class ping:
    def __init__(self, client):
        self.client = client

        self.launch = datetime.utcnow()

    def uptime(self):
        delta_uptime = datetime.utcnow() - self.launch
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        return "{0} Tag/e, {1} Stunde/n, {2} Minute/n, {3} Sekunde/n".format(days, hours, minutes, seconds)

    @client.command(pass_context=True)
    async def ping(self, ctx):
        start = time.time()
        async with aiosession.get("https://discordapp.com"):
            duration = time.time() - start
        duration = round(duration * 1000)
        embed = discord.Embed(
            title='Reactionstest',
            colour=botcolor
        )
        embed.add_field(name='Pong :ping_pong:', value='{0} ms'.format(duration))
        embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        msg = await self.client.send_message(ctx.message.channel, embed=embed)


def setup(client):
    client.add_cog(ping(client))
