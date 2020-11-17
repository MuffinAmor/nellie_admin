import discord
from discord.ext import commands
import asyncio
import sys
import random
from discord.ext.commands import CommandNotFound
import datetime

client = commands.Bot(command_prefix='nl!')

botcolor = 0xff0096

dev_list = ['474947907913515019']

client.remove_command('help')

class serverowner:
    def __init__(self, client):
        self.client = client
		

    @client.command(pass_context=True)
    async def lockeveryone(self, ctx):
        if not ctx.message.author.bot: 
            if ctx.message.author is ctx.message.server.owner:	 		
                role = discord.utils.get(ctx.message.server.roles, name="@everyone")
                perms = discord.Permissions(0) 
                await self.client.send_typing(ctx.message.channel)
                await self.client.edit_role(ctx.message.server, role, permissions=perms)
                await self.client.say('{0} has been remove all permissions for @everyone'.format(ctx.message.author.mention))
            elif ctx.message.author.id in dev_list:	 	
                role = discord.utils.get(ctx.message.server.roles, name="@everyone")
                perms = discord.Permissions(0) 
                await self.client.send_typing(ctx.message.channel)
                await self.client.edit_role(ctx.message.server, role, permissions=perms)
                await self.client.say('{0} has been remove all permissions for @everyone'.format(ctx.message.author.mention))
            else:
                msg = await self.client.send_message(ctx.message.channel, "You need the Owner Crown to do that")
######################################################################################################################## 	
    @client.command(pass_context=True)
    async def banlist(self, ctx): 
        if not ctx.message.author.bot: 
            if ctx.message.author is ctx.message.server.owner:	 	
                bannedUsers = await self.client.get_bans(ctx.message.server)
                for user in bannedUsers:
                    await self.client.send_message(ctx.message.channel, user.name + '\n' + user.id)
            elif ctx.message.author.id in dev_list:	 	
                bannedUsers = await self.client.get_bans(ctx.message.server)
                for user in bannedUsers:
                    await self.client.send_message(ctx.message.channel, user.name + '\n' + user.id)
            else:
                msg = await self.client.send_message(ctx.message.channel, "You need the Owner Crown to do that")
######################################################################################################################## 				
    @client.event	
    async def on_message(self, message):
        if not message.author.bot:
            if message.content.startswith ("nl!setverfilevel"):
                if "None" in message.content:
                    if message.author is message.server.owner:	 	
                        verfi = discord.VerificationLevel(0)
                        await self.client.edit_server(message.server, verification_level=verfi)
                        msg = await self.client.send_message(message.channel, "The Verification Level has been set to `None` ")
                    if not message.author is message.server.owner:	 	
                        msg = await self.client.send_message(message.channel, "You need the Owner Crown to do that")
                if "Low" in message.content:
                    if message.author is message.server.owner:
                        verfi = discord.VerificationLevel(1)
                        await self.client.edit_server(message.server, verification_level=verfi)
                        msg = await self.client.send_message(message.channel, "The Verification Level has been set to `Low` ")
                    if not message.author is message.server.owner:
                        msg = await self.client.send_message(message.channel, "You need the Owner Crown to do that")
                if "Medium" in message.content:
                    if message.author is message.server.owner:
                        verfi = discord.VerificationLevel(2)
                        await self.client.edit_server(message.server, verification_level=verfi)
                        msg = await self.client.send_message(message.channel, "The Verification Level has been set to `Medium` ")
                    if not message.author is message.server.owner:
                        msg = await self.client.send_message(message.channel, "You need the Owner Crown to do that")
                if "High" in message.content:
                    if message.author is message.server.owner:
                        verfi = discord.VerificationLevel(3)
                        await self.client.edit_server(message.server, verification_level=verfi)
                        msg = await self.client.send_message(message.channel, "The Verification Level has been set to `High` ")
                    if not message.author is message.server.owner:	
                        msg = await self.client.send_message(message.channel, "You need the Owner Crown to do that")
                else:
                    msg = await self.client.say("Oooooops, thats not a Verification Level")
######################################################################################################################## 					
    @client.command(pass_context=True)
    async def changeservername(self, ctx, *name):
        if not ctx.message.author.bot:
            if ctx.message.author is ctx.message.server.owner:	
                if name:
                    msg = ' '.join(name)
                    await self.client.edit_server(ctx.message.server, name=msg)
                    msg = await self.client.say("The server has been changed to {0}".format(msg))
                if not name: 
                    msg = await self.client.say("Please provide a Server name")
            elif ctx.message.author.id in dev_list:
                if name:
                    msg = ' '.join(name)
                    await self.client.edit_server(ctx.message.server, name=msg)
                    msg = await self.client.say("The server has been changed to {0}".format(msg))
                if not name: 
                    message = await self.client.say("Please provide a Server name")
            else:	
                msg = await self.client.send_message(ctx.message.channel, "You need the Owner Crown to do that")
######################################################################################################################## 				
    @client.command(pass_context=True)
    async def rrp(self, ctx, role:discord.Role):
        if not ctx.message.author.bot:
            if ctx.message.author is ctx.message.server.owner:	
                if role is None:
                    msg = await self.client.say("Please tag a role")
                else:
                    perms = discord.Permissions(0)
                    await self.client.edit_role(ctx.message.server, role, permissions=perms) 
                    msg = await self.client.say('{0} has been remove all permissions for {1}'.format(ctx.message.author.mention, role))
            elif ctx.message.author.id in dev_list:
                if role is None:
                    msg = await self.client.say("Please tag a role")
                else:
                    perms = discord.Permissions(0)
                    await self.client.edit_role(ctx.message.server, role, permissions=perms) 
                    msg = await self.client.say('{0} has been remove all permissions for {1}'.format(ctx.message.author.mention, role))
            else:
                msg = await self.client.send_message(ctx.message.channel, "You need the Owner Crown to do that")
######################################################################################################################## 						
    @client.command(pass_context=True)
    async def giveserverrole(self, ctx, role:discord.Role):	
        if not ctx.message.author.bot: 
            if ctx.message.author is ctx.message.server.owner:	 	
                if role is None:
                    msg = await self.client.say("You need to choose a role, buddy!")
                else:
                    for member in ctx.message.server.members:
                        await self.client.add_roles(member, role)
                    msg = await self.client.say("The Role {0} has been added to all Server Members".format(role.name))
            elif ctx.message.author.id in dev_list:
                if role is None:
                    msg = await self.client.say("You need to choose a role, buddy!")
                else:
                    for member in ctx.message.server.members:
                        await self.client.add_roles(member, role)
                    msg = await self.client.say("The Role {0} has been added to all Server Members".format(role.name))
            else:
                msg = await self.client.send_message(ctx.message.channel, "You need the Owner Crown to do that")
########################################################################################################################				
    @client.command(pass_context=True)
    async def removeserverrole(self, ctx, role:discord.Role):	
        if not ctx.message.author.bot: 
            if ctx.message.author is ctx.message.server.owner:	 	
                if role is None:
                    msg = await self.client.say("You need to choose a role, buddy!")
                else:
                    for member in ctx.message.server.members:
                        await self.client.remove_roles(member, role)
                    msg = await self.client.say("The Role {0} has been removeed to all Server Members".format(role.name))
            elif ctx.message.author.id in dev_list:
                if role is None:
                    msg = await self.client.say("You need to choose a role, buddy!")
                else:
                    for member in ctx.message.server.members:
                        await self.client.remove_roles(member, role)
                    msg = await self.client.say("The Role {0} has been removeed to all Server Members".format(role.name))
            else:
                msg = await self.client.send_message(ctx.message.channel, "You need the Owner Crown to do that")
			
        
def setup(client):
    client.add_cog(serverowner(client))
			
			
			
        
			
