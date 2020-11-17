import discord
from discord.ext import commands
import asyncio
import sys
from datetime import datetime
import json
import os

os.chdir(r'/home/pi/Nellie/commands/data')

if os.path.isfile("joinrole.json"):
    with open('joinrole.json', encoding='utf-8') as f:
        onjoin = json.load(f)
else:
    onjoin = {}
    onjoin['server'] = []
    with open('joinrole.json', 'w') as f:
        json.dump(onjoin, f, indent=4)

if os.path.isfile("muterole.json"):
    with open('muterole.json', encoding='utf-8') as a:
        mute = json.load(a)
else:
    mute = {}
    mute['clients'] = []
    with open('muterole.json', 'w') as a:
        json.dump(mute, a, indent=4)    


client = commands.Bot(command_prefix='nl!')	
	
botcolor = 0x000ffc

client.remove_command('help')

pass_list = ['547124033460564116', '526546384372605231', '511531519530606880', '533372604350988299']

dev_list = ['474947907913515019', '486988989262462991']

disable_list = ['00000000000000000']

class admin:
    def __init__(self, client):
        self.client = client
		
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def setmuterole(self, ctx, role:discord.Role):
        if not ctx.message.author.bot:
            server = ctx.message.server
            if role is None:
                msg = await self.client.say("Please provide a Role")
                await asyncio.sleep(30)
                await self.client.delete_message(msg)
                return
            for current_word in mute['clients']:
                if current_word['id'] == server.id:
                    current_word['role'].clear()
                    current_word['role'].append(str(role.id))
                    break
            else:
                mute['clients'].append({
                'id':server.id,
                'role': [str(role.id)],
                })
            with open('muterole.json','w+') as f:
                json.dump(mute,f, indent=4)
                msg = await self.client.say("The Role {} has been setted as your Muterole".format(role.name))
########################################################################################################################
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, ammount = 50):
        if not ctx.message.author.bot:
                channel = ctx.message.channel
                ammount = int(ammount) + 1
                mgs = []
                async for x in self.client.logs_from(channel, limit = ammount):
                    mgs.append(x)
                await self.client.delete_messages(mgs)
                embed0 = discord.Embed(title='The chat is clear. This message disapears in 10', color=botcolor)
                embed1 = discord.Embed(title='The chat is clear. This message disapears in 9', color=botcolor)
                embed2 = discord.Embed(title='The chat is clear. This message disapears in 8', color=botcolor)
                embed3 = discord.Embed(title='The chat is clear. This message disapears in 7', color=botcolor)
                embed4 = discord.Embed(title='The chat is clear. This message disapears in 6', color=botcolor)
                embed5 = discord.Embed(title='The chat is clear. This message disapears in 5', color=botcolor)
                embed6 = discord.Embed(title='The chat is clear. This message disapears in 4', color=botcolor)
                embed7 = discord.Embed(title='The chat is clear. This message disapears in 3', color=botcolor)
                embed8 = discord.Embed(title='The chat is clear. This message disapears in 2', color=botcolor)
                embed9 = discord.Embed(title='The chat is clear. This message disapears in 1', color=botcolor)
                hack = await self.client.send_message(channel, embed=embed0)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed1)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed2)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed3)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed4)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed5)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed6)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed7)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed8)
                await asyncio.sleep(1)
                await self.client.edit_message(hack, embed=embed9)
                await asyncio.sleep(1)
                await self.client.delete_message(hack)
########################################################################################################################
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member):
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= member.top_role.position:
                        msg2 = await self.client.say("You can only kick a user that is under you in the Role Hierachy")
            else:
                if member.id == "474947907913515019":
                    pass
                if member is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                else:
                    await self.client.kick(member)
                    msg1 = await self.client.say("{0} has been kicked from the Server".format(member.mention))
#########################################################################################################################    
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx,  member: discord.Member=None):
        server = ctx.message.server
        if not ctx.message.author.bot:		
            if ctx.message.author.top_role.position <= member.top_role.position:
                        msg2 = await self.client.say("You can only unmute a user that is under you in the Role Hierachy")
                        
                        
            else:
                if member.id == "474947907913515019":
                    pass
                if member is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    for current_word in mute['clients']:
                        if current_word['id'] == server.id:
                            role=' '.join(current_word['role'])
                            muterole = discord.utils.get(ctx.message.server.roles, id=role)
                            if muterole in member.roles:
                                await self.client.remove_roles(member, muterole)
                                msg = await self.client.say("{0} has been unmuted".format(member.mention))
                                
                                await self.client.delete_message(msg)
                                break
                            else:
                                msg = await self.client.say("{0} is not muted.".format(member.name))
                                
                                await self.client.delete_message(msg)
                                break
                
########################################################################################################################
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def softban(self, ctx, member: discord.Member, days: int = 7, time: int=600):
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= member.top_role.position:
                        msg2 = await self.client.say("You can only softban a user that is under you in the Role Hierachy")
                        
                        
            else:
                if member.id == "474947907913515019":
                    pass
                if member is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    invitelinknew = await self.client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 1)
                    msg1 = await self.client.say('{0} was softbanned for {1} seconds.'.format(Member, time))
                    await self.client.send_message(member, "You are softbanned for {0} seconds. {1}".format(time, invitelinknew))
                    await self.client.ban(member, days)
                    await asyncio.sleep(time)
                    await self.client.unban(ctx.message.server, member)
                    
                    
########################################################################################################################  			
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def tempmute(self, ctx,  member: discord.Member, time=60):
        server = ctx.message.server
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= member.top_role.position:
                        msg2 = await self.client.say("You can only mute a user that is under you in the Role Hierachy")
                        
                        
            else:
                if member.id == "474947907913515019":
                    pass
                if member is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                    
                    await self.client.delete_message(msg)
                if member.server_permissions.administrator ==True:
                    msg = await self.client.say("Users with administrator permissions can´t be muted")
                else:
                    for current_word in mute['clients']:
                        if current_word['id'] == server.id:
                            role=' '.join(current_word['role'])
                            muterole = discord.utils.get(ctx.message.server.roles, id=role)
                            if not muterole in member.roles:
                                await self.client.add_roles(member, muterole)
                                msg = await self.client.say("{0} has been muted for {1} seconds".format(member.mention, time))
                                break
                            else:
                                msg = await self.client.say("{0} is allready muted.".format(member.name))
                                break
                    time = int(time) - 60
                    await asyncio.sleep(time)
                    for current_word in mute['clients']:
                        if current_word['id'] == server.id:
                            role=' '.join(current_word['role'])
                            muterole = discord.utils.get(ctx.message.server.roles, id=role)
                            if muterole in member.roles:
                                await self.client.remove_roles(member, muterole)
                                msg1 = await self.client.say("{0} has been unmuted".format(member.mention))
                                
                                
                                break
                            else:
                                msg = await self.client.say("{0} is not muted.".format(member.name))
                                break
                    
########################################################################################################################  
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx,  member: discord.Member):
        server = ctx.message.server
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= member.top_role.position:
                        msg2 = await self.client.say("You can only mute a user that is under you in the Role Hierachy")
                        
                        
            else:
                if member.id == "474947907913515019":
                    pass
                if member is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                    
                    await self.client.delete_message(msg)
                if member.server_permissions.administrator ==True:
                    msg = await self.client.say("Users with administrator permissions can´t be muted")
                    
                    await self.client.delete_message(msg)
                else:
                    for current_word in mute['clients']:
                        if current_word['id'] == server.id:
                            role=' '.join(current_word['role'])
                            muterole = discord.utils.get(ctx.message.server.roles, id=role)
                            if not muterole in member.roles:
                                await self.client.add_roles(member, muterole)
                                msg = await self.client.say("{0} has been muted".format(member.mention))
                                
                                await self.client.delete_message(msg)
                                break
                            else:
                                msg = await self.client.say("{0} is allready muted.".format(member.name))
                                
                                await self.client.delete_message(msg)
                                break
########################################################################################################################
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def delrole(self, ctx, role: discord.Role):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if ctx.message.author.top_role.position <= role.position:
                        msg2 = await self.client.say("Ops. Don´t break the Role system bud.\nYou can only delete a role that is not higher than your current highest role.")
                        
                        
            else:						
                if role is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    await self.client.delete_role(role.server, role)
                    msg1 = await self.client.say("The role {0} has been deleted!".format(role.name))
                    
                    
########################################################################################################################
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, days: int = 1):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= member.top_role.position:
                        msg2 = await self.client.say("Ops. Don´t break the Role system bud.\nYou can only ban a user with a role that is not higher than your current highest role.")
                        
                        
            else:
                if member.id == "474947907913515019":
                    pass
                if member is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    await self.client.ban(member, days)
                    msg1 = await self.client.say('**{0}** has been banned.'.format(member))
                    
                    
########################################################################################################################
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def give(self, ctx, role: discord.Role, member: discord.Member=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if ctx.message.author.id in dev_list:		
                if role is None:
                    msg = await self.client.say("You need to tag a role, buddy!")
                else:
                    member = member or ctx.message.author
                    await self.client.add_roles(member, role)
                    msg1 = await self.client.say("Role has been added")
                    
                    
            else:
                if role is None:
                    msg = await self.client.say("You need to tag a role, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    member = member or ctx.message.author
                    if ctx.message.author.top_role.position <= role.position:
                        msg2 = await self.client.say("Ops. Don´t break the Role system bud.\nYou can only add a role that is not higher than your current highest role.")
                        
                        
                    else:
                        await self.client.add_roles(member, role)
                        msg1 = await self.client.say("Role has been added")
                        
                        
########################################################################################################################
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def write_white(self, ctx, role: discord.Role, member: discord.Member=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= role.position:
                msg2 = await self.client.say("Ops. Don´t break the Role system bud.\nYou can only remove a role that is not higher than your current highest role.")
                
                
            else:
                if member.id == "474947907913515019":
                    pass
                if member is None:
                    msg = await self.client.say("You need to tag someone, buddy!")
                    
                    await self.client.delete_message(msg)
                elif role is None:
                    msg = await self.client.say("You need to tag a role, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    member = member or ctx.message.author
                    await self.client.remove_roles(member, role)
                    msg1 = await self.client.say("Role has been removed")
                    
                    
########################################################################################################################			
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def createrole(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            mesg = ' '.join(args)
            server = (ctx.message.server)
            Hellblau = discord.Color(0x00caff)
            Member = discord.Permissions(87370817)
            await self.client.create_role(ctx.message.server, name=mesg, permissions=Member, colour=Hellblau)
            msg = await self.client.say("Role has been created")
            
            await self.client.delete_message(msg)
########################################################################################################################     
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def customadmin(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            mesg = ' '.join(args)
            server = (ctx.message.server)
            Hellblau = discord.Color(0x00caff)
            Admin = discord.Permissions(8)
            await self.client.create_role(ctx.message.server, name=mesg, permissions=Admin, colour=Hellblau)
            msg = await self.client.say("Role has been created")
            
            await self.client.delete_message(msg)
########################################################################################################################	  
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def voicekick(self, ctx, user:discord.User):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if user.id == "474947907913515019":
                    pass
            if user is None:
                msg = await self.client.say("You need to tag someone, buddy!")
                
                await self.client.delete_message(msg)
            else:
                kick_channel = await self.client.create_channel(ctx.message.server, "kick", type=discord.ChannelType.voice)
                await self.client.move_member(user,kick_channel)
                await self.client.delete_channel(kick_channel)
                msg = await self.client.say("User has been kicked successfully from the Voicechat")
                
                await self.client.delete_message(msg)
######################################################################################################################## 
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def rolemsg(self, ctx, role: discord.Role, *, message):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if role is None:
                msg = await self.client.say("You need to tag a role, buddy!")
                
                await self.client.delete_message(msg)
            else:
                for member in ctx.message.server.members:
                    await self.client.send_message(member, message)
                    msg = await self.client.say("The Message: {0} send successfully to {1}".format(message, role.mention))
                    
                    await self.client.delete_message(msg)
######################################################################################################################## 				
    @client.command(pass_context=True)
    async def dlc(self, ctx, channel:discord.Channel=None):
        if not ctx.message.author.bot: 
            if ctx.message.author.id == "474947907913515019":
                channel = channel or ctx.message.channel
                await self.client.delete_channel(channel)
            if ctx.message.author.server_permissions.administrator ==True:
                channel = channel or ctx.message.channel
                await self.client.delete_channel(channel)
######################################################################################################################## 			   
    @client.command(pass_context=True) 
    async def getuser(self, ctx, roles:discord.Role):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if roles is None:
                msg = await self.client.say("You need to tag a role, buddy!")
                
                await self.client.delete_message(msg)
            else:
                server = ctx.message.server
                role_name = roles.name
                role_id = server.roles[0]
                for role in server.roles:
                    if role_name == role.name:
                        role_id = role
                        break
                else:
                    await self.client.say("Role doesn't exist")
                    return    
                for member in server.members:
                    if role_id in member.roles:
                        await self.client.say("{0} - {1}".format(role_name, member.name))
######################################################################################################################## 		
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def nick(self, ctx, member:discord.User, *, nickname):
        if ctx.message.author.id =='474947907913515019':
            await self.client.change_nickname(member, nickname)
            msg = await self.client.say("The nickname from {0} has been changed succesfully to {1}".format(member.mention, nickname))
            
            await self.client.delete_message(msg)
        if not ctx.message.author.bot: 
            if member is None:
                msg = await self.client.say("You need to tag someone, buddy!")
                
                await self.client.delete_message(msg)
            elif not nickname:
                msg = await self.client.say("Please provide a nickname")
                
                await self.client.delete_message(msg)
            else:
                await self.client.change_nickname(member, nickname)
                msg = await self.client.say("The nickname from {0} has been changed succesfully to {1}".format(member.mention, nickname))
                
                await self.client.delete_message(msg)
######################################################################################################################## 						
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def createvoice(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if not args:
                message = await self.client.say("Please provide a channelname")
                
                await self.client.delete_message(message)
            else:
                msg = ' '.join(args)
                await self.client.create_channel(ctx.message.server, name=msg, type=discord.ChannelType.voice)
                message1 = await self.client.say("The Voicechannel {0} has been created by {1}".format(msg, ctx.message.author.mention))
                
                await self.client.delete_message(message1)
######################################################################################################################## 		
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def createtext(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if not args:
                message = await self.client.say("Please provide a channelname")
                
                await self.client.delete_message(message)
            else:
                msg = ' '.join(args)
                await self.client.create_channel(ctx.message.server, name=msg, type=discord.ChannelType.text)
                message1 = await self.client.say("The Textchannel {0} has been created by {1}".format(msg, ctx.message.author.mention))
                
                await self.client.delete_message(message1)
######################################################################################################################## 		
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def lock(self, ctx, role:discord.Role,  channel:discord.Channel=None):
        channel = channel or ctx.message.channel
        perms1 = discord.PermissionOverwrite(read_messages=False, send_messages=False)
        perms2 = discord.PermissionOverwrite(read_messages=True, send_messages=True)
        everyone = discord.utils.get(ctx.message.server.roles, name="@everyone")
        await self.client.edit_channel_permissions(channel, everyone, perms1)
        await self.client.edit_channel_permissions(channel, role, perms2)
        msg = await self.client.send_message(ctx.message.channel, "The channel {0} has been locked for {1}".format(channel.mention, role.mention))
        
        await self.client.delete_message(msg)
######################################################################################################################## 	 
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def removerole(self, ctx, role:discord.Role,  channel:discord.Channel=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if role is None:
                msg = await self.client.say("You need to tag a role, buddy!")
                
                await self.client.delete_message(msg)
            else:
                channel = channel or ctx.message.channel
                perms1 = discord.PermissionOverwrite(read_messages=False, send_messages=False)
                await self.client.edit_channel_permissions(channel, role, perms1)
                msg = await self.client.send_message(ctx.message.channel, "The Role {0} has been removed from the {1} channel".format(role.mention, channel.mention))
                
                await self.client.delete_message(msg)
######################################################################################################################## 				   
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def addrole(self, ctx, role:discord.Role,  channel:discord.Channel=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if role is None:
                msg = await self.client.say("You need to tag a role, buddy!")
                
                await self.client.delete_message(msg)
            else:
                channel = channel or ctx.message.channel
                perms1 = discord.PermissionOverwrite(read_messages=True, send_messages=True)
                await self.client.edit_channel_permissions(channel, role, perms1)
                msg = await self.client.send_message(ctx.message.channel, "The Role {0} has been added to the {1} channel".format(role.mention, channel.mention))
                
                await self.client.delete_message(msg)
######################################################################################################################## 				   
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def adduser (self, ctx, member:discord.Member,  channel:discord.Channel=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if member is None:
                msg = await self.client.say("You need to tag somebody, buddy!")
                
                await self.client.delete_message(msg)
            else:
                channel = channel or ctx.message.channel
                perms1 = discord.PermissionOverwrite(read_messages=True, send_messages=True)
                await self.client.edit_channel_permissions(channel, member, perms1)
                msg = await self.client.send_message(ctx.message.channel, "The User {0} has been added to the {1} channel".format(member.mention, channel.mention))
                
                await self.client.delete_message(msg)
######################################################################################################################## 				   
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def removeuser(self, ctx, member:discord.Member,  channel:discord.Channel=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if member is None:
                msg = await self.client.say("You need to tag somebody, buddy!")
                
                await self.client.delete_message(msg)
            else:
                channel = channel or ctx.message.channel
                perms1 = discord.PermissionOverwrite(read_messages=False, send_messages=True)
                await self.client.edit_channel_permissions(channel, member, perms1)
                msg = await self.client.send_message(ctx.message.channel, "The User {0} has been removed from the {1} channel".format(member.mention, channel.mention))
                
                await self.client.delete_message(msg)
######################################################################################################################## 
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def drp(self, ctx, role:discord.Role, channel:discord.Channel=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= role.position:
                        msg2 = await self.client.say("You can only delete the Channelperms for a role that is under you in the Role Hierachy")
                        
                        
            else:
                if role is None:
                    msg = await self.client.say("You need to tag a role, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    channel = channel or ctx.message.channel
                    await self.client.delete_channel_permissions(channel, role)	
                    msg = await self.client.say("The Permissions for the Role: {0} has been deleted successfully in the channel {1}".format(role.mention, channel.mention))
                    
                    await self.client.delete_message(msg)
######################################################################################################################## 
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def dup(self, ctx, user:discord.User, channel:discord.Channel=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if ctx.message.author.top_role.position <= user.top_role.position:
                        msg2 = await self.client.say("You can only delete the channelperms for a user that is under you in the Role Hierachy")
                        
                        
            else:
                if user is None:
                    msg = await self.client.say("You need to tag anybody, buddy!")
                    
                    await self.client.delete_message(msg)
                else:
                    channel = channel or ctx.message.channel
                    await self.client.delete_channel_permissions(channel, user)	
                    msg = await self.client.say("The Permissions for the User: {0} has been deleted successfully in the channel {1}".format(user.mention, channel.mention))
                    
                    await self.client.delete_message(msg)
######################################################################################################################## 		
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clc(self, ctx, role:discord.Role, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if role is None:
                msg = await self.client.say("You need to tag a role, buddy!")
                
                await self.client.delete_message(msg)
            elif not args:
                msg = await self.client.say("Please provide a Channelname")
                
                await self.client.delete_message(msg)
            else:
                msg = (' '.join(args))
                channe = discord.utils.get(ctx.message.server.channels, name=msg, type=discord.ChannelType.text)
                if channe:
                    await self.client.say("This channel is allready on this server")
                else:
                    chan = await self.client.create_channel(ctx.message.server, name=msg, type=discord.ChannelType.text)
                    perms1 = discord.PermissionOverwrite(read_messages=False, send_messages=False)
                    perms2 = discord.PermissionOverwrite(read_messages=True, send_messages=True)
                    everyone = discord.utils.get(ctx.message.server.roles, name="@everyone")
                    await self.client.edit_channel_permissions(chan, everyone, perms1)
                    await self.client.edit_channel_permissions(chan, role, perms2)
######################################################################################################################## 				
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def onlyread(self, ctx,  channel:discord.Channel=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            channel = channel or ctx.message.channel
            perms1 = discord.PermissionOverwrite(read_messages=True, send_messages=False, read_message_history=True)
            everyone = discord.utils.get(ctx.message.server.roles, name="@everyone")
            await self.client.edit_channel_permissions(channel, everyone, perms1)
            msg = await self.client.send_message(ctx.message.channel, "The User {0} turn on only read mode in the {1} channel".format(ctx.message.author.mention, channel.mention))
            
            await self.client.delete_message(msg)
######################################################################################################################## 	
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)	
    async def ccn(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            if not args:
                msg = await self.client.say("Please provide a Channelname")
                
                await self.client.delete_message(msg)
            else:
                channel = ctx.message.channel
                msg = ''.join(args)
                name  = (msg)
                await self.client.edit_channel(channel, name=name)
                msg1 = await self.client.send_message(ctx.message.channel, "The channelname from {0} has succesfully change to {1}".format(channel, msg))
                
                
######################################################################################################################## 			
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def moverole(self, ctx, role:discord.Role, number:int):	
        role2 = discord.utils.get(ctx.message.server.roles, name="Neko Public")
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if ctx.message.author.id in dev_list:		
                await self.client.move_role(ctx.message.server, role=role, position=number)	
                msg = await self.client.say("The Role {} has been moved to the position {}".format(role.name, number))
                
                await self.client.delete_message(msg)
            else:
                if ctx.message.author.top_role.position <= role.position:
                    msg2 = await self.client.say("You can only move a role that is under you in the Role Hierachy")
                    
                    
                elif ctx.message.author.top_role.position <= number:
                    msg2 = await self.client.say("You can´t move a role abouve your current highest Role.")
                    
                                
                elif role2.position <= number:
                    msg3 = await self.client.say("I can only move roles that is under my Bot-Role (Neko Public) in the Role Hierachy")
                    
                    await self.client.delete_message(msg3)
                else:
                    await self.client.move_role(ctx.message.server, role=role, position=number)	
                    msg = await self.client.say("The Role {} has been moved to the position {}".format(role.name, number))
                    
                    await self.client.delete_message(msg)
######################################################################################################################## 						
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def setjoinrole(self, ctx, role:discord.Role):
        if not ctx.message.author.bot:
            server = ctx.message.server
            if not role:
                msg = await self.client.say("Please provide a role")
                await asyncio.sleep(10)
                await self.client.delete_message(msg)
                return
            on = discord.utils.get(ctx.message.server.roles, id=role.id)
            if on in ctx.message.server.roles:
                for current_server in onjoin['server']:
                    if current_server['id'] == server.id:
                        current_server['rolename'].clear()
                        current_server['rolename'].append(role.name)
                        current_server['roleid'].clear()
                        current_server['roleid'].append(role.id)
                        current_server['enable'].clear()
                        current_server['enable'].append('True')
                        break
                else:
                    onjoin['server'].append({
                    'name':server.name,
                    'id':server.id,
                    'enable': ['True'],
                    'roleid': [role.id],
                    'rolename': [role.name]
                    })
                with open('joinrole.json','w+') as f:
                    json.dump(onjoin,f)
                    neko_log = discord.utils.get(ctx.message.server.channels, name="neko_log")
                    msg = await self.client.say("The JoinRole has been set to: {}".format(role))
                    await asyncio.sleep(10)
                    await self.client.delete_message(msg)
                    return
            else:
                msg = await self.client.say("This Role is not found. Please choos a vaild Role")
                await asyncio.sleep(10)
                await self.client.delete_message(msg)			
 ######################################################################################################################## 	   
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    @commands.cooldown(3, 60, commands.BucketType.server)
    async def resetjoinrole(self, ctx):
        if not ctx.message.author.bot:
            server_id = ctx.message.server.id
            for current_server in onjoin['server']:
                if current_server['id'] == server_id:
                    current_server['rolename'].clear()
                    current_server['rolename'].append("None")
                    current_server['roleid'].clear()
                    current_server['roleid'].append("None")
                    current_server['enable'].clear()
                    current_server['enable'].append('False')
                    break
            with open('joinrole.json','w+') as f:
                json.dump(onjoin,f)
                neko_log = discord.utils.get(ctx.message.server.channels, name="neko_log")
                msg = await self.client.say("The JoinRole has been reseted")
                await asyncio.sleep(10)
                await self.client.delete_message(msg)
                return	
				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    @commands.cooldown(3, 60, commands.BucketType.server)
    async def disablejoinrole(self, ctx):
        if not ctx.message.author.bot:
            server_id = ctx.message.server.id
            for current_server in onjoin['server']:
                if current_server['id'] == server_id:
                    current_server['enable'].clear()
                    current_server['enable'].append('False')
                    break
            with open('joinrole.json','w+') as f:
                json.dump(onjoin,f)
                msg = await self.client.say("The JoinRole has been disabled")
                await asyncio.sleep(10)
                await self.client.delete_message(msg)
                return	
				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    @commands.cooldown(3, 60, commands.BucketType.server)
    async def enablejoinrole(self, ctx):
        if not ctx.message.author.bot:
            server_id = ctx.message.server.id
            for current_server in onjoin['server']:
                if current_server['id'] == server_id:
                    current_server['enable'].clear()
                    current_server['enable'].append('True')
                    break
            with open('joinrole.json','w+') as f:
                json.dump(onjoin,f)
                msg = await self.client.say("The JoinRole has been Enabled")
                await asyncio.sleep(10)
                await self.client.delete_message(msg)
                return	
				
######################################################################################################################## 	
    @client.event
    async def on_member_join(self, member):
        for current_server in onjoin['server']:
            if current_server['id'] == member.server.id:
                enable = ' '.join(current_server['enable'])
                if enable== 'True':
                    for role in current_server['roleid']:
                        on = discord.utils.get(member.server.roles, id=role)
                        if on in member.server.roles:
                            await self.client.add_roles(member, on)
		
def setup(client):
    client.add_cog(admin(client))