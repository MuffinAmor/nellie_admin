import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import json
import os
import os
import psutil
import time
import aiohttp

from datetime import datetime

client = commands.Bot(command_prefix='nl!')
botcolor = 0x000ffc

aiosession = aiohttp.ClientSession(loop=client.loop)
process = psutil.Process(os.getpid())
memory = process.memory_info().rss / float(2 ** 20)

class info:
    def __init__(self, client):
        self.client = client
        self.launch = datetime.utcnow()
        self.counter = 0
       
    def uptime(self):
        delta_uptime = datetime.utcnow() - self.launch
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        return "{0} Tag/e, {1} Stunde/n, {2} Minute/n, {3} Sekunde/n".format(days, hours, minutes, seconds)

    async def on_message(self, message):
        if message.content.startswith('nl!'):
            self.counter += 1	
        if message.content.startswith('nl!'):
            home = self.client.get_server('382290709249785857')
            channel = discord.utils.get(home.channels, id="569255998838276106", type=discord.ChannelType.voice)
            await self.client.edit_channel(channel, name="Command Counter: %d" % self.counter)
			
        start = time.time()
        async with aiosession.get("https://discordapp.com"):
            duration = time.time() - start
        duration = round(duration * 1000)
        if message.content.startswith('nl!info'):
            servers = list(self.client.servers)
            user = sum(len(s.members) for s in self.client.servers)
            embed = discord.Embed(
                title='Thats are my stats!',
                colour=botcolor
            )
            embed.add_field(name="The Bot is connected on `{0}` servers".format(str(len(servers))), value='** **', inline='False')
            embed.add_field(name="Neko has run `%d` commands since last bot restart and `{0}` users".format(user) % self.counter, value='** **', inline='False')
            embed.add_field(name="`{0.name}` has currently `{0.member_count}` members".format(message.server), value='** **', inline='False')
            embed.add_field(name='Online seit:', value='**{}**'.format(self.uptime()), inline='False')
            embed.add_field(name='Bot version:', value='4.0.0', inline='False')
            embed.add_field(name='CPU:', value="{0}%".format(psutil.cpu_percent()), inline='False')
            embed.add_field(name='CPU Kerne:', value='{0} Kerne'.format(psutil.cpu_count()), inline='False')
            embed.add_field(name='RAM:', value="{0} MB".format(round(memory, 2)), inline='False')
            embed.add_field(name='Python Version:', value='3.6.3', inline='False'),
            embed.add_field(name='Discord.py version:', value=discord.__version__, inline='False')
            embed.set_footer(text='Message was requested by {}'.format(message.author))
            embed.timestamp = datetime.utcnow()
            msg = await self.client.send_message(message.channel, embed=embed)
			
    @client.event
    async def on_server_remove(self, server): 
        servers = list(self.client.servers)
        home = self.client.get_server('382290709249785857')
        member = sum(len(s.members) for s in client.servers if not s.id =='264445053596991498')
        channel1 = discord.utils.get(home.channels, id="569216934663684126", type=discord.ChannelType.voice)
        channel4 = discord.utils.get(home.channels, id="569228100387340297", type=discord.ChannelType.voice)
        await self.client.edit_channel(channel1, name="Totalusers : {}".format(member))
        await self.client.edit_channel(channel4, name="Servers: {}".format(str(len(servers))))
#########################################################################################################################
    @client.event
    async def on_server_join(self, server):
        servers = list(self.client.servers)
        home = self.client.get_server('382290709249785857')
        member = sum(len(s.members) for s in client.servers if not s.id =='264445053596991498')
        channel1 = discord.utils.get(home.channels, id="569216934663684126", type=discord.ChannelType.voice)
        channel4 = discord.utils.get(home.channels, id="569228100387340297", type=discord.ChannelType.voice)
        await self.client.edit_channel(channel1, name="Totalusers : {}".format(member))
        await self.client.edit_channel(channel4, name="Servers: {}".format(str(len(servers))))
#########################################################################################################################
    @client.event
    async def on_member_join(self, member):
        servers = list(self.client.servers)
        home = self.client.get_server('382290709249785857')
        member1 = sum(len(s.members) for s in self.client.servers)
        channel1 = discord.utils.get(home.channels, id="569216934663684126", type=discord.ChannelType.voice)
        channel4 = discord.utils.get(home.channels, id="569228100387340297", type=discord.ChannelType.voice)
        await self.client.edit_channel(channel1, name="Totalusers : {}".format(member1))
        await self.client.edit_channel(channel4, name="Servers: {}".format(str(len(servers))))
#########################################################################################################################
    @client.event
    async def on_member_remove(self, member):
        servers = list(self.client.servers)
        home = self.client.get_server('382290709249785857')
        member1 = sum(len(s.members) for s in self.client.servers)
        channel1 = discord.utils.get(home.channels, id="569216934663684126", type=discord.ChannelType.voice)
        channel4 = discord.utils.get(home.channels, id="569228100387340297", type=discord.ChannelType.voice)
        await self.client.edit_channel(channel1, name="Totalusers : {}".format(member1))
        await self.client.edit_channel(channel4, name="Servers: {}".format(str(len(servers))))

    @client.command(pass_context=True)
    async def statsetup(self, ctx):		
        servers = list(self.client.servers)
        home = self.client.get_server('382290709249785857')
        member = sum(len(s.members) for s in client.servers if not s.id =='264445053596991498')
        channel1 = discord.utils.get(home.channels, id="569216934663684126", type=discord.ChannelType.voice)
        channel4 = discord.utils.get(home.channels, id="569228100387340297", type=discord.ChannelType.voice)
        await self.client.edit_channel(channel1, name="Totalusers : {}".format(member))
        await self.client.edit_channel(channel4, name="Servers: {}".format(str(len(servers))))
def setup(client):
    client.add_cog(info(client))
