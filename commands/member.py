import discord
from discord.ext import commands 
import asyncio
import random
from datetime import datetime
import pyfiglet
from pyfiglet import figlet_format, FontNotFound
import sys
import praw
import json
import os

os.chdir(r'/home/pi/Nellie/commands/data')

if os.path.isfile("joinrole.json"):
    with open('joinrole.json', encoding='utf-8') as f:
        onjoin = json.load(f)
else:
    onjoin = {}
    onjoin['server'] = []
    with open('joinrole.json','w+') as f:
        json.dump(onjoin , f, indent=4)	
		
client = commands.Bot(command_prefix='nl!')	

reddit = praw.Reddit(client_id='CFfgp9jESrgbLA',
                     client_secret='HZhSLIsgRMlgP379vA_7YNHQdaU',
                     user_agent='windows:com:Neko Public:reddit.3.22.0(by /u/<MuffinAmor88919>)')

botcolor = 0x00ffff

client.remove_command('help')

dev_id = ['474947907913515019', '486988989262462991']

pass_list = ['474947907913515019']

def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "346785898576216064", "408043714854780958"]

    return commands.check(predicate)

bot_list = ['533372604350988299', '547124033410564116', '526546384372105231']

class member:
    def __init__(self, client):
        self.client = client
 ########################################################################################################################
    @client.command(pass_context = True)
    async def say(self, ctx, *args):
        if not ctx.message.author.bot:
            if ctx.message.author.server_permissions.administrator ==True:
                msg = ' '.join(args)
                await self.client.say(msg)
            if ctx.message.author.id == '474947907913515019':
                msg = ' '.join(args)
                await self.client.say(msg)
            else:
                if "@everyone" in ctx.message.content:
                    msg = await self.client.say("`@everyone` mentions about that function are not allowed.") 
                if "@here" in ctx.message.content:
                    msg = await self.client.say("`@here` mentions about that function are not allowed.") 
                if "http" in ctx.message.content:
                    msg = await self.client.say("`links` about that function are not allowed.") 
                else:
                    msg = ' '.join(args)
                    await self.client.say(msg)
########################################################################################################################
    @client.command(pass_context = True)
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def hack(self, ctx, member: discord.Member):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            embed0 = discord.Embed(title='Hacking {0} now...'.format(member.name), color=ctx.message.author.top_role.color)
            embed1 = discord.Embed(title='Finding discord login...', color=ctx.message.author.top_role.color)
            embed2 = discord.Embed(title='Found:',description='**Email:** `{0}***@gmail.com`\n' '**Password:** `********`'.format(member.name), color=ctx.message.author.top_role.color)
            embed3 = discord.Embed(title='Fetching DMs', color=ctx.message.author.top_role.color)
            embed4 = discord.Embed(title='Listing most common words...', color=ctx.message.author.top_role.color)
            embed5 = discord.Embed(title='Injecting virus into discriminator {0}'.format(member.discriminator), color=ctx.message.author.top_role.color)
            embed6 = discord.Embed(title='Virus injected', color=ctx.message.author.top_role.color)
            embed7 = discord.Embed(title='Finding IP adress', color=ctx.message.author.top_role.color)
            embed8 = discord.Embed(title='Spamming email...', color=ctx.message.author.top_role.color)
            embed9 = discord.Embed(title='Selling data to facebook...', color=ctx.message.author.top_role.color)
            embed10 = discord.Embed(title='Finished hacking {0}'.format(member.name), color=ctx.message.author.top_role.color)
            hack = await self.client.say(embed=embed0)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed1)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed2)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed3)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed4)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed5)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed6)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed7)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed8)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed9)
            await asyncio.sleep(2)
            await self.client.edit_message(hack, embed=embed10)
########################################################################################################################		
    @client.command(pass_context=True)
    async def whisper(self, ctx, member: discord.Member=None, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            mesg = ' '.join(args)
            member = member or ctx.message.author
            server = ctx.message.server
            msg = ("{0} send you a whisper: {1} " .format(ctx.message.author, mesg))
            msg2 = ("the whisper has send succesfully to {}".format(member.mention))
            await self.client.send_message(member, msg)
            await self.client.send_message(ctx.message.author, msg2)
########################################################################################################################	
    @client.command(pass_context = True)
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def support(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            server1 = self.client.get_server('382290709249785857')
            channel = discord.utils.get(server1.channels, name="welcome_and_goodbye", type=discord.ChannelType.text)
            invitelinknew = await self.client.create_invite(destination = channel, xkcd = True, max_age=600)
            embed =discord.Embed(color=ctx.message.author.top_role.color)
            embed.add_field(name="<:Neko_Logo:549531102117625866>Support Server Invite Link<:Neko_Logo:549531102117625866>", value="[Do you need help? Click me!]({0})".format(invitelinknew))
            embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await self.client.send_message(ctx.message.channel, embed=embed)
########################################################################################################################
    @client.command(pass_context=True)
    async def invite(self, ctx, age:int):
        if not ctx.message.author.bot:
            invitelinknew = await self.client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100, max_age=age)
            embed =discord.Embed(color=ctx.message.author.top_role.color)
            embed.add_field(name="Discord Invite Link", value=invitelinknew)
            embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await self.client.send_message(ctx.message.channel, embed=embed)
            await asyncio.sleep(age)
            await self.client.delete_message(msg)
########################################################################################################################			
    @client.command(pass_context=True)
    async def custominvite(self, ctx, channel:discord.Channel, age:int, uses:int):
        if not ctx.message.author.bot:
            invitelinknew = await self.client.create_invite(destination = channel, xkcd = True, max_uses = 100)
            embed =discord.Embed(color=ctx.message.author.top_role.color)
            embed.add_field(name="Discord Invite Link", value=invitelinknew)
            embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await self.client.send_message(ctx.message.channel, embed=embed)
            await asyncio.sleep(age)
            await self.client.delete_message(msg)
########################################################################################################################			
    @client.command(pass_context=True)
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def tempchannel(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            time = int(600)
            msg = ' '.join(args)
            temp = await self.client.create_channel(ctx.message.server, name=msg, type=discord.ChannelType.text)
            await self.client.send_message(temp, "{0} has create a Tempchannel for {1} seconds".format(ctx.message.author.mention, time))
            await asyncio.sleep(time)
            await self.client.delete_channel(temp)
########################################################################################################################				   
    @client.command(pass_context=True)
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def tempvoice(self, ctx, *args):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            time = int(600)
            msg = ' '.join(args)
            temp = await self.client.create_channel(ctx.message.server, name=msg, type=discord.ChannelType.voice)
            await asyncio.sleep(time)
            await self.client.delete_channel(temp)
########################################################################################################################
    @client.command(pass_context=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def one_to_twenty(self, ctx, number=20):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            try:
                arg = random.randint(1, int(number))
                arg2 = random.randint(1, int(number))
                arg3 = random.randint(1, int(number))
                arg4 = random.randint(1, int(number))
                arg5 = random.randint(1, int(number))
                arg6 = random.randint(1, int(number))
            except ValueError:
                await self.client.say("Invalid number")
            else:
                msg =await self.client.say("ich wähle aus den Zahlen von 2 bis {0}".format(number)) 
                await asyncio.sleep(5)
                msg1 = await self.client.say("dieeee {0} :thinking:".format((str(arg))))
                await asyncio.sleep(9)
                msg2 = await self.client.say("und die {0} :thinking: ".format((str(arg2))))
                await asyncio.sleep(2)
                msg3 = await self.client.say("eventuell noch die {0} :thinking: ".format((str(arg3))))
                await asyncio.sleep(7)
                msg4 = await self.client.say("ach und die {0} gefällt mir auch noch! :thinking: ".format((str(arg4))))
                await asyncio.sleep(3)
                msg5 = await self.client.say("und zu guter letzt die  {0} :thinking: ".format((str(arg5))))
                await asyncio.sleep(2)
                msg6 = await self.client.say("Hoffentlich hast du nicht drauf gewettet! weil ich nehme noch die {0} dazu".format((str(arg6))))
                await asyncio.sleep(30)
                await self.client.delete_message(msg)
                await self.client.delete_message(msg1)
                await self.client.delete_message(msg2)
                await self.client.delete_message(msg3)
                await self.client.delete_message(msg4)
                await self.client.delete_message(msg5)
                await self.client.delete_message(msg6)
########################################################################################################################		
    @client.command(pass_context=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def serverinfo(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            server_id = ctx.message.server.id			
            for current_server in onjoin['server']:
                if current_server['id'] == server_id:
                    server = ctx.message.server
                    server_info1 = (ctx.message.timestamp - server.created_at).days
                    rl = list(role.mention for role in server.roles if not role.name == "@everyone")
                    roles = '  |  '.join(rl)
                    el = list(emojis.name for emojis in ctx.message.server.emojis)
                    Bot = list(member.bot for member in ctx.message.server.members if member.bot is True) 
                    user = list(member.bot for member in ctx.message.server.members if member.bot is False)
                    embed1=discord.Embed(
                        color=ctx.message.author.top_role.color)
                    embed1.add_field(name='<:Neko_Logo:549531102117625866>__Server Info__<:Neko_Logo:549531102117625866>', value='** **', inline=False)
                    embed1.add_field(name='Name:', value='{}'.format(server.name), inline=True)
                    embed1.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                    embed1.add_field(name='Region:', value='{}'.format(server.region), inline=True)
                    embed1.add_field(name='AFK Channel:', value='{0} ({1} seconds)'.format(server.afk_channel, server.afk_timeout), inline=True)
                    embed1.add_field(name='Membercount:', value='{} members'.format(server.member_count), inline=True)
                    embed1.add_field(name='Botcount:', value='{} Bots'.format(str(len(Bot))), inline=True) 
                    embed1.add_field(name='Humancount:', value='{} users'.format(str(len(user))), inline=True)
                    embed1.add_field(name='Large Server:', value='{} (250+ member)'.format(server.large), inline=True)
                    embed1.add_field(name='Serverowner:', value='{}'.format(server.owner), inline=True)
                    embed1.add_field(name='Verifylevel:', value='{} '.format(server.verification_level), inline=True)
                    embed1.add_field(name='Serverroles:', value='{} '.format(roles), inline=True)
                    embed1.add_field(name='Created at:', value='{}'.format("{} ({} days ago!)".format(server.created_at.strftime("%d. %b. %Y %H:%M"), server_info1)), inline=False)
                    embed1.set_thumbnail(url="{0}".format(server.icon_url))
                    embed1.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                    embed1.timestamp = datetime.utcnow()
                    break
            else:
                server = ctx.message.server
                server_info1 = (ctx.message.timestamp - server.created_at).days
                rl = list(role.name for role in server.roles if not role.name == "@everyone")
                roles = '  |  '.join(rl)
                el = list(emojis.name for emojis in ctx.message.server.emojis)
                Bot = list(member.bot for member in ctx.message.server.members if member.bot is True) 
                user = list(member.bot for member in ctx.message.server.members if member.bot is False)
                embed1=discord.Embed(
                    color=ctx.message.author.top_role.color)
                embed1.add_field(name='<:Neko_Logo:549531102117625866>__Server Info__<:Neko_Logo:549531102117625866>', value='** **', inline=False)
                embed1.add_field(name='Name:', value='{}'.format(server.name), inline=True)
                embed1.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                embed1.add_field(name='Region:', value='{}'.format(server.region), inline=True)
                embed1.add_field(name='AFK Channel:', value='{0} ({1} seconds)'.format(server.afk_channel, server.afk_timeout), inline=True)
                embed1.add_field(name='Membercount:', value='{} members'.format(server.member_count), inline=True)
                embed1.add_field(name='Botcount:', value='{} Bots'.format(str(len(Bot))), inline=True) 
                embed1.add_field(name='Humancount:', value='{} users'.format(str(len(user))), inline=True)
                embed1.add_field(name='Large Server:', value='{} (250+ member)'.format(server.large), inline=True)
                embed1.add_field(name='Serverowner:', value='{}'.format(server.owner), inline=True)
                embed1.add_field(name='On Join Role:', value="None", inline=True)
                embed1.add_field(name='Verifylevel:', value='{} '.format(server.verification_level), inline=True)
                embed1.add_field(name='Serverroles:', value='{} '.format(roles), inline=True)
                embed1.add_field(name='Created at:', value='{}'.format("{} ({} days ago!)".format(server.created_at.strftime("%d. %b. %Y %H:%M"), server_info1)), inline=False)
                embed1.set_thumbnail(url="{0}".format(server.icon_url))
                embed1.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed1.timestamp = datetime.utcnow()
            try: 
                msg1 = await self.client.send_message(ctx.message.channel, embed=embed1)
                await asyncio.sleep(120)
                await self.client.delete_message(msg1)
            except:
                server = ctx.message.server
                server_info1 = (ctx.message.timestamp - server.created_at).days
                Bot = list(member.bot for member in ctx.message.server.members if member.bot is True) 
                user = list(member.bot for member in ctx.message.server.members if member.bot is False)
                embed=discord.Embed(
                    color=ctx.message.author.top_role.color)
                embed.add_field(name='<:Neko_Logo:549531102117625866>__Server Info__<:Neko_Logo:549531102117625866>', value='** **', inline=False)
                embed.add_field(name='Name:', value='{}'.format(server.name), inline=True)
                embed.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                embed.add_field(name='Region:', value='{}'.format(server.region), inline=True)
                embed.add_field(name='AFK Channel:', value='{0} ({1} seconds)'.format(server.afk_channel, server.afk_timeout), inline=True)
                embed.add_field(name='Membercount:', value='{} members'.format(server.member_count), inline=True)
                embed.add_field(name='Botcount:', value='{} Bots'.format(str(len(Bot))), inline=True) 
                embed.add_field(name='Humancount:', value='{} users'.format(str(len(user))), inline=True)
                embed.add_field(name='Large Server:', value='{} (250+ member)'.format(server.large), inline=True)
                embed.add_field(name='Serverowner:', value='{}'.format(server.owner), inline=True)
                embed.add_field(name='Verifylevel:', value='{} '.format(server.verification_level), inline=True)
                embed.add_field(name='Created at:', value='{}'.format("{} ({} days ago!)".format(server.created_at.strftime("%d. %b. %Y %H:%M"), server_info1)), inline=  False)
                embed.set_thumbnail(url="{0}".format(server.icon_url))
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                msg = await self.client.send_message(ctx.message.channel, embed=embed)
########################################################################################################################
    @client.command(pass_context=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def dbl(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            msg = await self.client.say("https://discordbots.org/bot/533372604350988299")	
########################################################################################################################		
    @client.command(pass_context=True)
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def finddbl(self, ctx, member:discord.Member):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            member = member
            msg = await self.client.say("https://discordbots.org/bot/{0}".format(member.id))
########################################################################################################################		
    @client.command(pass_context=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def roleinfo(self, ctx, role: discord.Role):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            role_info1 = (ctx.message.timestamp - role.created_at).days
            l = list(permi for permi, value in role.permissions if str(value)== 'True')
            i = '\n📍 '.join(l)
            embed=discord.Embed(color=role.color)
            embed.add_field(name='__Role Info__', value='** **', inline=False)
            embed.add_field(name='Rolename:', value='{0} | {1}'.format(role.name, role.mention), inline=False)
            embed.add_field(name='Role ID:', value='{0}'.format(role.id), inline=True)
            embed.add_field(name='Role color:', value='{0}'.format(role.color), inline=True)
            embed.add_field(name='Role shows seperat from online?:', value='{0}'.format(role.hoist), inline=True)
            embed.add_field(name='Role position:', value='{0}'.format(role.position), inline=True)
            embed.add_field(name='Role mentionable:', value='{0}'.format(role.mentionable), inline=True)
            embed.add_field(name='Role permissions:', value='📍 {0}'.format(i), inline=False)
            embed.add_field(name='Created at:', value='{}'.format("{} ({} days ago!)".format(role.created_at.strftime("%d. %b. %Y %H:%M"), role_info1)), inline=False)
            author = ctx.message.author
            embed.set_footer(text='Message was requested by {0}'.format(author), icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await self.client.send_message(ctx.message.channel, embed=embed)
########################################################################################################################
    @client.command(pass_context=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def channelinfo(self, ctx, channel:discord.Channel):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            channel_info1 = (ctx.message.timestamp - channel.created_at).days
            embed = discord.Embed(color=ctx.message.author.top_role.color)
            embed.add_field(name='__Channel Info__', value='** **', inline=False)
            embed.add_field(name='Name:', value='{}'.format(channel.name), inline=True)
            embed.add_field(name='Channel ID:', value='{}'.format(channel.id), inline=True)
            embed.add_field(name='Type:', value='{}'.format(channel.type), inline=True)
            embed.add_field(name='Bitrate:', value='{}'.format(channel.bitrate), inline=True)
            embed.add_field(name='Topic:', value='{}'.format(channel.topic), inline=True)
            embed.add_field(name='User Limit:', value='{}'.format(channel.user_limit), inline=True)
            embed.add_field(name='Voice Members:', value='{}'.format(channel.voice_members), inline=False)
            embed.add_field(name='Created at:', value='{}'.format("{} ({} days ago!)".format(channel.created_at.strftime("%d. %b. %Y %H:%M"), channel_info1)), inline=False)
            author = ctx.message.author
            embed.set_footer(text='Message was requested by: {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.timestamp = datetime.utcnow()
            msg = await self.client.say(embed=embed)
########################################################################################################################			
    @client.command(pass_context=True)
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def callsupport(self, ctx, *args):	
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if args:
                user = ctx.message.author
                server1 = self.client.get_server(user.server.id)
                inv = await self.client.invites_from(server1)
                server2 = self.client.get_server('575378478573289472')
                channel = discord.utils.get(server2.channels, name="support_calls", type=discord.ChannelType.text)
                reason = ' '.join(args)
                for invites in inv:
                    embed = discord.Embed(title="Support Call".format(user.name), color=user.top_role.color)
                    embed.add_field(name="Author", value=user, inline=True)
                    embed.add_field(name="Author ID", value=user.id, inline=True)
                    embed.add_field(name="Server", value=user.server, inline=True)
                    embed.add_field(name="Server ID", value=user.server.id, inline=True)
                    embed.add_field(name="Reason", value=reason, inline=True)
                    embed.add_field(name="Invite", value=invites, inline=False)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                    await self.client.send_message(channel, embed=embed)
                    break
                embed0 = discord.Embed(title="You have created a ticket successfully!!".format(user.name), color=user.top_role.color)
                embed0.add_field(name="Author", value=user, inline=True)
                embed0.add_field(name="Author ID", value=user.id, inline=True)
                embed0.add_field(name="Server", value=user.server, inline=True)
                embed0.add_field(name="Server ID", value=user.server.id, inline=True)
                embed0.add_field(name="Reason", value=reason, inline=True)
                embed0.add_field(name="Info:", value="A supporter from the Neko Coding Support Server joins as soon as possible your Server.\nReasonfields filled with Junk get ignored.", inline=False)
                embed0.set_thumbnail(url=user.avatar_url)
                embed0.set_footer(text='Message was requested by {}'.format(user), icon_url=user.avatar_url)
                msg2 = await self.client.send_message(ctx.message.channel, embed=embed0)
            if not args:
                msg = await self.client.say("Please provide a reason for calling the Support.\nAbuse this command follows consequences for the whole Server. (Bot removing, Botblocklist etc.)")
				
    @commands.command(pass_context=True)
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def tableflip(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            x = await self.client.say('┬─┬ノ( º _ ºノ)')
            await asyncio.sleep(1)
            await self.client.edit_message(x, '(°-°)// ┬─┬')
            await asyncio.sleep(1)
            await self.client.edit_message(x, '(╯°□°)╯    ]')
            await asyncio.sleep(0.2)
            await self.client.edit_message(x, '(╯°□°)╯  ︵  ┻━┻')
		
    @commands.command(pass_context=True)
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def big(self, ctx, *, text):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            await self.client.say("```fix\n" + figlet_format(text, font="big") + "```")
		
    @commands.command(pass_context=True)
    async def duel(self, ctx, user: discord.User=None):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if(user):
                x = str(ctx.message.author.mention)
                xx = str(user.mention)
                z = await self.client.say("{}".format(x) + " duels " + "{}".format(xx))
                await asyncio.sleep(1.5)
                await self.client.edit_message(z, '⚔ Dueling.')
                await asyncio.sleep(0.5)
                await self.client.edit_message(z, '⚔ Dueling..')
                await asyncio.sleep(0.5)
                await self.client.edit_message(z, '⚔ Dueling...')
                await asyncio.sleep(0.5)
                l = random.randint(1, 2)
                if(l == 1):
                    await self.client.edit_message(z, '{}'.format(xx) + ' has won!')
                else:
                    await self.client.edit_message(z, '{}'.format(x) + ' has won!')
            else:
                await self.client.say("You can't duel no one! Tag someone!")
				
    @client.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def meme(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            await self.client.send_typing(ctx.message.channel)
            memes_submissions = reddit.subreddit('dankmemes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title=submission.title, color=botcolor)
            embed.set_image(url=submission.url)
            embed.set_footer(text='reddit.com')
            embed.timestamp = datetime.utcnow()
            await self.client.say(embed=embed)
			
    @client.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cat(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            await self.client.send_typing(ctx.message.channel)
            memes_submissions = reddit.subreddit('cat').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title=submission.title, color=botcolor)
            embed.set_image(url=submission.url)
            embed.set_footer(text='reddit.com')
            embed.timestamp = datetime.utcnow()
            await self.client.say(embed=embed)
			
    @client.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def dog(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            await self.client.send_typing(ctx.message.channel)
            memes_submissions = reddit.subreddit('dog').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title=submission.title, color=botcolor)
            embed.set_image(url=submission.url)
            embed.set_footer(text='reddit.com')
            embed.timestamp = datetime.utcnow()
            await self.client.say(embed=embed)
			
    @client.command(pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def anime(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            await self.client.send_typing(ctx.message.channel)
            memes_submissions = reddit.subreddit('animememes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            embed = discord.Embed(title=submission.title, color=botcolor)
            embed.set_image(url=submission.url)
            embed.set_footer(text='reddit.com')
            embed.timestamp = datetime.utcnow()
            await self.client.say(embed=embed)
			
    @client.command(pass_context=True)
    async def emojis1(self, ctx):
        server = ctx.message.server
        emojis = [str(x) for x in server.emojis]
        await self.client.say("".join(emojis))
        await self.client.delete_message(ctx.message)
		
    @client.command(pass_context=True)
    async def plus(self, ctx, sum1:int, sum2:int):
        await self.client.say(sum1+sum2)



    @client.command(pass_context=True)
    async def subtract(self, ctx, sum1:int, sum2:int):
        await self.client.say(sum1-sum2)



    @client.command(pass_context=True)
    async def multiply(self, ctx, sum1:int, sum2:int):
        await self.client.say(sum1*sum2)
	
	
	

    @client.command(pass_context=True)
    async def divide(self, ctx, sum1:int, sum2:int):
        await self.client.say(sum1/sum2)
	

    @client.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def weeb(self, ctx, member:discord.Member, number=100):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            if member.id == "474947907913515019":
                await self.client.say("My master is a weeb")
            else:
                try:
                    arg = random.randint(1, int(number))
                except ValueError:
                    await self.client.say("Invalid number")
                else:
                    await self.client.say("{0} is a {1}% weeb".format(member.name, (str(arg))))

    @client.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sortname(self, ctx, member:discord.Member):  
        sortedname = ' '.join(sorted(member.name))
        msg = await self.client.say(sortedname)
		
	
    @client.command(pass_context = True)
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def smile(self, ctx):
        if ctx.message.author.bot:
            pass
        if not ctx.message.author.bot:
            x = await self.client.say(':smile:')
            await asyncio.sleep(1)
            await self.client.edit_message(x, ':smiley:')
            await asyncio.sleep(1)
            await self.client.edit_message(x, ':smile:')
            await asyncio.sleep(1)
            await self.client.edit_message(x, ':smiley:')
			
    @client.command(pass_context = True)
    async def sfa(self, ctx):
        await self.client.say("hi")  
	
    @client.command(pass_context = True)
    @is_vale()
    async def emoteim(self, ctx):	
        with open(r'C:\Users\Niko\Desktop\neko.png', "rb") as image:
                image_byte = image.read()
                emoji = await self.client.create_custom_emoji(ctx.message.server, name="Neko", image=image_byte)
	
def setup(client):
    client.add_cog(member(client))