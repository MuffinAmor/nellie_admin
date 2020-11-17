import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import random
import aiohttp


client = commands.Bot(command_prefix='ng!')

botcolor = 0x00ffff

pass_list = ['552926171537473536', '511531519530106880', '382290709249785857']

class auto:
    def __init__(self, client,):
        self.client = client
########################################################################################################################
    @client.event
    async def on_command_error(self, error, ctx): 
        if isinstance(error, commands.CommandNotFound):
            return
        if not ctx.message.author.server.id == "264445053596991498":
            if message.content.startswith('nl!tenor'):
                return
            if message.content.startswith('nl!hug'):
                return
            if message.content.startswith('nl!pat'):
                return
            if isinstance(error, commands.CommandNotFound):
                choice = random.randint(1, 3)
                if choice == 1:
                    embed = discord.Embed(
                        description='Which Command is this? :eyes: Do you want to open my help menu?',
                        colour=botcolor
                    )
                    msg = await self.client.send_message(ctx.message.channel, embed=embed)
                    await self.client.add_reaction(msg, "✅")
                    await self.client.add_reaction(msg, "❎")
                if choice == 2:
                    embed = discord.Embed(
                        description='Thats sound not like one of my Commands. Do you need help from the help menu?',
                        colour=botcolor
                    )
                    msg = await self.client.send_message(ctx.message.channel, embed=embed)
                    await self.client.add_reaction(msg, "✅")
                    await self.client.add_reaction(msg, "❎")
                if choice == 3:
                    embed = discord.Embed(
                        description='All what you need is help. Do you want my help?',
                        colour=botcolor
                    )
                    msg = await self.client.send_message(ctx.message.channel, embed=embed)
                    await self.client.add_reaction(msg, "✅")
                    await self.client.add_reaction(msg, "❎")
            if isinstance(error, commands.BadArgument):
                msg = await self.client.send_message(ctx.message.channel, "Invalid input, bro")
            if isinstance(error, commands.MissingRequiredArgument):
                msg = await self.client.send_message(ctx.message.channel, error)
######################################################################################################################## 	 
    @client.event
    async def on_message(self, message):
        if message.content.startswith('nl!say'):
            await self.client.delete_message(message)
        if message.content.startswith('nl!whisper'):
            await self.client.delete_message(message)
#########################################################################################################################
    @client.event
    async def on_server_remove(self, server):
        embed = discord.Embed(description=' Neko has been leaved the server *{0}*'.format(server), color=botcolor)
        embed.set_footer(text='This message was requested by Neko')
        embed.timestamp = datetime.utcnow()
        server1 = self.client.get_server('575378478573289472')
        channel = discord.utils.get(server1.channels, name="neko_server_log", type=discord.ChannelType.text)
        await self.client.send_message(channel, embed=embed)
        headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUzMzM3MjYwNDM1MDk4ODI5OSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTU5OTQ1NDk1fQ.bwri27GtxFBId6K5YE7GzxdnTH_TUb2aEAQrmrJ-3f8"}
        payload = {"server_count"  : len(self.client.servers)}
        async with aiohttp.ClientSession() as aioclient:
            await self.aioclient.post('https://discordbots.org/api/bots/533372604350988299/stats', data=payload, headers=headers)
#########################################################################################################################
    @client.event
    async def on_server_join(self, server):
        embed = discord.Embed(description=' Neko has been joined the server *{0}*'.format(server), color=botcolor)
        embed.set_footer(text='This message was requested by Neko')
        embed.timestamp = datetime.utcnow()
        server1 = self.client.get_server('575378478573289472')
        channel = discord.utils.get(server1.channels, name="neko_server_log", type=discord.ChannelType.text)
        server_info1 = (embed.timestamp - server.created_at).days
        Bot = list(member.bot for member in server.members if member.bot is True) 
        user = list(member.bot for member in server.members if member.bot is False)
        embed=discord.Embed(
            color=botcolor)
        embed.add_field(name='<:Neko_Logo:549531102117625866>__Server Join__<:Neko_Logo:549531102117625866>', value='** **', inline=False)
        embed.add_field(name='Name:', value='{}'.format(server.name), inline=True)
        embed.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
        embed.add_field(name='Region:', value='{}'.format(server.region), inline=True)
        embed.add_field(name='Membercount:', value='{} members'.format(server.member_count), inline=True)
        embed.add_field(name='Botcount:', value='{} Bots'.format(str(len(Bot))), inline=True) 
        embed.add_field(name='Humancount:', value='{} users'.format(str(len(user))), inline=True)
        embed.add_field(name='Large Server:', value='{} (250+ member)'.format(server.large), inline=True)
        embed.add_field(name='Serverowner:', value='{}'.format(server.owner), inline=True)
        embed.add_field(name='Verifylevel:', value='{} '.format(server.verification_level), inline=True)
        embed.add_field(name='Created at:', value='{}'.format("{} ({} days ago!)".format(server.created_at.strftime("%d. %b. %Y %H:%M"), server_info1)), inline=  False)
        embed.set_thumbnail(url="{0}".format(server.icon_url))
        embed.set_footer(text='New Serverjoin', icon_url=server.icon_url)
        embed.timestamp = datetime.utcnow()
        await self.client.send_message(channel, embed=embed)
        headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUzMzM3MjYwNDM1MDk4ODI5OSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTU5OTQ1NDk1fQ.bwri27GtxFBId6K5YE7GzxdnTH_TUb2aEAQrmrJ-3f8"}
        payload = {"server_count"  : len(self.client.servers)}
        async with aiohttp.ClientSession() as aioclient:
            await self.aioclient.post('https://discordbots.org/api/bots/533372604350988299/stats', data=payload, headers=headers)
#########################################################################################################################

 
def setup(client):
    client.add_cog(auto(client))