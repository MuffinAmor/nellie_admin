import discord
from discord.ext import commands
from datetime import datetime
import asyncio
import json
import os



os.chdir(r'/home/pi/Nellie/commands/data')

if os.path.isfile("reports.json"):
    with open('reports.json', encoding='utf-8') as f:
        report = json.load(f)
else:
    report = {}
    report['users'] = []
    with open('reports.json','w+') as f:
        json.dump(report , f, indent=4)	

client = commands.Bot(command_prefix='nl!')

botcolor = 0xfffe00

pass_list = ['547124033410564116']

client.remove_command('help')


def is_vale():
    def predicate(ctx):
        return ctx.message.author.id in ["474947907913515019", "486988989262462991"]

    return commands.check(predicate)


class warn:
    def __init__(self, client):
        self.client = client
		
    @client.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def warn(self, ctx,  user:discord.User,  *reason:str):
      if not reason:
        msg = await self.client.say("Please provide a reason")
        return
      reason = ' '.join(reason)
      for current_user in report['users']:
        if current_user['id'] == user.id:
          current_user['reasons'].append(reason)
          break
      else:
        report['users'].append({
          'id':user.id,
          'reasons': [reason,]
        })
      with open('reports.json','w+') as f:
        json.dump(report,f, indent=4)
        neko_log = discord.utils.get(ctx.message.server.channels, name="neko_log")
        embed = discord.Embed(description='{0} has been reported.'.format(user), color=botcolor)
        await self.client.say(ctx.message.channel, embed=embed)
        server = self.client.get_server('575378478573289472')#NekoCodingStaffTeam
        channel = discord.utils.get(server.channels, name="warn_log", type=discord.ChannelType.text)
        for current_user in report['users']:
            if user.id == current_user['id']:
                embed1 = discord.Embed(title="Warning".format(user.name), color=0xff0000)
                embed1.add_field(name="Author", value=ctx.message.author, inline=True)
                embed1.add_field(name="Author ID", value=ctx.message.author.id, inline=True)
                embed1.add_field(name="Warned User:", value=user.mention, inline=True)
                embed1.add_field(name="User ID", value=user.id, inline=True)
                embed1.add_field(name="Warned for:", value=reason, inline=True)
                embed1.add_field(name="Server", value=user.server, inline=True)
                embed1.add_field(name="Warnings", value="{0} has been reported {1} times for:\n {2}".format(user.mention, len(current_user['reasons']),', '.join(current_user['reasons']) ), inline=False)
                embed1.set_thumbnail(url=user.avatar_url)
                msg = await self.client.send_message(channel, embed=embed1)
                break
        else:
            embed2 = discord.Embed(title="Warning".format(user.name),color=0xff0000)
            embed2.add_field(name="Author", value=ctx.message.author, inline=True)
            embed2.add_field(name="Author ID", value=ctx.message.author.id, inline=True)
            embed2.add_field(name="Warned User:", value=user.mention, inline=True)
            embed2.add_field(name="User ID", value=user.id, inline=True)
            embed2.add_field(name="Warned for:", value=reason, inline=True)
            embed2.add_field(name="Server", value=user.server, inline=True)
            embed2.add_field(name="Warnings", value="{0} has never been reported".format(user.mention), inline=False)
            embed2.set_thumbnail(url=user.avatar_url)
            msg = await self.client.send_message(channel, embed=embed2)
			
    @client.command(pass_context = True)
    @is_vale()
    @commands.cooldown(3, 60, commands.BucketType.user)
    async def delwarns(self, ctx,  user:discord.User):
        for current_user in report['users']:
            if current_user['id'] == user.id:
                current_user['reasons'].clear()
                current_user['reasons'].append("None")
                break
        else:
            msg = await self.client.send_message("Ops, i have no dates about this user")
            await asyncio.sleep(60)
            await self.client.delete_message(msg)	
        with open('reports.json','w+') as f:
            json.dump(report , f, indent=4)	
            msg = await self.client.say("The Warnings from {0} has been deleted".format(user.name))
########################################################################################################################
    @client.command(pass_context = True)
    async def warnings(self, ctx, user:discord.User):
        for current_user in report['users']:
            if user.id == current_user['id']:
                await self.client.say("{0} has been reported {1} times for:\n {2}".format(user.mention, len(current_user['reasons']),', '.join(current_user['reasons']) ))
                break
        else:
            await self.client.say("{0} has never been reported".format(user.name)) 
		
    @client.command(pass_context = True)
    async def warncheck(self, ctx):
        embed = discord.Embed(title="Warn Info", description="", color=botcolor)
        msg = await self.client.send_message(ctx.message.channel, embed=embed)
        await self.client.add_reaction(msg, "⏩")
        await self.client.add_reaction(msg, "❎")
        await asyncio.sleep(0.5)
        for user in ctx.message.server.members:
            for current_user in report['users']:
                if user.id == current_user['id']:
                    embed = discord.Embed(title="Warn Info", description="", color=botcolor)
                    embed.add_field(name="Warned User:", value="{0}".format(user.name), inline=True)
                    embed.add_field(name="Warns", value=len(current_user['reasons']), inline=True)
                    embed.add_field(name="Reasons", value=', '.join(current_user['reasons']), inline=False)
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    msg = await self.client.edit_message(msg, embed=embed)
                    await self.client.add_reaction(msg, "⏩")
                    await self.client.add_reaction(msg, "❎")
                    await asyncio.sleep(0.5)
                    await self.client.wait_for_reaction(['⏩'], message=msg)
                    await self.client.remove_reaction(msg, "⏩", ctx.message.author)
        else:
                await self.client.delete_message(msg)
                msg = await self.client.say("No more warned User")
                return				
########################################################################################################################		
    @client.command(pass_context=True)
    async def userinfo(self, ctx, user: discord.User):
        user_passed1 = (ctx.message.timestamp - user.joined_at).days
        user_created1 = (ctx.message.timestamp - user.created_at).days
        l = list(permi for permi, value in user.server_permissions if str(value)== 'True')
        i = '\n📍 '.join(l)
        rl = list(role.mention for role in user.roles if not role.name == "@everyone")
        r = ', '.join(rl) 
        for current_user in report['users']:
            if user.id == current_user['id']:
                embed = discord.Embed(title="{}'s info".format(user.name), description="Here is the Userprofile", color=user.top_role.color)
                embed.add_field(name="Name", value=user.name, inline=True)
                embed.add_field(name="ID", value=user.id, inline=True)
                embed.add_field(name="Discriminator", value="#{0}".format(user.discriminator), inline=True)
                embed.add_field(name="Status", value=user.status, inline=True)
                embed.add_field(name="Highest Role", value=user.top_role, inline=True)
                embed.add_field(name="Roles", value=r, inline=True)
                embed.add_field(name="Warnings", value="{0} has been reported {1} times for:\n {2}".format(user.mention, len(current_user['reasons']),', '.join(current_user['reasons']) ), inline=False)
                embed.add_field(name='User permissions:', value='📍 {0}'.format(i), inline=False)
                embed.add_field(name="Joined at:", value=("{} ({} days ago!)".format(user.joined_at.strftime("%d %b %Y %H:%M"), user_passed1)), inline=False)
                embed.add_field(name="Created at:", value=("{} ({} days ago!)".format(user.created_at.strftime("%d %b %Y %H:%M"), user_created1)), inline=False)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                msg = await self.client.send_message(ctx.message.channel, embed=embed)
                break
        else:
                embed = discord.Embed(title="{}'s info".format(user.name), description="Here is the Userprofile", color=user.top_role.color)
                embed.add_field(name="Name", value=user.name, inline=True)
                embed.add_field(name="ID", value=user.id, inline=True)
                embed.add_field(name="Discriminator", value="#{0}".format(user.discriminator), inline=True)
                embed.add_field(name="Status", value=user.status, inline=True)
                embed.add_field(name="Highest Role", value=user.top_role, inline=True)
                embed.add_field(name="Roles", value=r, inline=True)
                embed.add_field(name="Warnings", value="{0} has never been reported".format(user.name), inline=False)
                embed.add_field(name='User permissions:', value='📍 {0}'.format(i), inline=False)
                embed.add_field(name="Joined at:", value=("{} ({} days ago!)".format(user.joined_at.strftime("%d %b %Y %H:%M"), user_passed1)), inline=False)
                embed.add_field(name="Created at:", value=("{} ({} days ago!)".format(user.created_at.strftime("%d %b %Y %H:%M"), user_created1)), inline=False)
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                msg = await self.client.send_message(ctx.message.channel, embed=embed)
########################################################################################################################
    @client.command(pass_context=True)
    async def finduser(self, ctx, *find):
        userId = ' '.join(find)
        hi = await self.client.get_user_info(userId)
        for find in report['users']:
            if hi.id == find['id']:
                embed = discord.Embed(title='__Discord ID finder__',
                                      description="Username: {0}\n"
                                                  "User ID: {1}\n" 
                                                  "Created at: {2}\n"
                                                  "{3} warnings for: {4}" .format(hi, userId, hi.created_at, len(find['reasons']), ', '.join(find['reasons'])),
                    color=botcolor)
                embed.set_thumbnail(url=hi.avatar_url)	
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author))
                embed.timestamp = datetime.utcnow()
                msg = await self.client.say(embed=embed)
                break  
        else:
                embed = discord.Embed(title='__Discord ID finder__', description='Username: {0}\n' 'User ID: {1}\n' 'Created at: {2}\n' 'No warnings'.format(hi, userId, hi.created_at), color=botcolor)
                embed.set_thumbnail(url=hi.avatar_url)	
                embed.set_footer(text='Message was requested by {}'.format(ctx.message.author))
                embed.timestamp = datetime.utcnow()
                msg = await self.client.say(embed=embed)
                   	
def setup(client):
    client.add_cog(warn(client))