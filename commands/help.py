import discord
from discord.ext import commands
import asyncio
import sys
import random
from discord.ext.commands import CommandNotFound
from datetime import datetime
import json
import os

client = commands.Bot(command_prefix='nl!')

botcolor = 0x000ffc

client.remove_command('help')

dev_list = ['474947907913515019', '486988989262462991']

disable_list = ['00000000000000000']


def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991"]
		
    return commands.check(predicate)
	
class help:
    def __init__(self, client):
        self.client = client
########################################################################################################################
########################################################################################################################
########################################################################################################################					
    @client.command(pass_context=True)
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def help(self, ctx):		
        if not ctx.message.author.bot: 
            if not ctx.message.author.id in dev_list:
                if ctx.message.author.server_permissions.administrator ==True:
                    author=ctx.message.author
                    embed=discord.Embed(
                        color=ctx.message.author.top_role.color)
                    embed.set_author(name='Admin help Menu')
                    embed.add_field(name='nl!admin (Only for Server Admin´s)', value='Show all Admin commands', inline='False')
                    embed.add_field(name='nl!member (For all Server Members)', value='Show all Member commands', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')					
                    embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                if not ctx.message.author.server_permissions.administrator ==True:
                    author=ctx.message.author
                    embed=discord.Embed(
                        color=ctx.message.author.top_role.color)
                    embed.set_author(name='Member Commands')
                    embed.add_field(name='**nl!callsupport [reason]**', value='Do you have a problem with Neko Public?\nCall us and we come for you!!!  🛠', inline='False')
                    embed.add_field(name='**nl!support**', value='You don´t want that we join your server?\n No problem, join our server and call us for help.  💫', inline='False')
                    embed.add_field(name='nl!say [text]', value='Let Neko write whatever you want ✍️', inline='False')
                    embed.add_field(name='nl!userinfo [user]', value='Show you some informations about a tagged user :information_source:', inline='False')
                    embed.add_field(name='nl!hack [user]', value='hack a mentioned user :D :hash:', inline='False')
                    embed.add_field(name='nl!whisper[user] [text]', value='send the mentioned user a pm from Neko :busts_in_silhouette:', inline='False')
                    embed.add_field(name='nl!info', value='Show some server and client stats :passport_control:', inline='False')
                    embed.add_field(name='nl!invite', value='Create an invite for your server 📩 ', inline='False')
                    embed.add_field(name='nl!ping', value='check the Bot reaction ☄️', inline='False')
                    embed.add_field(name='nl!tempchannel [name]', value='Create a temporal text-channel on your server which delete automatically after 10 minutes ⌨️', inline='False')
                    embed.add_field(name='nl!tempvoice  [name]', value='Create a temporal voice-channel on your server which delete automatically after 10 minutes 📞', inline='False')
                    embed.add_field(name='nl!one_to_twenty', value='Neko give you 5 random numbers 👨🏼‍🏫', inline='False')
                    embed.add_field(name='nl!finduser [id]', value='search for a user that id you type in 👀', inline='False')
                    embed.add_field(name='nl!dbl', value='Shows the DBL description 📄', inline='False')
                    embed.add_field(name='nl!roleinfo [role]', value='Give you some informations about that Role 🔮', inline='False')
                    embed.add_field(name='nl!channelinfo [channel]', value='Give you some informations about the channel 🔦', inline='False')
                    embed.add_field(name='nl!weeb [name]', value='How many % weeb is the Person?', inline='False')
                    embed.add_field(name='nl!sortname [name]', value='Sort the Nameletters of the Tagged person', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                    embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
            if ctx.message.author.id in dev_list:
                author=ctx.message.author
                embed=discord.Embed(
                    color=ctx.message.author.top_role.color)
                embed.set_author(name='Neko Dev help menu')
                embed.add_field(name='nl!owner (Only for the Bot Owner)', value='Show all Bot Owner commands', inline='False')
                embed.add_field(name='nl!admin (Only for Server Admin´s)', value='Show all Admin commands', inline='False')
                embed.add_field(name='nl!member (For all Server Members)', value='Show all Member commands', inline='False')
                embed.add_field(name='nl!dev (Only for the Bot Devs)', value='Show all Bot Developer commands.', inline='False')
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')					
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                await asyncio.sleep(120)
                await self.client.delete_message(msg1) 
########################################################################################################################	
    @client.event
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "✅":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:
                    if not user.id in dev_list:
                        if user.server_permissions.administrator ==True:
                            author=user
                            embed=discord.Embed(
                                color=user.top_role.color)
                            embed.set_author(name='Admin help Menu')
                            embed.add_field(name='nl!admin (Only for Server Admin´s)', value='Show all Admin commands', inline='False')
                            embed.add_field(name='nl!member (For all Server Members)', value='Show all Member commands', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')					
                            embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                            embed.timestamp = datetime.utcnow()
                            await self.client.edit_message(reaction.message, embed=embed)
                            await self.client.remove_reaction(reaction.message, "✅", user)
                            await self.client.remove_reaction(reaction.message, "✅", reaction.message.author)
                        if not user.server_permissions.administrator ==True:
                            author=user
                            embed=discord.Embed(
                                color=user.top_role.color)
                            embed.set_author(name='Member Commands')
                            embed.add_field(name='**nl!callsupport [reason]**', value='Do you have a problem with Neko Public?\nCall us and we come for you!!!', inline='False')
                            embed.add_field(name='**nl!support**', value='You don´t want that we join your server?\n No problem, join our server and call us for help.', inline='False')
                            embed.add_field(name='nl!say [text]', value='Let Neko write whatever you want :pencil:', inline='False')
                            embed.add_field(name='nl!userinfo [user]', value='Show you some informations about a tagged user :information_source:', inline='False')
                            embed.add_field(name='nl!hack [user]', value='hack a mentioned user :D :hash:', inline='False')
                            embed.add_field(name='nl!whisper[user] [text]', value='send the mentioned user a pm from Neko :busts_in_silhouette:', inline='False')
                            embed.add_field(name='nl!stats', value='Show some server and client stats :passport_control:', inline='False')
                            embed.add_field(name='nl!invite', value='Create an invite for your server', inline='False')
                            embed.add_field(name='nl!ping', value='check the Bot reaction', inline='False')
                            embed.add_field(name='nl!tempchannel [name]', value='Create a temporal text-channel on your server which delete automatically after 10 minutes', inline='False')
                            embed.add_field(name='nl!tempvoice  [name]', value='Create a temporal voice-channel on your server which delete automatically after 10 minutes', inline= 'False')
                            embed.add_field(name='nl!one_to_twenty', value='Neko give you 5 random numbers', inline='False')
                            embed.add_field(name='nl!finduser [id]', value='search for a user that id you type in', inline='False')
                            embed.add_field(name='nl!dbl', value='Shows the DBL description', inline='False')
                            embed.add_field(name='nl!roleinfo [role]', value='Give you some informations about that Role', inline='False')
                            embed.add_field(name='nl!channelinfo [channel]', value='Give you some informations about the channel', inline='False')
                            embed.add_field(name='nl!weeb [name]', value='How many % weeb is the Person?', inline='False')
                            embed.add_field(name='nl!sortname [name]', value='Sort the Nameletters of the Tagged person', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                            embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                            embed.timestamp = datetime.utcnow()
                            await self.client.edit_message(reaction.message, embed=embed)
                            await self.client.remove_reaction(reaction.message, "✅", user) 
                            await self.client.remove_reaction(reaction.message, "✅", reaction.message.author)
                    if user.id in dev_list: 
                        author=user
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Neko Dev help menu')
                        embed.add_field(name='nl!owner (Only for the Bot Owner)', value='Show all Bot Owner commands', inline='False')
                        embed.add_field(name='nl!admin (Only for Server Admin´s)', value='Show all Admin commands', inline='False')
                        embed.add_field(name='nl!member (For all Server Members)', value='Show all Member commands', inline='False')
                        embed.add_field(name='nl!dev (Only for the Bot Devs)', value='Show all Bot Developer commands.', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')					
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed)
                        await self.client.remove_reaction(reaction.message, "✅", user)
                        await self.client.remove_reaction(reaction.message, "✅", reaction.message.author)
        if reaction.emoji == "❎":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if reaction.message.author.bot:
                        try:
                            await self.client.delete_message(reaction.message)
                        except:
                            embed=discord.Embed(description='I am sorry {0}, but i have not enough permissions to delete this message'.format(user.mention), color=user.top_role. color)
                            embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                            embed.timestamp = datetime.utcnow()
                            await self.client.edit_message(reaction.message, embed=embed) 
                            await self.client.remove_reaction(reaction.message, "✅", user)
                            await self.client.remove_reaction(reaction.message, "✅", reaction.message.author)
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
        if reaction.emoji == "🌗":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:  
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.add_field(name='<:Neko_Logo:549531102117625866>Role Moderation<:Neko_Logo:549531102117625866>', value='** **', inline='False')
                        embed.add_field(name='nl!addrole [Role][Channel]', value='add to the mentioned Channel or the command Channel the mentioned Role', inline='False')
                        embed.add_field(name='nl!customrole [Rolename]', value='Create custom Role with the name that you write', inline='False')
                        embed.add_field(name='nl!customadmin [Rolename]', value='Create custom Role with admin permissions ', inline='False')
                        embed.add_field(name='nl!delrole [Role]', value='delete the Role that you mentioned/tipe', inline='False')
                        embed.add_field(name='nl!drp [Role][Channel]', value='Delete the Role permissions in the Mentioned or Command channel', inline='False')
                        embed.add_field(name='nl!give [Role][Member]', value='give the mentioned Member the Role that you tag/write', inline='False')
                        embed.add_field(name='nl!getuser [Role]', value='List all user with the mentioned Role', inline='False')
                        embed.add_field(name='nl!moverole [Role][Positionnumber]', value='Move the tagged role in the written Position. 1 = low, 10+ high', inline='False')
                        embed.add_field(name='nl!removerole [Role][Channel]', value='Remove the Role out of the mentioned or command Channel', inline='False')
                        embed.add_field(name='nl!rolemsg [Role][Message]', value='send a DM to all with the Role that you mention', inline='False')
                        embed.add_field(name='nl!rrp [Role]', value='*R*emove *r*ole *p*ermissions from the Role that you mention', inline='False')
                        embed.add_field(name='nl!write_white [Role][Member]', value='remove the mentioned Member the Role that you tag/write', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed)
                        await self.client.remove_reaction(reaction.message, "🌗", user)
                    if not user.server_permissions.administrator ==True:   
                         await self.client.remove_reaction(reaction.message, "🌗", user)
        if reaction.emoji == "🌑":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:    
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Channel Moderation')
                        embed.add_field(name='nl!createtext [Name]', value='create a Text- channel with the written name', inline='False')
                        embed.add_field(name='nl!createvoice [Name]', value='create a Voice- channel with the written name', inline='False')
                        embed.add_field(name='nl!clc [Role][Name]', value='Create a role-locked channel with the written name', inline='False')
                        embed.add_field(name='nl!ccn [Name]', value='Change the name of the Command channel', inline='False')
                        embed.add_field(name='nl!dlc', value='delete the channel in which you send the message', inline='False')
                        embed.add_field(name='nl!lock [Role][Channel]', value='lock the mentioned channel or the command channel for the mentioned role', inline='False')
                        embed.add_field(name='nl!onlyread [Channel]', value='Turn on the only read mode for @everyone', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "🌑", user)
                    if not user.server_permissions.administrator ==True: 
                        await self.client.remove_reaction(reaction.message, "🌑", user)
        if reaction.emoji == "🌓":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:  
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Member Moderation')
                        embed.add_field(name='nl!adduser [Member][channel]', value='Add the Member out of the mentioned or command channel', inline='False')
                        embed.add_field(name='nl!ban [Member]', value='Ban the mentioned Member', inline='False')
                        embed.add_field(name='nl!clear [Number]', value='clear a chat on the amount of number that you tipe', inline='False')
                        embed.add_field(name='nl!dup [Member][Channel]', value='Delete the Member permissions in the Mentioned or Command channel', inline='False')
                        embed.add_field(name='nl!kick [Member]', value='Kick the mentioned Member', inline='False')
                        embed.add_field(name='nl!mute [Member]', value='Mute a tagged Member', inline='False')
                        embed.add_field(name='nl!nick [Member][Nickname]', value='Nick a mentioned Member', inline='False')
                        embed.add_field(name='nl!removeuser [Member][Channel]', value='Remove the Member out of the mentioned or command channel', inline='False')
                        embed.add_field(name='nl!tempmute [Member][time]', value='Mute the tagged Member for the amount of time', inline='False')
                        embed.add_field(name='nl!unmute [Member]', value='Unmute the tagged Member', inline='False')
                        embed.add_field(name='nl!softban [Member][Days for delete messages][softbantime]', value='softan the mentioned Member', inline='False')
                        embed.add_field(name='nl!voicekick [Member]', value='kick the mentioned Member out of the voicechannel', inline='False')
                        embed.add_field(name='nl!warn [Member][Reason]', value='Warn a mention Member for the reason that you tipe', inline='False')
                        embed.add_field(name='nl!warnings [Member]', value='List you the warnings and reason about the mentioned Member on all supportet servers', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "🌓", user)
                    if not user.server_permissions.administrator ==True:  
                        await self.client.remove_reaction(reaction.message, "🌓", user)
        if reaction.emoji == "🌙":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user is user.server.owner:
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Server Moderation(Server Owner Only)')
                        embed.add_field(name='nl!changeservername [name]', value='change the Servername', inline='False')
                        embed.add_field(name='nl!banlist', value='write a list of all banned users on this server', inline='False')
                        embed.add_field(name='nl!lockeveryone', value='Remove all perms for @everyone for the whole server', inline='False')
                        embed.add_field(name='nl!setverfilevel [level: None, Low, Medium, High]', value='change the server Verification Level', inline='False')
                        embed.add_field(name='nl!giveserverrole [role]', value='Give the tagged role to all users which the Bot have access to.', inline='False')
                        embed.add_field(name='nl!removeserverrole [role]', value='Remove the tagged role from all users which the Bot have access to.', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "🌙", user)
                    if user.id in dev_list:
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Server Moderation(Server Owner Only)')
                        embed.add_field(name='nl!changeservername [name]', value='change the Servername', inline='False')
                        embed.add_field(name='nl!banlist', value='write a list of all banned users on this server', inline='False')
                        embed.add_field(name='nl!lockeveryone', value='Remove all perms for @everyone for the whole server', inline='False')
                        embed.add_field(name='nl!setverfilevel [level: None, Low, Medium, High]', value='change the server Verification Level', inline='False')
                        embed.add_field(name='nl!giveserverrole [role]', value='Give the tagged role to all users which the Bot have access to.', inline='False')
                        embed.add_field(name='nl!removeserverrole [role]', value='Remove the tagged role from all users which the Bot have access to.', inline='False')
                        embed.add_field(name='nl!setjoinrole [role]', value='Set and change the Role that the Users become when they join the Server.', inline='False')
                        embed.add_field(name='nl!resetjoinrole', value='Remove the Role that the Users become when they join the Server.', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "🌙", user)
                    else:
                        await self.client.remove_reaction(reaction.message, "🌙", user)
        if reaction.emoji == "🌝":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True: 
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Administrator Navigation Menu')
                        embed.add_field(name='Reaction: 🌗', value='Open the Role Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌑', value='Open the Channel Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌙', value='Open the Server Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌓', value='Open the Member Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌝', value='Back to this Menu', inline='False')
                        embed.add_field(name='Reaction: ❌', value='Close the Administrator Menu', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "🌝", user)
                    if not user.server_permissions.administrator ==True:  
                        await self.client.remove_reaction(reaction.message, "🌝", user)
        if reaction.emoji == "❌":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True: 
                        if reaction.message.author.id == "533372604350988299":
                            await self.client.delete_message(reaction.message)
                    if not user.server_permissions.administrator ==True:  
                        await self.client.remove_reaction(reaction.message, "❌", user)
########################################################################################################################
        if reaction.emoji == "🌟":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:  
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Server Economy')
                        embed.add_field(name='JoinRole menu 💠', value='Open the help menu for the JoinRole', inline='False')
                        embed.add_field(name='Word Blocker menu 🌐', value='Open the help menu for the Wordblocker', inline='False')
                        embed.add_field(name='Logchannel menu 🎞', value='Open the help menu for the Logchannel', inline='False')
                        embed.add_field(name='NSFW channel menu 🔞', value='Open the help menu for the NSFW channel', inline='False')
                        embed.add_field(name='Admin Menu ❕', value='Return to the admin menu', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg = await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(msg, "🌟", user)
                        await self.client.remove_reaction(msg, "🌗", reaction.message.author)
                        await self.client.remove_reaction(msg, "🌑", reaction.message.author)
                        await self.client.remove_reaction(msg, "🌙", reaction.message.author)
                        await self.client.remove_reaction(msg, "🌓", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "🌝", reaction.message.author)
                        await self.client.add_reaction(msg, "🌐")
                        await self.client.add_reaction(msg, "💠")
                        await self.client.add_reaction(msg, "🎞")
                        await self.client.add_reaction(msg, "🔞")
                        await self.client.add_reaction(msg, "❕")
                    if not user.server_permissions.administrator ==True:  
                        await self.client.remove_reaction(reaction.message, "🌓", user)
        if reaction.emoji == "🌐":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:  
                        embed = discord.Embed(
                            color=user.top_role.color)
                        embed.add_field(name='WordBlocker Menu', value='** **', inline=False)
                        embed.add_field(name='nl!addword [word]', value='Add a word to the wordblacklist and turn the Wordblocker to on', inline='False')
                        embed.add_field(name='nl!removeword [word]', value='Remove a word from the wordblacklist', inline='False')
                        embed.add_field(name='nl!clearwords', value='Clear the wordblacklist', inline='False')
                        embed.add_field(name='nl!disablewordblocker', value='Turns the Wordblocker to off', inline='False')
                        embed.add_field(name='nl!enablewordblocker', value='Turns the Wordblocker to on', inline='False')
                        embed.add_field(name='nl!wordblockerinfo', value='Give you infos about the wordblocker', inline='False')
                        embed.add_field(name='nl!ignorechannel [channel]', value='Add the Channel to the ignorelist', inline='False')
                        embed.add_field(name='nl!removeignorechannel [channel]', value='Remove the Channel from the ignorelist', inline='False')
                        embed.add_field(name='nl!clearignorechannels', value='Remove all ignore channels from the irgnored Channel list', inline='False')
                        author = user
                        embed.set_footer(text='Message was requested by: {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed)
                        await self.client.remove_reaction(reaction.message, "🌐", user)
                    if not user.server_permissions.administrator ==True:   
                        await self.client.remove_reaction(reaction.message, "🌐", user)
        if reaction.emoji == "💠":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:    
                        embed = discord.Embed(
                            color=user.top_role.color)
                        embed.add_field(name='JoinRole Menu', value='** **', inline=False)
                        embed.add_field(name='nl!setjoinrole [role]', value='Set and change the Role that the Users become when they join the Server.', inline='False')
                        embed.add_field(name='nl!resetjoinrole', value='Remove the Role that the Users become when they join the Server.', inline='False')
                        embed.add_field(name='nl!disablejoinrole', value='Disable the Role that the Users become when they join the Server.', inline='False')
                        embed.add_field(name='nl!enablejoinrole', value='Enable the Role that the Users become when they join the Server.', inline='False')
                        author = user
                        embed.set_footer(text='Message was requested by: {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "💠", user)
                    if not user.server_permissions.administrator ==True: 
                        await self.client.remove_reaction(reaction.message, "💠", user)
        if reaction.emoji == "🎞":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:    
                        embed = discord.Embed(
                            color=user.top_role.color)
                        embed.add_field(name='Logchannel Menu', value='** **', inline=False)
                        embed.add_field(name='nl!setlog [channel]', value='Set the Log messages in the named channel', inline='False')
                        embed.add_field(name='nl!disablelog', value='Disable the Logchannel. Need to set again with nl!setlog', inline='False')
                        embed.add_field(name='nl!loginfo', value='Send a short description and infos about the settings', inline='False')
                        author = user
                        embed.set_footer(text='Message was requested by: {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "🎞", user)
                    if not user.server_permissions.administrator ==True: 
                        await self.client.remove_reaction(reaction.message, "🎞", user)
        if reaction.emoji == "🔞":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True:    
                        embed = discord.Embed(
                            color=user.top_role.color)
                        embed.add_field(name='NSFW channel Menu', value='** **', inline=False)
                        embed.add_field(name='nl!setnsfw [channel]', value='Set the NSFW channel in the named channel', inline='False')
                        embed.add_field(name='nl!disablensfw', value='Disable the NSFW. Need to set again with nl!setnsfw', inline='False')
                        embed.add_field(name='nl!nsfwinfo', value='Send a short description and infos about the NSFW settings', inline='False')
                        author = user
                        embed.set_footer(text='Message was requested by: {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "🔞", user)
                    if not user.server_permissions.administrator ==True: 
                        await self.client.remove_reaction(reaction.message, "🔞", user)						
        if reaction.emoji == "❕":
            if not user.bot:
                if reaction.message.author.id == "533372604350988299":
                    if user.server_permissions.administrator ==True: 
                        embed=discord.Embed(
                            color=user.top_role.color)
                        embed.set_author(name='Administrator Navigation Menu')
                        embed.add_field(name='Reaction: 🌗', value='Open the Role Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌑', value='Open the Channel Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌙', value='Open the Server Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌟', value='Open the Server Economy help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌓', value='Open the Member Moderation help Menu', inline='False')
                        embed.add_field(name='Reaction: 🌝', value='Back to this Menu', inline='False')
                        embed.add_field(name='Reaction: ❌', value='Close the Administrator Menu', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                        embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg = await self.client.edit_message(reaction.message, embed=embed) 
                        await self.client.remove_reaction(reaction.message, "❕", user)
                        await self.client.remove_reaction(reaction.message, "🌐", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "💠", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "❕", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "❌", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "🌝", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "🔞", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "🎞", reaction.message.author)
                        await self.client.remove_reaction(reaction.message, "🌟", reaction.message.author)
                        await self.client.add_reaction(msg, "🌗")
                        await self.client.add_reaction(msg, "🌑")
                        await self.client.add_reaction(msg, "🌙")
                        await self.client.add_reaction(msg, "🌓")
                        await self.client.add_reaction(msg, "🌟")
                        await self.client.add_reaction(msg, "🌝")
                        await self.client.add_reaction(msg, "❌")
                    if not user.server_permissions.administrator ==True:  
                        await self.client.remove_reaction(reaction.message, "🌝", user)
########################################################################################################################
    @client.command(pass_context=True)
    @is_vale()
    async def owner(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot: 
            author=ctx.message.author
            embed=discord.Embed(
            color=ctx.message.author.top_role.color)
            embed.set_author(name='Neko Owner Commands')
            embed.add_field(name='nl!findserver [id]', value='Give you the Informations about the ID servers. The Bot need a member of this servers', inline='False')
            embed.add_field(name='nl!goodnight', value='send Neko sleep :zzz:', inline='False')
            embed.add_field(name='nl!leave', value='The bot leaves the message servers :warning:', inline='False')
            embed.add_field(name='nl!load', value='load an extension :zap:', inline='False')
            embed.add_field(name='nl!reload', value='reload an extension :zap:', inline='False')
            embed.add_field(name='nl!servers', value='list you a list with all servers that the bot support', inline='False')
            embed.add_field(name='nl!unload', value='unload an extension :zap:', inline='False')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
            embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg1 = await self.client.send_message(ctx.message.channel, embed=embed) 
            await self.client.add_reaction(msg1, "❎")
########################################################################################################################	
########################################################################################################################		
    @client.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def admin(self, ctx):	
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
                embed=discord.Embed(
                    color=ctx.message.author.top_role.color)
                embed.set_author(name='Administrator Navigation Menu')
                embed.add_field(name='Reaction: 🌗', value='Open the Role Moderation help Menu', inline='False')
                embed.add_field(name='Reaction: 🌑', value='Open the Channel Moderation help Menu', inline='False')
                embed.add_field(name='Reaction: 🌙', value='Open the Server Moderation help Menu', inline='False')
                embed.add_field(name='Reaction: 🌓', value='Open the Member Moderation help Menu', inline='False')
                embed.add_field(name='Reaction: 🌟', value='Open the Server Economy help Menu', inline='False')
                embed.add_field(name='Reaction: 🌝', value='Back to this Menu', inline='False')
                embed.add_field(name='Reaction: ❌', value='Close the Administrator Menu', inline='False')
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await self.client.send_typing(ctx.message.channel)
                msg = await self.client.send_message(ctx.message.channel, embed=embed)
                await self.client.add_reaction(msg, "🌗")
                await self.client.add_reaction(msg, "🌑")
                await self.client.add_reaction(msg, "🌙")
                await self.client.add_reaction(msg, "🌓")
                await self.client.add_reaction(msg, "🌟")
                await self.client.add_reaction(msg, "🌝")
                await self.client.add_reaction(msg, "❌")
                #nl!reload commands.admin
########################################################################################################################		
		
def setup(client):
    client.add_cog(help(client))