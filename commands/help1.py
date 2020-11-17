import discord
from discord.ext import commands 
import asyncio
from datetime import datetime
import sys
import os
import json

os.chdir(r'/home/pi/Nellie/commands/data')
if os.path.isfile("nsfw.json"):
    with open('nsfw.json', encoding='utf-8') as f:
        nsfw = json.load(f)
else:
    nsfw = {}
    nsfw['data'] = []
    with open('nsfw.json','w+') as f:
        json.dump(nsfw , f, indent=4)	

client = commands.Bot(command_prefix='nl!')

botcolor = 0xffffff

dev_list = ['474947907913515019', '486988989262462991']

disable_list = ['00000000000000000']

client.remove_command('help')

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991", "406479076048633857"]

    return commands.check(predicate)
	
class help1:
    def __init__(self, client):
        self.client = client
########################################################################################################################		
    @client.command(pass_context=True)
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def member(self, ctx):
        if not ctx.message.author.bot:
            with open('nsfw.json', encoding='utf-8') as f:
               nsfw = json.load(f)		
            author=ctx.message.author
            embed=discord.Embed(
                color=ctx.message.author.top_role.color)
            embed.set_author(name='Member Navigation')
            embed.add_field(name='Member Commands 👨‍👩‍👧‍👧', value='Show you the Member Commands', inline='False')
            embed.add_field(name='Reddit Commands  🔥', value='Open the Reddit Help Menu', inline='False')
            embed.add_field(name='Info Commands 📜', value='Open the Info Help Menu', inline='False')
            embed.add_field(name='Tenor Commands 📽', value='Open the Tenor Help Menu', inline='False')
            for current_server in nsfw['data']:
                if current_server['id'] == ctx.message.server.id:
                    channel = ' '.join(current_server['channelid'])
                    if channel == ctx.message.channel.id:
                        embed.add_field(name='NSFW Commands 💦', value='Shows you the NSFW Command Navigation', inline='False')
            embed.add_field(name='Calculator Commands 🔢', value='Open the Calculator Menu', inline='False')
            embed.add_field(name='Back  ⏪ ', value='Back to the Navigation', inline='False')
            embed.add_field(name='Close ❎', value='Close the Help Menu', inline='False')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
            embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await self.client.send_message(ctx.message.channel, embed=embed)
            await self.client.add_reaction(msg, "👨‍👩‍👧‍👧")
            await self.client.add_reaction(msg, "🔥")
            await self.client.add_reaction(msg, "📜")
            await self.client.add_reaction(msg, "📽")
            for current_server in nsfw['data']:
                if current_server['id'] == ctx.message.server.id:
                    channel = ' '.join(current_server['channelid'])
                    if channel == ctx.message.channel.id:
                        await self.client.add_reaction(msg, "💦")
            await self.client.add_reaction(msg, "🔢")
            await self.client.add_reaction(msg, "⏪")
            await self.client.add_reaction(msg, "❎")
			
			
    @client.event
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "👨‍👩‍👧‍👧":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Member Commands')
                    embed.add_field(name='**nl!callsupport *reason***', value='Do you have a problem with Neko Public?\nCall us and we come for you!!!', inline='False')
                    embed.add_field(name='**nl!support**', value='You don´t want that we join your server?\n No problem, join our server and call us for help.', inline='False')
                    embed.add_field(name='nl!say *text*', value='Let Neko write whatever you want ✍️', inline='False')
                    embed.add_field(name='nl!hack *user*', value='hack a mentioned user :D :hash:', inline='False')
                    embed.add_field(name='nl!whisper *user text*', value='send the mentioned user a pm from Neko :busts_in_silhouette:', inline='False')
                    embed.add_field(name='nl!invite', value='Create an invite for your server 📩 ', inline='False')
                    embed.add_field(name='nl!ping', value='check the Bot reaction ☄️', inline='False')
                    embed.add_field(name='nl!one_to_twenty', value='Neko give you 5 random numbers 👨🏼‍🏫', inline='False')
                    embed.add_field(name='nl!dbl', value='Shows the DBL description 📄', inline='False')
                    embed.add_field(name='nl!weeb *membername*', value='How much % weeb is the member?', inline='False')
                    embed.add_field(name='nl!smile', value='give u a smile', inline='False')
                    embed.add_field(name='nl!sortname *membername*', value='sort the nameletters of a member', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                    embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await self.client.edit_message(reaction.message, embed=embed)
                    try:
                        await self.client.remove_reaction(reaction.message, "👨‍👩‍👧‍👧", user)
                    except Exception as error:
                        pass
        if reaction.emoji == "🔥":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:			
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Reddit Commands')
                    embed.add_field(name='nl!meme', value='Show you a random meme from Reddit', inline='False')
                    embed.add_field(name='nl!cat', value='Send a sweet cat picture in the chat.', inline='False')
                    embed.add_field(name='nl!dog', value='Send a cute dog picture in the chat', inline='False')
                    embed.add_field(name='nl!anime', value='Show you a random anime meme', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                    embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await self.client.edit_message(reaction.message, embed=embed)
                    try:
                        await self.client.remove_reaction(reaction.message, "🔥", user)
                    except Exception as error:
                        pass
        if reaction.emoji == "📜":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:			
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Info Commands')
                    embed.add_field(name='nl!userinfo *user*', value='Show you some informations about a tagged user :information_source:', inline='False')
                    embed.add_field(name='nl!info', value='Show some server and client stats :passport_control:', inline='False')
                    embed.add_field(name='nl!finduser *id*', value='search for a user that id you type in 👀', inline='False')
                    embed.add_field(name='nl!roleinfo *role*', value='Give you some informations about that Role 🔮', inline='False')
                    embed.add_field(name='nl!channelinfo *channel*', value='Give you some informations about the channel 🔦', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                    embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await self.client.edit_message(reaction.message, embed=embed)
                    try:
                        await self.client.remove_reaction(reaction.message, "📜", user) 
                    except Exception as error:
                        pass 
        if reaction.emoji == "📽":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:			
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Tenor Commands')
                    embed.add_field(name='nl!tenor *title*', value='Search a tenor gif with your title', inline='False')
                    embed.add_field(name='nl!hug *membername*', value='Send your mates love with a hug with his or her name', inline='False')
                    embed.add_field(name='nl!pat *membername*', value='You have been patted', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                    embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await self.client.edit_message(reaction.message, embed=embed)
                    try:
                        await self.client.remove_reaction(reaction.message, "📽", user)  
                    except Exception as error:
                        pass
        if reaction.emoji == "💦":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:			
                    for current_server in nsfw['data']:
                        if current_server['id'] == reaction.message.server.id:
                            channel = ' '.join(current_server['channelid'])
                            if channel == reaction.message.channel.id:
                                embed=discord.Embed(
                                    color=user.color)
                                embed.set_author(name='NSFW Commands')
                                embed.add_field(name='Hentai 😻', value='React to see the Hentai Commands.', inline='False')
                                embed.add_field(name='Reallifeporn 😍', value='React to see the Reallife Porn Commands.', inline='False')
                                embed.add_field(name='Back 👈🏼', value='React to go back to the normal Member Menu', inline='False')
                                embed.add_field(name='Close ❎', value='Close the Member Menu ', inline='False')
                                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                                embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                                embed.timestamp = datetime.utcnow()
                                msg = await self.client.edit_message(reaction.message, embed=embed)
                                await self.client.remove_reaction(reaction.message, "💦", user)  
                                await self.client.remove_reaction(reaction.message, "👨‍👩‍👧‍👧", reaction.message.author)  
                                await self.client.remove_reaction(reaction.message, "🔥", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "📜", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "📽", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "💦", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "🔢", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "⏪", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "❎", reaction.message.author)
                                await self.client.add_reaction(msg, "😻")
                                await self.client.add_reaction(msg, "😍")
                                await self.client.add_reaction(msg, "👈🏼")
                                await self.client.add_reaction(msg, "❎")
        if reaction.emoji == "😻":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:	
                    for current_server in nsfw['data']:
                        if current_server['id'] == reaction.message.server.id:
                            channel = ' '.join(current_server['channelid'])
                            if channel == reaction.message.channel.id:
                                embed=discord.Embed(
                                    color=user.color)
                                embed.set_author(name='Hentai Commands')
                                embed.add_field(name='nl!rule34', value='Shows you a picture from the rule34 subreddit', inline='False')
                                embed.add_field(name='nl!hentai', value='Shows you a picture from the hentai subreddit', inline='False')
                                embed.add_field(name='nl!hentai_gif', value='Shows you a gif from the HENTAI_GIF subreddit', inline='False')
                                embed.add_field(name='nl!pokeporn', value='Shows you a picture from the pokeporn subreddit', inline='False')
                                embed.add_field(name='nl!futanari', value='Shows you a picture from the futanari subreddit', inline='False')
                                embed.add_field(name='nl!hentaibeast', value='Shows you a picture from the HentaiBeast subreddit', inline='False')
                                embed.add_field(name='nl!ahegao', value='Shows you a picture from the ahegao subreddit', inline='False')
                                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                                embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                                embed.timestamp = datetime.utcnow()
                                await self.client.edit_message(reaction.message, embed=embed)
                                try:
                                    await self.client.remove_reaction(reaction.message, "😻", user)  
                                except Exception as error:
                                    pass      		
        if reaction.emoji == "😍":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:	
                    for current_server in nsfw['data']:
                        if current_server['id'] == reaction.message.server.id:
                            channel = ' '.join(current_server['channelid'])
                            if channel == reaction.message.channel.id:        									
                                embed=discord.Embed(
                                    color=user.color)
                                embed.set_author(name='Reallife Porn Commands')
                                embed.add_field(name='nl!porn', value='Shows you a picture from the porn subreddit', inline='False')
                                embed.add_field(name='nl!lesbians', value='Shows you a picture from the lesbains subreddit', inline='False')
                                embed.add_field(name='nl!boobs', value='Shows you a picture from the boobs subreddit', inline='False')
                                embed.add_field(name='nl!ass', value='Shows you a picture from the ass subreddit', inline='False')
                                embed.add_field(name='nl!rearpussy', value='Shows you a picture from the rearpussy subreddit', inline='False')
                                embed.add_field(name='nl!booty', value='Shows you a picture from the booty subreddit', inline='False')
                                embed.add_field(name='nl!porngif', value='Shows you a gif from the porngif subreddit', inline='False')
                                embed.add_field(name='nl!cumsluts', value='Shows you a picture from the cumsluts subreddit', inline='False')
                                embed.add_field(name='nl!tiny', value='Shows you a picture from the dirtysmall subreddit', inline='False')
                                embed.add_field(name='nl!gayporn', value='Shows you a picture from the gayporn subreddit', inline='False')
                                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                                embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                                embed.timestamp = datetime.utcnow()
                                await self.client.edit_message(reaction.message, embed=embed)
                                try:
                                    await self.client.remove_reaction(reaction.message, "😍", user)  
                                except Exception as error:
                                    pass      		
        if reaction.emoji == "👈🏼":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:	
                    for current_server in nsfw['data']:
                        if current_server['id'] == reaction.message.server.id:
                            channel = ' '.join(current_server['channelid'])
                            if channel == reaction.message.channel.id:        		
                                embed=discord.Embed(
                                    color=user.color)				
                                embed.set_author(name='Member Navigation')
                                embed.add_field(name='Member Commands 👨‍👩‍👧‍👧', value='Show you the Member Commands', inline='False')
                                embed.add_field(name='Reddit Commands  🔥', value='Open the Reddit Help Menu', inline='False')
                                embed.add_field(name='Info Commands 📜', value='Open the Info Help Menu', inline='False')
                                embed.add_field(name='Tenor Commands 📽', value='Open the Tenor Help Menu', inline='False')
                                for current_server in nsfw['data']:
                                    if current_server['id'] == reaction.message.server.id:
                                        channel = ' '.join(current_server['channelid'])
                                        if channel == reaction.message.channel.id:
                                            embed.add_field(name='NSFW Commands 💦', value='Shows you the NSFW Command Navigation', inline='False')
                                embed.add_field(name='Calculator Commands 🔢', value='Open the Calculator Menu', inline='False')
                                embed.add_field(name='Back  ⏪ ', value='Back to the Navigation', inline='False')
                                embed.add_field(name='Close ❎ ', value='Close the Help Menu', inline='False')
                                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                                embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                                embed.timestamp = datetime.utcnow()
                                msg = await self.client.edit_message(reaction.message, embed=embed)	 
                                await self.client.remove_reaction(reaction.message, "👈🏼", user)  
                                await self.client.remove_reaction(reaction.message, "😻", reaction.message.author)  
                                await self.client.remove_reaction(reaction.message, "😍", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "👈🏼", reaction.message.author)
                                await self.client.remove_reaction(reaction.message, "❎", reaction.message.author)
                                await self.client.add_reaction(msg, "👨‍👩‍👧‍👧")
                                await self.client.add_reaction(msg, "🔥")
                                await self.client.add_reaction(msg, "📜")
                                await self.client.add_reaction(msg, "📽")
                                for current_server in nsfw['data']:
                                    if current_server['id'] == reaction.message.server.id:
                                        channel = ' '.join(current_server['channelid'])
                                        if channel == reaction.message.channel.id:
                                            await self.client.add_reaction(msg, "💦")
                                await self.client.add_reaction(msg, "🔢")
                                await self.client.add_reaction(msg, "⏪")
                                await self.client.add_reaction(msg, "❎")
		
		
        if reaction.emoji == "🔢":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:			
                    embed=discord.Embed(
                        color=user.color)
                    embed.set_author(name='Calculator Commands')
                    embed.add_field(name='nl!plus *number1 number2*', value='add two numbers', inline='False')
                    embed.add_field(name='nl!subtract *number1 number2*', value='subtract two numbers', inline='False')
                    embed.add_field(name='nl!multiply *number1 number2*', value='multiply two numbers', inline='False')
                    embed.add_field(name='nl!divide *number1 number2*', value='devide two numbers', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                    embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await self.client.edit_message(reaction.message, embed=embed)
                    try:
                        await self.client.remove_reaction(reaction.message, "🔢", user)  
                    except Exception as error:
                        pass    
        if reaction.emoji == "⏪":
            if reaction.message.author.id == "533372604350988299":
                if not user.bot:	
                    embed=discord.Embed(
                        color=user.color)				
                    embed.set_author(name='Member Navigation')
                    embed.add_field(name='Member Commands 👨‍👩‍👧‍👧', value='Show you the Member Commands', inline='False')
                    embed.add_field(name='Reddit Commands  🔥', value='Open the Reddit Help Menu', inline='False')
                    embed.add_field(name='Info Commands 📜', value='Open the Info Help Menu', inline='False')
                    embed.add_field(name='Tenor Commands 📽', value='Open the Tenor Help Menu', inline='False')
                    for current_server in nsfw['data']:
                        if current_server['id'] == reaction.message.server.id:
                            channel = ' '.join(current_server['channelid'])
                            if channel == reaction.message.channel.id:
                                embed.add_field(name='NSFW Commands 💦', value='Shows you the NSFW Command Navigation', inline='False')
                    embed.add_field(name='Calculator Commands 🔢', value='Open the Calculator Menu', inline='False') 
                    embed.add_field(name='Back  ⏪ ', value='Back to the Navigation', inline='False')
                    embed.add_field(name='Close ❎', value='Close the Help Menu', inline='False')
                    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                    embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await self.client.edit_message(reaction.message, embed=embed)	 
                    try:
                        await self.client.remove_reaction(reaction.message, "⏪", user)  
                    except Exception as error:
                        pass				
########################################################################################################################
    async def on_message(self, message):
        if not message.author.bot: 
            if self.client.user in message.mentions:
                    if not message.author.id in dev_list:
                        if message.author.server_permissions.administrator ==True:
                            author=message.author
                            embed=discord.Embed(
                                color=ctx.message.author.top_role.color)
                            embed.set_author(name='Admin help Menu')
                            embed.add_field(name='nl!admin (Only for Server Admin´s)', value='Show all Admin commands', inline='False')
                            embed.add_field(name='nl!member (For all Server Members)', value='Show all Member commands', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')					
                            embed.set_footer(text='Message was requested by {}'.format(message.author), icon_url=message.author.avatar_url)
                            embed.timestamp = datetime.utcnow()
                            await self.client.delete_message(message)
                            msg1 = await self.client.send_message(message.channel, embed=embed)
                        if not message.author.server_permissions.administrator ==True:
                            with open('nsfw.json', encoding='utf-8') as f:
                                nsfw = json.load(f)		
                            author=ctx.message.author
                            embed=discord.Embed(
                                color=ctx.message.author.top_role.color)
                            embed.set_author(name='Member Navigation')
                            embed.add_field(name='Member Commands 👨‍👩‍👧‍👧', value='Show you the Member Commands', inline='False')
                            embed.add_field(name='Reddit Commands  🔥', value='Open the Reddit Help Menu', inline='False')
                            embed.add_field(name='Info Commands 📜', value='Open the Info Help Menu', inline='False')
                            embed.add_field(name='Tenor Commands 📽', value='Open the Tenor Help Menu', inline='False')
                            for current_server in nsfw['data']:
                                if current_server['id'] == ctx.message.server.id:
                                    channel = ' '.join(current_server['channelid'])
                                    if channel == ctx.message.channel.id:
                                        embed.add_field(name='NSFW Commands 💦', value='Shows you the NSFW Command Navigation', inline='False')
                            embed.add_field(name='Calculator Commands 🔢', value='Open the Calculator Menu', inline='False')
                            embed.add_field(name='Back  ⏪ ', value='Back to the Navigation', inline='False')
                            embed.add_field(name='Close ❎', value='Close the Help Menu', inline='False')
                            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')			
                            embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                            embed.timestamp = datetime.utcnow()
                            msg = await self.client.send_message(ctx.message.channel, embed=embed)
                            await self.client.add_reaction(msg, "👨‍👩‍👧‍👧")
                            await self.client.add_reaction(msg, "🔥")
                            await self.client.add_reaction(msg, "📜")
                            await self.client.add_reaction(msg, "📽")
                            for current_server in nsfw['data']:
                                if current_server['id'] == ctx.message.server.id:
                                    channel = ' '.join(current_server['channelid'])
                                    if channel == ctx.message.channel.id:
                                        await self.client.add_reaction(msg, "💦")
                            await self.client.add_reaction(msg, "🔢")
                            await self.client.add_reaction(msg, "⏪")
                            await self.client.add_reaction(msg, "❎")
                    if message.author.id in dev_list:
                        author=message.author
                        embed=discord.Embed(
                            color=message.author.top_role.color)
                        embed.set_author(name='Neko Dev help menu')
                        embed.add_field(name='nl!owner (Only for the Bot Owner)', value='Show all Bot Owner commands', inline='False')
                        embed.add_field(name='nl!admin (Only for Server Admin´s)', value='Show all Admin commands', inline='False')
                        embed.add_field(name='nl!member (For all Server Members)', value='Show all Member commands', inline='False')
                        embed.add_field(name='nl!dev (Only for the Bot Devs)', value='Show all Bot Developer commands.', inline='False')
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/560579412333166612/561190692999921684/Neko_Glitch.gif')					
                        embed.set_footer(text='Message was requested by {}'.format(message.author), icon_url=message.author.avatar_url)
                        embed.timestamp = datetime.utcnow()
                        await self.client.delete_message(message)
                        msg1 = await self.client.send_message(message.channel, embed=embed)
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################



		
def setup(client):
    client.add_cog(help1(client))