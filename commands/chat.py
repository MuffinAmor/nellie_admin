import discord
from discord.ext import commands
import asyncio
import sys
import random
from discord.ext.commands import CommandNotFound
from datetime import datetime
import json
import os


os.chdir(r'/home/pi/bot/Global/commands/data') #C:\Users\Desktop\Discord Neko Bot lite\commands\data


if os.path.isfile("ban.json"):
    with open('ban.json', encoding='utf-8') as f:
        report = json.load(f)
else:
    report = {}
    report['users'] = []
    with open('ban.json', 'w') as f:
        json.dump(report, f, indent=4)


if os.path.isfile("chat.json"):	  
    with open('chat.json', encoding='utf-8') as w:
        gc = json.load(w)
else:
    gc = {}
    gc['global'] = []
    with open('chat.json', 'w') as f:
        json.dump(gc, f, indent=4)


if os.path.isfile("wordblocker.json"):	 	
    with open('wordblocker.json', encoding='utf-8') as m:
        blocked = json.load(m)
else:
    blocked = {}
    blocked['global'] = []
    with open('wordblocker.json', 'w') as f:
        json.dump(blocked, f, indent=4)
		
if os.path.isfile("rank.json"):	 	
    with open('rank.json', encoding='utf-8') as r:
        rank = json.load(r)
else:
    rank = {}
    rank['vips'] = []
    rank['vips'].append({
    'id': [""]
    })
    print("Datenbankfehler in der VIPS- Patition. rank.json!!!!!!!!")
    rank['dev'] = []
    rank['dev'].append({
    'id': ["474947907913515019"]
    })
    print("Datenbankfehler in der DEV- Patition. rank.json!!!!!!!!\n")
    rank['mod'] = []
    rank['mod'].append({
    'id': [""]
    })
    print("Datenbankfehler in der MOD- Patition. rank.json!!!!!!!!\n")
    rank['vip'] = []
    rank['vip'].append({
    'id': [""]
    })
    print("Datenbankfehler in der VIP- Patition. rank.json!!!!!!!!\n")
    rank['pmod'] = []
    rank['pmod'].append({
    'id': [""]
    })
    print("Datenbankfehler in der PMOD- Patition. rank.json!!!!!!!!\n")
    rank['lmod'] = []
    rank['lmod'].append({
    'id': [""]
    })
    print("Datenbankfehler in der lMOD- Patition. rank.json!!!!!!!!\n")
    rank['partner'] = []
    rank['partner'].append({
    'id': [""]
    })
    print("Datenbankfehler in der Partner- Patition. rank.json!!!!!!!!")
    with open('rank.json', 'w') as r:
        json.dump(rank, r, indent=4)
	
		
		
		
bot = commands.Bot(command_prefix='ng!')

botcolor = 0x00ff06

bot.remove_command('help')


VIP_List = [406479076048633857,361889776003055646, 517724360988164116 ,310514834112249866, 518648895883051009]

MOD_List = [517724360988164116, 406479076048633857, 441272343290183689]

def is_vale():
    def predicate(ctx):
        return ctx.author.id in [474947907913515019]

    return commands.check(predicate)


def is_dev():
    def predicate(ctx):
        for a in rank['dev']:
            return ctx.author.id in a['id']

    return commands.check(predicate)

def is_mod():
    def predicate(ctx):
        for a in rank['mod']:
            return str(ctx.author.id) in a['id']

    return commands.check(predicate)

def is_lmod():
    def predicate(ctx):
        for a in rank['lmod']:
            return str(ctx.author.id) in a['id']

    return commands.check(predicate)



class chat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
########################################################################################################################
        with open('users.json', 'r') as f:
            self.users = json.load(f)

    def lvl_up(self, autohr_id):
        cur_exp = self.users[autohr_id]['exp']
        cur_lvl = self.users[autohr_id]['level']
        end_lvl = int(cur_exp ** (1/3))

        if cur_lvl < end_lvl:
            self.users[autohr_id]['level'] += 1
            with open('users.json', 'w') as f:
                json.dump(self.users, f, indent=4)
            return True
        else:
            return False






    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot==False:    
            server = message.guild
            msg = message.content
            channel = message.channel
            author_id = str(message.author.id)
            for b in rank['dev']:
                if str(message.author.id) in b['id']:
                    dev = "yes"
                else:
                    dev = ""
            for c in rank['mod']:
                if str(message.author.id) in c['id']:
                    mod = "yes"
                else:
                    mod = ""
            for current_word in blocked['global']:
                blacklist = ' '.join(current_word['words'])
                if msg in blacklist:
                    blacklist = "yes"
                else:
                    blacklist = ""
            for a in rank['vips']:
                if str(message.guild.id) in a['id']:
                    vips = "yes"
                else:
                    vips = ""
            for d in rank['vip']:
                if str(message.author.id) in d['id']:
                    vip = "yes"
                else:
                    vip = ""
            for e in rank['pmod']:
                if str(message.author.id) in e['id']:
                    pmod = "yes"
                else:
                    pmod = ""
            for f in rank['lmod']:
                if str(message.author.id) in f['id']:
                    lmod = "yes"
                else:
                    lmod = ""            
            for user in report['users']:
                if str(message.author.id) in str(user['id']):
                    blocks = "yes"
                else:
                    blocks = ""
            for g in rank['partner']:
                if str(message.guild.id) in g['id']:
                    partner = "yes"
                else:
                    partner = ""
            for servers in self.bot.guilds:
                for current_global in gc['global']:
                    if server.id == current_global['id']:
                        channelid = ' '.join(current_global['channelid'])
                        numid1 = int(channelid)
                        if numid1 == message.channel.id:
                            for current_global in gc['global']:
                                if str(servers.id) in str(current_global['id']):
                                    channelid = ' '.join(current_global['channelid'])		
                                    numid2 = int(channelid)	
                                    channel2 = self.bot.get_channel(numid2)		
                                    if channel2:
                                        if not author_id in self.users:
                                            self.users[author_id] = {}
                                            self.users[author_id]['level'] = 1
                                            self.users[author_id]['exp'] = 0
                                        self.users[author_id]['exp'] += 1
                                        with open('users.json', 'w') as f:
                                            json.dump(self.users, f, indent=4)
                                        if self.lvl_up(author_id):
                                            try:
                                                channel = self.bot.get_channel(613457084272607316)
                                                embed = discord.Embed(color=message.author.color)
                                                embed.add_field(name=':tada: LEVEL UP :tada:', value='{0} is now level **{1}**\nThe User have **{2}** EXP'.format(message.author.name, get_lvl(author_id), get_xp(author_id)))
                                                embed.set_footer(text='Level Up', icon_url=message.author.avatar_url)
                                                embed.timestamp=datetime.now()
                                                await channel.send(embed=embed)
                                            except Exception as error:
                                                print(error)
                                        break
                            break
                break     
            if message.author.bot==False:				
                if dev == "yes":
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2:
                                                try:
                                                    try:
                                                        ins = self.bot.get_guild(382290709249785857)
                                                        inv = await ins.invites()
                                                        for invites in inv:
                                                            invite = invites.url
                                                            break
                                                    except:
                                                        invite = ""
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(
                                                        color=message.author.color)
                                                    embed.add_field(name='<:Neko_Logo:549531102117625866>Developer | {0} | Level {1}<:Neko_Logo:549531102117625866>'.format(message.author.name, level), value="{}\n[Supportserver]({})".format(msg, invite), inline=False)
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text='Network Developer', icon_url=message.author.avatar_url)
                                                    await channel2.send(embed=embed)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break   
                elif lmod == "yes":
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2: 
                                                try:
                                                    try:
                                                        ins = self.bot.get_guild(382290709249785857)
                                                        inv = await ins.invites()
                                                        for invites in inv:
                                                            invite = invites.url
                                                    except:
                                                        invite = ""
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(title='🛡 LMOD | {0} | Level {1} 🛡'.format(message.author.name, level), description="{}\n[Supportserver]({})".format(msg, invite), color=message.author.color)
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text="Global Chat Moderator", icon_url=message.author. avatar_url)
                                                    await channel2.send(embed=embed)
                                                    await asyncio.sleep(0.5)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break      

                elif mod == "yes":
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2:  
                                                try:
                                                    try:
                                                        ins = self.bot.get_guild(382290709249785857)
                                                        inv = await ins.invites()
                                                        for invites in inv:
                                                            invite = invites.url
                                                    except:
                                                        invite = ""
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(title='🛡Moderator | {0} | Level {1}🛡'.format(message.author.name, level), description="{}\n[Supportserver]({})".format(msg, invite), color=0x18bd51)
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text="Global Chat Moderator", icon_url=message.author. avatar_url)
                                                    await channel2.send(embed=embed)
                                                    await asyncio.sleep(0.5)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break      

                elif blocks == "yes":
                    for current_global in gc['global']:
                        if server.id == current_global['id']:
                            channelid = ' '.join(current_global['channelid'])
                            numid1 = int(channelid)
                            if numid1 == message.channel.id:
                                try:
                                    await message.delete()
                                except Exception as error:
                                    pass
                                embed=discord.Embed(title='System Alert', description="Hello {},\nYou are blocked from the Network channel.\nYou can contact the Bot Staff Team to appeal the ban".format(message.author.mention), color=0xff0000)
                                embed.timestamp = datetime.utcnow()
                                embed.set_footer(text=message.author.id, icon_url=message.author.avatar_url)
                                sysmsg = await channel.send(embed=embed)
                                try:
                                    asyncio.sleep(20)
                                    sysmsg.delete()
                                except Exception as error:
                                    pass
                                    return
                elif blacklist == "yes":
                    for current_global in gc['global']:
                        if server.id == current_global['id']:
                            channelid = ' '.join(current_global['channelid'])
                            numid1 = int(channelid)
                            if numid1 == message.channel.id:
                                try:
                                    await message.delete() 
                                except Exception as error:
                                    pass
                                embed=discord.Embed(title='System Alert', description="Hello {},\nA word in your message is blocked from the Global chat.\nYour message is not send".format(message.author.mention), color=0xff0000)
                                embed.timestamp = datetime.utcnow()  
                                embed.set_footer(text=message.author.id, icon_url=message.author.avatar_url)
                                sysmsg = await channel.send(embed=embed)
                                try:
                                    asyncio.sleep(20)
                                    await sysmsg.delete()
                                except Exception as error:
                                    pass
                                return 
                elif pmod == "yes":
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2: 
                                                try:
                                                    try:
                                                        ins = self.bot.get_guild(382290709249785857)
                                                        inv = await ins.invites()
                                                        for invites in inv:
                                                            invite = invites.url
                                                    except:
                                                        invite = ""
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(title='🛡PMOD | {0} | Level {1}🛡'.format(message.author.name, level), description="{}\n[Supportserver]({})".format(msg, invite), color=0x18bd51)
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text="Global Chat Moderator", icon_url=message.author. avatar_url)
                                                    await channel2.send(embed=embed)
                                                    await asyncio.sleep(0.5)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break   
                elif partner == "yes":
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2:
                                                try:
                                                    try:
                                                        if servers.id == 442712922800652289:
                                                            invite = "https://discord.io/pokefuchs"
                                                        else:
                                                            inv = await message.guild.invites()
                                                            for invites in inv:
                                                                invite = invites.url
                                                                break
                                                    except Exception as error:
                                                        invite = "** **"
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(color=0xce2727) 
                                                    embed.add_field(name='💎 {0} 💎 | {1} | Level {2}'.format(message.author.guild, message.author.name, level), value="{}\n[Server Invite]({})".format(msg[0:1000], invite), inline=False)
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text='{}'.format(message.author.id), icon_url=message.author.avatar_url)
                                                    await channel2.send(embed=embed)
                                                    await asyncio.sleep(0.5)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break  
                elif vips == "yes":
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2:
                                                try:
                                                    try:
                                                        inv = await message.guild.invites()
                                                        for invites in inv:
                                                            invite = invites.url
                                                            break
                                                    except Exception as error:
                                                        invite = ""
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(color=message.author.top_role.color) 
                                                    embed.add_field(name='🌟{0}🌟 | {1} | Level {2}'.format(message.author.guild, message.author.name, level), value="{}\n[Server Invite]({})".format(msg[0:500], invite), inline=False)
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text='{}'.format(message.author.id), icon_url=message.author.avatar_url)
                                                    await channel2.send(embed=embed)
                                                    await asyncio.sleep(0.5)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break  
                elif vip =="yes":
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2: 
                                                try:
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(title='🌟VIP | {0} | Level {1}🌟'.format(message.author.name, level), description=msg[0:200], color=message.author.top_role.  color)
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text=message.author.id, icon_url=message.author.avatar_url)
                                                    await channel2.send(embed=embed)
                                                    await asyncio.sleep(0.5)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break  	
                else:
                    for servers in self.bot.guilds:
                        for current_global in gc['global']:
                            if server.id == current_global['id']:
                                channelid = ' '.join(current_global['channelid'])
                                numid1 = int(channelid)
                                if numid1 == message.channel.id:
                                    for current_global in gc['global']:
                                        if str(servers.id) in str(current_global['id']):
                                            channelid = ' '.join(current_global['channelid'])		
                                            numid2 = int(channelid)	
                                            channel2 = self.bot.get_channel(numid2)		
                                            if channel2:
                                                try:
                                                    level = get_lvl(str(message.author.id))
                                                    embed=discord.Embed(title='{0} | {1} | Level {2}'.format(message.author.guild, message.author.name, level), description=msg[0:150], color=message.author.top_role.color) 
                                                    embed.timestamp = datetime.utcnow()
                                                    embed.set_footer(text='{}'.format(message.author.id), icon_url=message.author.avatar_url)
                                                    await channel2.send(embed=embed)
                                                    await asyncio.sleep(0.5)
                                                    try:
                                                        await message.delete()
                                                    except:
                                                        pass
                                                except Exception as error:
                                                    print(error) 
                                                    break  
                if message.author.bot==False:
                    for current_global in gc['global']:
                        if server.id == current_global['id']:
                            channelid = ' '.join(current_global['channelid'])
                            numid1 = int(channelid)
                            if numid1 == message.channel.id:
                                print("{}>>    {}".format(message.author.id, msg))








    @bot.command(pass_context = True, aliases=['rank'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def level(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        try:
            embed = discord.Embed(title="{}'s level stats".format(member.name), color=member.color, timestamp=datetime.now())
            embed.add_field(name='Level', value=get_lvl(str(member.id)))
            embed.add_field(name='EXP', value=get_xp(str(member.id)))
            await ctx.channel.send(embed=embed)
        except KeyError:
            embed = discord.Embed(color=member.color, timestamp=datetime.now())
            embed.add_field(name='{} is not in the Database'.format(member.name), value='** **')
            await ctx.channel.send(embed=embed)








################################################################################################################################################

    @bot.command(pass_context=True)
    @is_mod()
    async def moderation(self, ctx):
        if ctx.author.bot==False: 
            embed=discord.Embed(
                color=ctx.message.author.top_role.color)
            embed.set_author(name='Global Chat Help Menu')
            embed.add_field(name='ng!addrank *id* *rank (mod or pmod)* Lmod only', value='Give a User the Mod Rank', inline='False')
            embed.add_field(name='ng!removerank *id* *rank (mod or pmod)* Lmod only', value='Remove a User from the Mod Rank', inline='False')
            embed.add_field(name='ng!abw *word*', value='Ad a word to the Global Chat', inline='False')
            embed.add_field(name='ng!chatban *userid*', value='Ban a user from the Globalchat', inline='False')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/522437022095245313/546359964101509151/Neko_Logo.png')			
            embed.set_footer(text='Do you need help? http://discord.gg/pqx5Hc6')
            embed.timestamp = datetime.utcnow()
            await ctx.channel.send(embed=embed)


    @commands.command(pass_context = True)
    @is_mod()
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def chatban(self, ctx, *args):
        user_id = ''.join(args)
        reason = "banned"
        if not args:
            msg = await ctx.channel.send("Please provide a reason")
            await asyncio.sleep(10)
            await msg.delete()
            return
        for current_user in report['users']:
            if current_user['id'] == user_id:
                current_user['reasons'].append(reason)
                break
        else:
            report['users'].append({
                'id':user_id,
                'reasons': [reason,]
            })
        with open('ban.json','w+') as f:
            json.dump(report,f, indent=4)
            member = self.bot.get_user_info(user_id)
            channel = self.bot.get_channel(598983182020509697)
            embed = discord.Embed(title="Userban: ***{0}***".format(member.name), color=0xff0000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/560579412333166612/573892323923198002/unknown.png")
            embed.set_footer(text='CHAT BANNED USER')
            embed.timestamp = datetime.utcnow()
            await channel.send(embed=embed)
            embed1 = discord.Embed(description='{0} has been banned.'.format(member.name), color=botcolor)
            await ctx.channel.send(embed=embed1)
            embed2 = discord.Embed(title="Userban: ***{0}***".format(member.name), color=0xff0000)
            embed2.set_image(url="https://cdn.discordapp.com/attachments/560579412333166612/573892323923198002/unknown.png")
            embed2.set_footer(text='CHAT BANNED USER')
            embed2.timestamp = datetime.utcnow()
            for servers in self.bot.guilds:
                for current_global in gc['global']:
                    if current_global['id'] == guild.id:
                        activ = ' '.join(current_global['enable'])
                        if activ == "True":
                            channelid = ' '.join(current_global['channelid'])
                            numid = int(channelid)
                            channel = self.bot.get_channel(numid)
                            if message.channel is channel:
                                for current_global in gc['global']:
                                    if servers.id in current_global['id']:
                                        channelid = ' '.join(current_global['channelid'])
                                        numid = int(channelid)
                                        channel = self.bot.get_channel(numid)
                                        await channel1.send(embed=embed2)
			
    @commands.command(pass_context = True)
    @is_mod()
    async def abw(self, ctx, *word:str):
        if ctx.message.author.bot==False:
            pass
        if not ctx.message.author.bot==False:
            if not word:
                msg = await ctx.channel.send("Please provide a word")
                await asyncio.sleep(10)
                await msg.delete()
                return
            word = ' '.join(word)
            for current_word in blocked['global']:
                current_word['words'].append(word)
                break
            else:
                blocked['global'].append({
                'words': [word, ]
                })
            with open('wordblocker.json','w+') as m:
                json.dump(blocked,m, indent=4)
                await ctx.channel.send("The Word {0} has been added to the Wordblacklist".format(word))
                channel = self.bot.get_channel(598983210340319252) 
                embed = discord.Embed(description='The Word ***{0}*** has been added to the Wordblacklist by {1}'.format(word, ctx.message.author.name), color=botcolor)
                embed.timestamp = datetime.utcnow()
                await channel.send(embed=embed)



    @commands.command(pass_context = True)
    @is_lmod()
    async def addmod(self, ctx, id:int, *ramen):
        if ctx.message.author.bot==False:
            name = ' '.join(ramen)
            if not ramen:
                embed = discord.Embed(description='Please write "mod" or "pmod" to give the user a rank', color=botcolor)
                embed.timestamp = datetime.utcnow()
                await channel.send(embed=embed)
            elif name == "mod":
                for c in rank['mod']:
                    if str(id) in c['id']:
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User **{0}** is allready in the Databank as Mod'.format(user.name), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break                        
                    if not str(ctx.guild.id) in c['id']:
                        c['id'].append(str(id))
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User {0} has been added to Mod'.format(user.mention), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break
            elif name == "pmod":
                for e in rank['pmod']:
                    if not str(id) in e['id']:
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User **{0}** is not in the Databank as Pmod'.format(user.name), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break
                    if str(ctx.guild.id) in e['id']:
                        e['id'].append(str(id))
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User {0} has been added to Pmod'.format(user.mention), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break
            with open('rank.json', 'w') as r:
                json.dump(rank, r, indent=4)


    @commands.command(pass_context = True)
    @is_lmod()
    async def removemod(self, ctx, id:int, *ramen):
        if ctx.message.author.bot==False:
            name = ' '.join(ramen)
            if not ramen:
                embed = discord.Embed(description='Please write "mod" or "pmod" to give the user a rank', color=botcolor)
                embed.timestamp = datetime.utcnow()
                await channel.send(embed=embed)
            elif name == "mod":
                for c in rank['mod']:
                    if not str(id) in c['id']:
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User **{0}** is not in the Databank as Mod'.format(user.name), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break                        
                    if str(ctx.guild.id) in c['id']:
                        c['id'].remove(str(id))
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User {0} has been removed from Mod'.format(user.mention), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break
            elif name == "pmod":
                for e in rank['pmod']:
                    if not str(id) in e['id']:
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User **{0}** is not in the Databank as Pmod'.format(user.name), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break
                    if str(ctx.guild.id) in e['id']:
                        e['id'].remove(str(id))
                        user = self.bot.get_user(id)
                        embed = discord.Embed(description='The User {0} has been removed from Pmod'.format(user.mention), color=botcolor)
                        embed.timestamp = datetime.utcnow()
                        await ctx.channel.send(embed=embed)
                        break
            with open('rank.json', 'w') as r:
                json.dump(rank, r, indent=4)



##########################################################################################################################

    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def setchannel(self, ctx, setchannel:discord.TextChannel):
        if ctx.message.author.bot==False:
            guild = ctx.message.guild
            active = 'True'
            if not setchannel:
                msg = await ctx.channel.send("Please provide a channelname")
                await asyncio.sleep(10)
                await msg.delete()
                return
            channel = setchannel
            channel_id = str(channel.id)
            for current_global in gc['global']:
                if current_global['id'] == guild.id:
                    current_global['channelname'].clear()
                    current_global['channelname'].append(channel.name)
                    current_global['channelid'].clear()
                    current_global['channelid'].append(channel_id)
                    current_global['enable'].clear()
                    current_global['enable'].append(active)
                    break
            else:
                gc['global'].append({
                'name':guild.name,
                'id':guild.id,
                'enable': [active],
                'channelname': [channel.name],
                'channelid': [channel_id]
                })
            with open('chat.json','w+') as w:
                json.dump(gc,w, indent=4)
                msg = await ctx.channel.send("The channel {0} has been setted as globalchat".format(setchannel.mention))
            with open('chat.json', encoding='utf-8') as r:
                rank = json.load(r) 
                await asyncio.sleep(60)
                await msg.delete()

    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def clearchannel(self, ctx):
        if ctx.message.author.bot==False:
            guild = ctx.message.guild
            active = 'False'
            for current_global in gc['global']:
                if current_global['id'] == guild.id:
                    current_global['channelname'].clear()
                    current_global['channelid'].clear()
                    current_global['enable'].clear()
                    current_global['enable'].append(active)
                    break
            with open('chat.json','w+') as w:
                json.dump(gc,w, indent=4)
                msg = await ctx.channel.send("The globalchannel has been resetted")
            with open('chat.json', encoding='utf-8') as r:
                rank = json.load(r) 
                await asyncio.sleep(60)
                await msg.delete()
				
		
				
   
         
##########################################################################################################################

    @commands.command(pass_context = True)
    @is_vale()
    async def addrank(self, ctx, id:int, *ramen):
        if ctx.message.author.bot==False:
            with open('rank.json', encoding='utf-8') as r:
                rank = json.load(r)
            name = ' '.join(ramen)
            if name == "vips":
                for s in self.bot.guilds:
                    if str(id) == str(s.id):
                        for a in rank['vips']:
                            if str(ctx.guild.id) in a['id']:
                                pass
                            elif not str(ctx.guild.id) in a['id']:
                                a['id'].append(str(id))
                                server  = await self.client.get_guild(id)
                                embed1.add_field(name='<:Neko_Logo:549531102117625866>__Server Info__<:Neko_Logo:549531102117625866>', value='The Server has been added as VIP Server to the Database', inline=False)
                                embed1.add_field(name='Name:', value='{}'.format(server.name), inline=True)
                                embed1.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                                embed1.set_thumbnail(url="{0}".format(server.icon_url))
                                await ctx.channel.send(embed=embed)	
                                with open('rank.json','w+') as m:
                                    json.dump(rank,m, indent=4)
                                break
                            else:
                                rank['vips'].append({
                                'id': [str(id),]
                                })
                                server  = await self.client.get_guild(id)
                                embed1.add_field(name='<:Neko_Logo:549531102117625866>__Server Info__<:Neko_Logo:549531102117625866>', value='The Server has been added as VIP Server to the Database', inline=False)
                                embed1.add_field(name='Name:', value='{}'.format(server.name), inline=True)
                                embed1.add_field(name='Server ID:', value='{}'.format(server.id), inline=True)
                                embed1.set_thumbnail(url="{0}".format(server.icon_url))
                                await ctx.channel.send(embed=embed)	
                                with open('rank.json','w+') as m:
                                    json.dump(rank,m, indent=4)
                                break
                        break
            elif name == "dev":
                for b in rank['dev']:
                    if str(id) in b['id']:
                        pass
                    if not str(id) in b['id']:
                        b['id'].append(str(id))
                        break
                    else:
                        rank['dev'].append({
                        'id': [str(id),]
                        })
            elif name == "vip":
                for d in rank['vip']:
                    if str(id) in d['id']:
                        pass
                    if not str(id) in d['id']:
                        d['id'].append(str(id))
                        break
                    else:
                        rank['vip'].append({
                        'id': [str(id),]
                        })

            elif name == "lmod":
                for f in rank['lmod']:
                    if str(id) in f['id']:
                        pass
                    if not str(id) in f['id']:
                        f['id'].append(str(id))
                        break
                    else:
                        rank['lmod'].append({
                        'id': [str(id),]
                        })
            elif name == "partner":
                for f in rank['partner']:
                    if str(id) in f['id']:
                        pass
                    if not str(id) in f['id']:
                        f['id'].append(str(id))
                        break
                    else:
                        rank['lmod'].append({
                        'id': [str(id),]
                        })
            with open('rank.json', 'w') as r:
                json.dump(rank, r, indent=4)


























def setup(bot):
    bot.add_cog(chat(bot))
			
def get_xp(user_id:str):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['exp']
    else:
        return 0


def get_lvl(user_id:str):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['level']
    else:
        return 0	
			
        
			
