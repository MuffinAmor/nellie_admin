import discord
from discord.ext import commands
import asyncio
from datetime import datetime
from re import match
import json
import os

os.chdir(r'/home/pi/Nellie/commands/data')

if os.path.isfile("serverlog.json"):
    with open('serverlog.json', encoding='utf-8') as f:
        log = json.load(f)
else:
    log = {}
    log['server'] = []
    with open('serverlog.json','w+') as f:
        json.dump(log , f, indent=4)	
	  
	  
botcolor = 0xff0000

client = commands.Bot(command_prefix='nl!')

dev_list = ['474947907913515019']

server_list = ['382290709249785857']

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991"]

    return commands.check(predicate)

class interface:
    def __init__(self, client,):
        self.client = client
########################################################################################################################
    @client.event
    async def on_channel_delete(self, channel):
        with open('serverlog.json', encoding='utf-8') as f:
            log = json.load(f)
            for current_server in log['server']:
                if current_server['id'] == channel.server.id:
                    channel = ' '.join(current_server['channel'])
                    log = discord.utils.get(channel.server.channels, id=channel)
                    embed = discord.Embed(description=' The Channel `{0}` has been deleted.'.format(channel.name), color=botcolor)
                    embed.set_footer(text='This message was requested by Neko')
                    embed.timestamp = datetime.utcnow()
                    await self.client.send_message(log, embed=embed)
#########################################################################################################################
    @client.event
    async def on_channel_create(self, channel):
        with open('serverlog.json', encoding='utf-8') as f:
            log = json.load(f)
            for current_server in log['server']:
                if current_server['id'] == channel.server.id:
                    channel = ' '.join(current_server['channel'])
                    log = discord.utils.get(channel.server.channels, id=channel)
                    embed = discord.Embed(description=' The Channel `{0}` has been created.'.format(channel), color=botcolor)
                    embed.set_footer(text='This message was requested by Neko')
                    embed.timestamp = datetime.utcnow()
                    await self.client.send_message(log, embed=embed)
#########################################################################################################################
    @client.event
    async def on_member_ban(self, user):
        with open('serverlog.json', encoding='utf-8') as f:
            log = json.load(f)
            for current_server in log['server']:
                if current_server['id'] == user.server.id:
                    channel = ' '.join(current_server['channel'])
                    log = discord.utils.get(user.server.channels, id=channel)
                    embed = discord.Embed(description=' The User `{0}` has been banned from the server.'.format(user.name), color=botcolor)
                    embed.set_footer(text='This message was requested by Neko')
                    embed.timestamp = datetime.utcnow()
                    await self.client.send_message(log, embed=embed)
#########################################################################################################################
    @client.event
    async def on_member_unban(self, server, user):
        with open('serverlog.json', encoding='utf-8') as f:
            log = json.load(f)
            for current_server in log['server']:
                if current_server['id'] == user.server.id:
                    channel = ' '.join(current_server['channel'])
                    log = discord.utils.get(user.server.channels, id=channel)
                    embed = discord.Embed(description=' The User `{0}` has been unbanned from the Server `{1}`'.format(user.name, server), color=botcolor)
                    embed.set_footer(text='This message was requested by Neko')
                    embed.timestamp = datetime.utcnow()
                    await self.client.send_message(log, embed=embed)
#########################################################################################################################
    @client.event
    async def on_server_role_create(self, role):
        with open('serverlog.json', encoding='utf-8') as f:
            log = json.load(f)
            for current_server in log['server']:
                if current_server['id'] == role.server.id:
                    channel = ' '.join(current_server['channel'])
                    log = discord.utils.get(role.server.channels, id=channel)
                    embed = discord.Embed(description=' The Role {0} has been created'.format(role.name), color=botcolor)
                    embed.set_footer(text='This message was requested by Neko')
                    embed.timestamp = datetime.utcnow()
                    await self.client.send_message(log, embed=embed)
#########################################################################################################################
    @client.event
    async def on_server_role_delete(self, role):
        with open('serverlog.json', encoding='utf-8') as f:
            log = json.load(f)
            for current_server in log['server']:
                if current_server['id'] == role.server.id:
                    channel = ' '.join(current_server['channel'])
                    log = discord.utils.get(role.server.channels, id=channel)
                    embed = discord.Embed(description=' The Role `{0}` has been deleted'.format(role.name), color=botcolor)
                    embed.set_footer(text='This message was requested by Neko')
                    embed.timestamp = datetime.utcnow()
                    await self.client.send_message(log, embed=embed)
#########################################################################################################################
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def setlog(self, ctx, channel:discord.Channel):
        if not ctx.message.author.bot:
            server_id = ctx.message.server.id
            if channel is None:
                msg = await self.client.say("Please provide a channel")
                await asyncio.sleep(10)
                await self.client.delete_message(msg)
                return
            on = discord.utils.get(ctx.message.server.channels, name=channel.name)
            if on in ctx.message.server.channels:
                for current_server in log['server']:
                    if current_server['id'] == server_id:
                        current_server['channel'].clear()
                        current_server['enable'].clear()
                        current_server['channel'].append(channel)
                        current_server['enable'].append('True')
                        break
                else:
                    log['server'].append({
                    'id':server_id,
                    'channel': [on.id], 
                    'enable': 'True',
                    })
                with open('serverlog.json','w+') as f:
                    json.dump(log,f, indent=4)
                    msg = await self.client.say("The log has been set to: {}".format(channel))
                    await asyncio.sleep(10)
                    await self.client.delete_message(msg)
            else:
                msg = await self.client.say("This channel is not found. Please choose a vaild channel")
                await asyncio.sleep(60)
                await self.client.delete_message(msg)
########################################################################################################################				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def disablelogchannel(self, ctx):
        if not ctx.message.author.bot:	
            server_id = ctx.message.server.id
            for current_server in log['server']:
                if current_server['id'] == server_id:
                    current_server['channel'].clear()
                    current_server['channel'].append("None")
                    current_server['enable'].clear()
                    current_server['enable'].append('None')
                    break
            with open('serverlog.json','w+') as f:
                json.dump(log,f,indent=4)
                msg = await self.client.say("The serverlog has been reseted.\nFor reactivation type nl!setlog *channelname*")
                await asyncio.sleep(60)
                await self.client.delete_message(msg)

    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def loginfo(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.message.server 
            with open('serverlog.json', encoding='utf-8') as f:
                log = json.load(f)
                for current_server in log['server']:
                    if current_server['id'] == server.id:
                        channel_id = ' '.current_server['channel']
                        log = discord.utils.get(server.channels, name=channel2)
                        embed=discord.Embed(
                            color=ctx.message.author.top_role.color)
                        embed.add_field(name='Logchannel Info', value='** **', inline=False)
                        embed.add_field(name='Server', value=server.name, inline=True)
                        embed.add_field(name='LogChannel', value=log, inline=False)
                        embed.add_field(name='Info:', value="The Log safe server activities like\nRole Delete or Role create\nMember Ban or Member unban\nChannel create or Channel delete\nand write it in the Logchannel.", inline=False)
                        embed.set_thumbnail(url=server.icon_url)
                        embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(120)
                        await self.client.delete_message(msg1)
                        break
                else:
                        embed=discord.Embed(
                            color=ctx.message.author.top_role.color)
                        embed.add_field(name='Logchannel Info', value='** **', inline=False)
                        embed.add_field(name='Server', value=server.name, inline=True)
                        embed.add_field(name='LogChannel', value="None", inline=False)
                        embed.add_field(name='Info:', value="The Log safe server activities like\nRole Delete or Role create\nMember Ban or Member unban\nChannel create or Channel delete\nand write it in the Logchannel.", inline=False)
                        embed.set_thumbnail(url=server.icon_url)
                        embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                        await asyncio.sleep(120)
                        await self.client.delete_message(msg1)
########################################################################################################################				
    @client.command(pass_context = True)
    @is_vale()
    @commands.cooldown(3, 60, commands.BucketType.server)
    async def resetlogdata(self, ctx):		
        with open('serverlog.json', encoding='utf-8') as f:	
            log = {}
            log['server'] = []
        with open('serverlog.json','w+') as f:
            json.dump(log,f,indent=4)


def setup(client):
    client.add_cog(interface(client))