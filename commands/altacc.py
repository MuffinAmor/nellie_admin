import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import os
import json
os.chdir(r'/home/pi/Nellie/commands/data')

if os.path.isfile("altacc.json"):
    with open('altacc.json', encoding='utf-8') as f:
        altacc = json.load(f)
else:
    altacc = {}
    altacc['altaccscan'] = []
    with open('altacc.json','w+') as f:
        json.dump(altacc , f, indent=4)	

client = commands.Bot(command_prefix='nl!')

botcolor = 0xffffff

client.remove_command('help')

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991", "406479076048633857"]

    return commands.check(predicate)
	
class alt:
    def __init__(self, client):
        self.client = client

    @client.command(pass_context = True)
    @is_vale()    
    async def setaltscan(self, ctx, channel:discord.Channel, *days:str):
        if not ctx.message.author.bot:
            server = ctx.message.server
            active = 'True'
            days = ' '.join(days)
            if not channel:
                msg = await self.client.say("Please provide a channel for the Log")
                return
            if not days:
                msg = await self.client.say("Please provide a numbers for the scanner")
                return
            for numbers in altacc['altaccscan']:
                if numbers['id'] == server.id:
                    numbers['days'].clear()
                    numbers['enable'].clear()
                    numbers['channelid'].clear()
                    numbers['days'].append(days)
                    numbers['enable'].append(active)
                    numbers['channelid'].append(channel.id)
                    break
            else:
                altacc['altaccscan'].append({
                'name':server.name,
                'id':server.id,
                'enable': [active],
                'days': [days],
                'channelid': [channel.id]
                })
            with open('altacc.json','w+') as f:
                json.dump(altacc, f , indent=4)
                msg = await self.client.say("The Scanner has been setted to {0} days in the {1} channel".format(days, channel.name))
                for numbers in altacc['altaccscan']:
                    if numbers['id'] == server.id:
                        num = ' '.join(numbers['days'])
                        days = int(num)
                        for user in ctx.message.server.members:
                            user_days = (ctx.message.timestamp - user.created_at).days
                            if days >= user_days:
                                user_passed1 = (ctx.message.timestamp - user.joined_at).days
                                user_created1 = (ctx.message.timestamp - user.created_at).days
                                channelid = ' '.join(numbers['channelid'])
                                channel = discord.utils.get(ctx.message.server.channels, id=channelid, type=discord.ChannelType.text)
                                embed = discord.Embed(title="{}'s info".format(user.name), description="Alt account in your Rightlines get detected", color=user.top_role.color)
                                embed.add_field(name="Name", value="{0}|{1}".format(user.name, user.mention), inline=True)
                                embed.add_field(name="ID", value=user.id, inline=True)
                                embed.add_field(name="Discriminator", value="#{0}".format(user.discriminator), inline=True)
                                embed.add_field(name="Joined at:", value=("{} ({} days ago!)".format(user.joined_at.strftime("%d %b %Y %H:%M"), user_passed1)), inline=False)
                                embed.add_field(name="Created at:", value=("{} ({} days ago!)".format(user.created_at.strftime("%d %b %Y %H:%M"), user_created1)), inline=False)
                                embed.set_thumbnail(url=user.avatar_url)
                                msg = await self.client.send_message(channel, embed=embed)
                        else:
                            pass

    @client.command(pass_context = True)
    @is_vale()
    async def enablescanner(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.message.server
            active = 'True'
            for numbers in altacc['altaccscan']:
                if numbers['id'] == server.id:
                    numbers['enable'].clear()
                    numbers['enable'].append(active)
                    break
            with open('altacc.json','w+') as f:
                json.dump(altacc,f, indent=4)
                msg = await self.client.say("The Scanner has been setted to online")
				
    @client.command(pass_context = True)
    @is_vale()
    async def disablescanner(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.message.server
            active = 'False'
            for numbers in altacc['altaccscan']:
                if numbers['id'] == server.id:
                    numbers['enable'].clear()
                    numbers['enable'].append(active)
                    break
            with open('altacc.json','w+') as f:
                json.dump(altacc,f, indent=4)
                msg = await self.client.say("The Scanner has been setted to offline")
				
    @client.command(pass_context = True)
    @is_vale()
    async def scannerinfo(self, ctx):
        if not ctx.message.author.bot:   
            server = ctx.message.server
            for numbers in altacc['altaccscan']:
                if numbers['id'] == server.id:
                    days = ''.join(numbers['days'])
                    enable = ' '.join(numbers['enable'])
                    channelid = ' '.join(numbers['channelid'])
                    channel = discord.utils.get(ctx.message.server.channels, id=channelid, type=discord.ChannelType.text)
                    if enable == "False":
                        embed=discord.Embed(
                            color=ctx.message.author.top_role.color)
                        embed.add_field(name='Altaccountscannerinfo', value='** **', inline=False)
                        embed.add_field(name='Server', value=server.name, inline=True)
                        embed.add_field(name='Scanner Online?', value=enable, inline=True)
                        embed.add_field(name='Days since account created', value="None", inline=False)
                        embed.add_field(name='Logchannel', value="None", inline=False)
                        embed.set_thumbnail(url=server.icon_url)
                        embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                        return
                    else:
                        embed=discord.Embed(
                            color=ctx.message.author.top_role.color)
                        embed.add_field(name='Altaccountscannerinfo', value='** **', inline=False)
                        embed.add_field(name='Server', value=server.name, inline=True)
                        embed.add_field(name='Scanner Online?', value=enable, inline=True)
                        embed.add_field(name='Days since account created', value=days, inline=False)
                        embed.add_field(name='Logchannel', value=channel.name, inline=False)
                        embed.set_thumbnail(url=server.icon_url)
                        embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                        return
            else:
                embed=discord.Embed(
                    color=ctx.message.author.top_role.color)
                embed.add_field(name='Altaccountscannerinfo', value='** **', inline=False)
                embed.add_field(name='Server', value=server.name, inline=True)
                embed.add_field(name='Scanner Online?', value="False", inline=True)
                embed.add_field(name='Days since acc created', value="None", inline=False)
                embed.add_field(name='LogChannel', value="None", inline=False)
                embed.set_thumbnail(url=server.icon_url)
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                return
         
    @client.event
    async def on_member_join(self, member):
        if not member.id == "533372604350988299":
            for numbers in altacc['altaccscan']:
                if numbers['id'] == member.server.id:
                    num = ' '.join(numbers['days'])
                    days = int(num)
                    member_days = (datetime.now() - member.created_at).days
                    if days >= member_days:
                        member_passed1 = (datetime.now() - member.joined_at).days
                        member_created1 = (datetime.now() - member.created_at).days
                        channelid = ' '.join(numbers['channelid'])
                        channel = discord.utils.get(member.server.channels, id=channelid)
                        embed = discord.Embed(title="{}'s info".format(member.name), description="Alt account in your Rightlines get detected", color=member.top_role.color)
                        embed.add_field(name="Name", value="{0}|{1}".format(member.name, member.mention), inline=True)
                        embed.add_field(name="ID", value=member.id, inline=True)
                        embed.add_field(name="Discriminator", value="#{0}".format(member.discriminator), inline=True)
                        embed.add_field(name="Joined at:", value=("{} ({} days ago!)".format(member.joined_at.strftime("%d %b %Y %H:%M"), member_passed1)), inline=False)
                        embed.add_field(name="Created at:", value=("{} ({} days ago!)".format(member.created_at.strftime("%d %b %Y %H:%M"), member_created1)), inline=False)
                        embed.set_thumbnail(url=member.avatar_url)
                        msg = await self.client.send_message(channel, embed=embed)
                        break

				
				
    @client.command(pass_context = True)
    @is_vale()
    async def check(self, ctx):
        if not ctx.message.author.bot: 
                server = ctx.message.server		
                for numbers in altacc['altaccscan']:
                    if numbers['id'] == server.id:
                        num = ' '.join(numbers['days'])
                        days = int(num)
                        for user in ctx.message.server.members:
                            user_days = (ctx.message.timestamp - user.created_at).days
                            if days >= user_days:
                                user_passed1 = (ctx.message.timestamp - user.joined_at).days
                                user_created1 = (ctx.message.timestamp - user.created_at).days
                                channelid = ' '.join(numbers['channelid'])
                                channel = discord.utils.get(ctx.message.server.channels, id=channelid, type=discord.ChannelType.text)
                                embed = discord.Embed(title="{}'s info".format(user.name), description="Alt account in your Rightlines get detected", color=user.top_role.color)
                                embed.add_field(name="Name", value="{0}|{1}".format(user.name, user.mention), inline=True)
                                embed.add_field(name="ID", value=user.id, inline=True)
                                embed.add_field(name="Discriminator", value="#{0}".format(user.discriminator), inline=True)
                                embed.add_field(name="Joined at:", value=("{} ({} days ago!)".format(user.joined_at.strftime("%d %b %Y %H:%M"), user_passed1)), inline=False)
                                embed.add_field(name="Created at:", value=("{} ({} days ago!)".format(user.created_at.strftime("%d %b %Y %H:%M"), user_created1)), inline=False)
                                embed.set_thumbnail(url=user.avatar_url)
                                msg = await self.client.send_message(ctx.message.channel, embed=embed)
                        else:
                            pass				
				
				
				
				
				
				
def setup(client):
    client.add_cog(alt(client))