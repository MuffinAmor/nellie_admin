import discord
from discord.ext import commands
from datetime import datetime
import asyncio
import json
import os

client = commands.Bot(command_prefix='nl!')

os.chdir(r'/home/pi/Nellie/commands/data')

if os.path.isfile("wordblocker.json"):
    with open('wordblocker.json', encoding='utf-8') as f:
        blocked = json.load(f)
else:
    blocked = {}
    blocked['clients'] = []
    with open('wordblocker.json','w+') as f:
        json.dump(blocked , f, indent=4)	

	
botcolor = 0xfffe00

pass_list = ['474947907913515019, 533372604350988299, 547124033410564116, 558758078011670549']

client.remove_command('help')

class wordblocker:
    def __init__(self, client):
        self.client = client
		
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def wordblockerinfo(self, ctx):
        if not ctx.message.author.bot:   
            server = ctx.message.server
            for current_word in blocked['clients']:
                if current_word['id'] == server.id:
                    enable = ''.join(current_word['enable'])
                    word = ', '.join(current_word['words'])
                    channelid = ', '.join(current_word['ignoredchannelid'])
                    channel = discord.utils.get(ctx.message.server.channels, id=channelid, type=discord.ChannelType.text)
                    if enable == "False":
                        embed=discord.Embed(
                            color=ctx.message.author.top_role.color)
                        embed.add_field(name='Wordblockerinfo', value='** **', inline=False)
                        embed.add_field(name='Server', value=server.name, inline=True)
                        embed.add_field(name='Wordblocker Online?', value=enable, inline=True)
                        embed.add_field(name='Blocked Words:', value="None", inline=False)
                        embed.add_field(name='Ignored Channels:', value=channel, inline=False)
                        embed.add_field(name='Infos', value="The words in the wordblocker get deleted in all enabled channels when somebody write it (admin or not.)\nExamples:\n hello*word*All\nHello *word* all\n WordHello all", inline=False)
                        embed.set_thumbnail(url=server.icon_url)
                        embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                        return
                    else:
                        embed=discord.Embed(
                            color=ctx.message.author.top_role.color)
                        embed.add_field(name='Wordblockerinfo', value='** **', inline=False)
                        embed.add_field(name='Server', value=server.name, inline=True)
                        embed.add_field(name='Wordblocker Online?', value=enable, inline=True)
                        embed.add_field(name='Blocked Words:', value=word, inline=False)
                        embed.add_field(name='Ignored Channels:', value=channel, inline=False)
                        embed.add_field(name='Infos', value="The words in the wordblocker get deleted in all enabled channels when somebody write it (admin or not.)\nExamples:\n hello*word*All\nHello *word* all\n WordHello all", inline=False)
                        embed.set_thumbnail(url=server.icon_url)
                        embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                        return
            else:
                embed=discord.Embed(
                    color=ctx.message.author.top_role.color)
                embed.add_field(name='Wordblockerinfo', value='** **', inline=False)
                embed.add_field(name='Server', value=server.name, inline=True)
                embed.add_field(name='Wordblocker Online?', value="False", inline=True)
                embed.add_field(name='Blocked Words:', value="None", inline=False)
                embed.add_field(name='Ignored Channels:', value="None", inline=False)
                embed.add_field(name='Infos', value="The words in the wordblocker get deleted in all enabled channels when somebody write it (admin or not.)\nExamples:\n hello*word*All\nHello *word* all\n *word*Hello all", inline=False)
                embed.set_thumbnail(url=server.icon_url)
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                msg1 = await self.client.send_message(ctx.message.channel, embed=embed)
                return
		
    @client.event
    async def on_message(self, message):
        if not message.author.id in pass_list:
            if not message.author.bot:
                server = message.server
                for current_word in blocked['clients']:
                    enable = ''.join(current_word['enable'])
                    if current_word['id'] == server.id:
                        if enable == "True":
                            channelid = ' '.join(current_word['ignoredchannelid'])
                            if channelid == "None":
                                wordlist = list(current_word['words'])
                                for word in wordlist:
                                    if word in message.content:
                                        await self.client.delete_message(message)
                                        msg = await self.client.send_message(message.channel, "I am sorry {0} but a Word in your message content is not allowed in this Chat".format(message.author.mention))
                                        break
                            else:
                                channel = discord.utils.get(message.server.channels, id=channelid, type=discord.ChannelType.text)
                                if message.channel.id is channel.id:
                                    break
                                else:
                                    wordlist = list(current_word['words'])
                                    for word in wordlist:
                                        if word in message.content:
                                            await self.client.delete_message(message)
                                            msg = await self.client.send_message(message.channel, "I am sorry {0} but a Word in your message content is not allowed in this Chat".format(message.author.mention))
                                            break

				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def addword(self, ctx, *word:str):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            server = ctx.message.server
            active = 'True'
            if not word:
                msg = await self.client.say("Please provide a word")
                return
            word = ' '.join(word)
            for current_word in blocked['clients']:
                if current_word['id'] == server.id:
                    current_word['words'].append(word)
                    current_word['enable'].clear()
                    current_word['enable'].append(active)
                    break
            else:
                blocked['clients'].append({
                'name':server.name,
                'id':server.id,
                'enable': [active],
                'ignoredchannelname': ['None', ],
                'ignoredchannelid': ['None', ],
                'words': [word, ],
                })
            with open('wordblocker.json','w+') as f:
                json.dump(blocked,f, indent=4)
                msg = await self.client.say("The Word {0} has been added to the Wordblacklist.".format(word))
				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def clearwords(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            server = ctx.message.server
            for current_word in blocked['clients']:
                if current_word['id'] == server.id:
                    current_word['words'].clear()
                    current_word['enable'].clear()
                    current_word['enable'].append("False")
                    break
            with open('wordblocker.json','w+') as f:
                json.dump(blocked,f, indent=4)
                msg = await self.client.say("The Wordblacklist has been cleared")
				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def removeword(self, ctx, *args:str):
        if not ctx.message.author.bot:
            server = ctx.message.server
            delword = ' '.join(args)
            if not delword:
                msg = await self.client.say("Please provide a word")
                return

            else:
                for current_word in blocked['clients']:
                    if current_word['id'] == server.id:
                        word1 = ' '.join(current_word['words'])
                        if not delword in word1:
                            msg = await self.client.say("Please please choose a word that is in the list")
                            
                            await self.client.delete_message(msg)
                        else:
                            current_word['words'].remove(delword)
                            word2 = ' '.join(current_word['words'])
                            if not word2:
                                current_word['enable'].clear()
                                current_word['enable'].append("False")
                                break    
                        
                with open('wordblocker.json','w+') as f:
                    json.dump(blocked,f, indent=4)
                    msg = await self.client.say("The Word *{0}* has been removed from the Wordblacklist.".format(delword)) 
				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def disablewordblocker(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.message.server
            for current_word in blocked['clients']:
                if current_word['id'] == server.id:
                    current_word['enable'].clear()
                    current_word['enable'].append("False")
                    break
            with open('wordblocker.json','w+') as f:
                json.dump(blocked,f, indent=4)
                msg = await self.client.say("The Wordblacklist has been disabled.")
				
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def enablewordblocker(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.message.server
            for current_word in blocked['clients']:
                if current_word['id'] == server.id:
                    current_word['enable'].clear()
                    current_word['enable'].append("True")
                    break
            with open('wordblocker.json','w+') as f:
                json.dump(blocked,f, indent=4)
                msg = await self.client.say("The Wordblacklist has been enabled.")
				

    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def ignorechannel(self, ctx, channel:discord.Channel):
        if not ctx.message.author.bot:
            if not channel:
                msg = await self.client.say("Please provide a channel")
                return
            else:
                server = ctx.message.server
                for current_word in blocked['clients']:
                    if current_word['id'] == server.id:
                        channel1 = ' '.join(current_word['ignoredchannelid'])
                        if channel1 == 'None':
                            current_word['ignoredchannelid'].clear()
                            current_word['ignoredchannelid'].append(channel.id)
                            current_word['ignoredchannelname'].clear()
                            current_word['ignoredchannelname'].append(channel.name)
                        else:
                            current_word['ignoredchannelid'].append(channel.id)
                            current_word['ignoredchannelname'].append(channel.name)
                            break
                with open('wordblocker.json','w+') as f:
                    json.dump(blocked,f, indent=4)
                    msg = await self.client.say("The Channel **{}** has been added to the Ignored Channels.".format(channel.name))

                
					
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def removeignoredchannel(self, ctx, channel:discord.Channel):
        if not ctx.message.author.bot:
            server = ctx.message.server
            if not channel:
                msg = await self.client.say("Please provide a channelname")
                await asyncio.sleep(10)
                await self.client.delete_message(msg)
                return
            else:
                for current_word in blocked['clients']:
                    if current_word['id'] == server.id:
                        word1 = ' '.join(current_word['ignoredchannelid'])
                        if not channel.id in word1:
                            msg = await self.client.say("Please please choose a Channel that is in the list")

                        else:
                            current_word['ignoredchannelid'].remove(channel.id)
                            current_word['ignoredchannelname'].remove(channel.name)
                            word2 = ' '.join(current_word['ignoredchannelid'])
                            if not word2:
                                current_word['ignoredchannelname'].clear()
                                current_word['ignoredchannelid'].clear()
                                current_word['ignoredchannelname'].append("None")
                                current_word['ignoredchannelid'].append("None")
                                break    
                        
                with open('wordblocker.json','w+') as f:
                    json.dump(blocked,f, indent=4)
                    msg = await self.client.say("The Word *{0}* has been removed from the Wordblacklist.".format(delword)) 

  
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def clearignorechannels(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.message.server
            for current_word in blocked['clients']:
                if current_word['id'] == server.id:
                    current_word['ignoredchannelid'].clear()
                    current_word['ignoredchannelid'].append("None")
                    current_word['ignoredchannelname'].clear()
                    current_word['ignoredchannelname'].append("None")
                    break
            with open('wordblocker.json','w+') as f:
                json.dump(blocked,f, indent=4)
                msg = await self.client.say("The ignored channels has been cleared.")


    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def safewb(self, ctx):
        with open('wordblocker.json','w+') as f:
            json.dump(blocked,f, indent=4)
            msg = await self.client.say("Your settings has been safed succesfully")

def setup(client):
    client.add_cog(wordblocker(client))